"""Search/read the pinned upstream text snapshot; never execute upstream files."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    sub.add_parser('verify')
    search = sub.add_parser('search')
    search.add_argument('query')
    search.add_argument('--limit', type=int, default=12)
    read = sub.add_parser('read')
    read.add_argument('source')
    read.add_argument('path')
    read.add_argument('--start', type=int, default=1)
    read.add_argument('--lines', type=int, default=100)
    args = parser.parse_args()
    lock = json.loads((ROOT/'references/sources.lock.json').read_text(encoding='utf-8'))
    with zipfile.ZipFile(ROOT/'assets/upstream-reference.zip') as archive:
        if args.command == 'list':
            print(json.dumps([{'id':s['id'],'commit':s['commit'],'license':s['license'],
                               'snapshot_files':len(s['snapshot_files'])} for s in lock['sources']],indent=2))
        elif args.command == 'verify':
            bad, total = [], 0
            for s in lock['sources']:
                for item in s['snapshot_files']:
                    name = s['id']+'/'+item['path']
                    try:
                        digest = hashlib.sha256(archive.read(name)).hexdigest()
                        if digest != item['sha256']:
                            bad.append(name)
                    except KeyError:
                        bad.append(name)
                    total += 1
            expected = {s['id']+'/'+f['path'] for s in lock['sources'] for f in s['snapshot_files']}
            bad.extend(sorted(set(archive.namelist())-expected))
            print(json.dumps({'checked':total,'mismatches':bad},indent=2))
            return 1 if bad else 0
        elif args.command == 'search':
            matches = []
            for name in archive.namelist():
                text = archive.read(name).decode('utf-8')
                lines = text.splitlines()
                for i, line in enumerate(lines):
                    if args.query.casefold() in (name+' '+line).casefold():
                        matches.append({'path':name,'line':i+1,'text':line[:220]})
                        break
                if len(matches) >= max(1,args.limit):
                    break
            print(json.dumps(matches,ensure_ascii=False,indent=2))
        else:
            if args.start < 1 or not 1 <= args.lines <= 500:
                parser.error('--start >=1 and --lines between 1 and 500')
            name = args.source+'/'+args.path
            if name not in archive.namelist():
                parser.error('not in offline snapshot; fetch only from locked source commit')
            lines = archive.read(name).decode('utf-8').splitlines()
            for i in range(args.start-1,min(len(lines),args.start-1+args.lines)):
                print(f'{i+1}: {lines[i]}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
