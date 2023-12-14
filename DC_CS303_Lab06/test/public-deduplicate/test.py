import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import deduplicate


with open("Input1.txt") as f:
    data = f.read().strip().split()

array = [int(x) for x in data]
res1 = deduplicate(array)


ofile = open('output', 'w')
ofile.write(str(res1))
ofile.close()
