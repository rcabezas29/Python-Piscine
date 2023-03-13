import sys

try:
    if sys.argv.__len__() != 3:
        raise ValueError('ERROR')
    s = sys.argv[1]
    n = int(sys.argv[2])
    
    words = s.split(' ')
    ret = []
    for w in words:
        if len(w) >= n:
            ret.append(w.replace(',', '').replace('.', ''))
    print(ret)
except ValueError as e:
    print(e)
    exit(1)