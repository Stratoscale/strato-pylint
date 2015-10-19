import re
import sys
import os.path
import fileinput

MINOR_CODES = ['[R0801(duplicate-code)]',
               '[W0511(fixme)]']

def absoluteFilename(fname):
    if fname.startswith('racktests'):
        return fname
    if fname.startswith('strato/runtime/abacusapi'):
        return '../abacusapi/py/'+fname
    if fname.startswith('strato_kv'):
        return 'infra/'+fname
    return 'py/'+fname

def formatIssue(line, absFname, minor=False):
    code, fname, lineno, desc = line.split(':', 3)
    color = '\033[33m' if minor else '\033[33;1m'
    colorFname = '%s%s\033[0m' % (color, absFname)
    code = '%-24s' % (code[:-2].split('(')[-1])
    if 'duplicate-code' in code:
        desc = re.sub('Similar lines in (\d)+ files',
                      'Similar lines in some files',
                      desc)
    return ' '.join((code, colorFname, lineno, desc))

def parsePylintError(lines, minor, seen):
    code, fname, lineno, desc = lines[0].split(':', 3)
    absFname = absoluteFilename(fname)
    if not os.path.isfile(absFname):
        return 0
    text = formatIssue(lines[0], absFname, True)
    if text in seen:
        return 0
    seen.add(text)
    if code in MINOR_CODES:
        minor.append(text)
        return 0
    print formatIssue(lines[0], absFname)
    return 1

seen = set()
current = None
count = 0
minor = []

args = sys.argv[1:]
useReturnCode = '--return' in args
if useReturnCode:
    args.remove('--return')

fileInput = fileinput.input(args)
for line in fileInput:
    line = line[:-1]
    if line.startswith('************* Module'):
        continue
    if line.startswith('['):
        if current is not None:
            count += parsePylintError(current, minor, seen)
        current = [line]
    else:
        if current is not None:
            current.append(line)
if current is not None:
    count += parsePylintError(current, minor, seen)
for issue in minor:
    print issue
print '\033[;1m%d problems and %d minor issues found\033[0m' % (count, len(minor))
if useReturnCode and count > 0:
    sys.exit(1)
