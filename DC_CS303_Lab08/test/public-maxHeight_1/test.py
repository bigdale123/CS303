import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import buildBST, maxHeight


key_val = []
root = buildBST(key_val);


ofile = open('output', 'w')
ofile.write(str(maxHeight(root)))
ofile.close()
