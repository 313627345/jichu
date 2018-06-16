#！usr/bin/python3

import sys
sys.setrecursionlimit(1000000)
def down(i):
    if i<0:
        return
    else:
        print(i)
        down(i-1)
