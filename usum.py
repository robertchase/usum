#! /usr/bin/env python
import operator


def num(value):
    f = float(value)
    try:
        i = int(value)
    except ValueError:
        return f
    return i if i == f else f


def group_by(data, cols):
    groups = {}
    for linenum, line in enumerate(data, start=1):
        toks = line.split()
        if not toks:
            continue
        try:
            names = list(toks[i-1] for i in cols)
            key = ' '.join(names)
            vcols = list(i for i in range(1, len(toks)+1) if i not in cols)
            values = list(num(toks[i-1]) for i in vcols)
            sums = groups.get(key)
            if sums and len(values) != len(sums):
                raise Exception("number of columns doesnt match key='%s'" % key)
        except Exception as e:
            raise Exception('line=%s: %s' % (linenum, str(e)))
        groups[key] = list(map(operator.add, sums, values)) if sums else values
    return groups


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='sum group by')
    parser.add_argument('groupby', nargs='*', type=int)
    args = parser.parse_args()

    groups = group_by(sys.stdin, args.groupby)

    for k, v in groups.items():
        sys.stdout.write('%s %s\n' % (k, ' '.join((str(n) for n in v))))
