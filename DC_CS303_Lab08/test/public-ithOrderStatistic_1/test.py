import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import buildBST, ithOrderStatistic



root = buildBST([]);
ofile = open('output', 'w')
ofile.write(str(ithOrderStatistic(root,3)))
ofile.close()
