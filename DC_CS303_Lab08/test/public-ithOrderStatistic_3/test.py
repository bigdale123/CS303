import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import buildBST, ithOrderStatistic


key_val = [
(0,"ct"),
(1,"LB"),
(2,"The"),
(3,"oz"),
(4,5248),
(5,"Andrea"),
(6,"tt"),
(7,"FLAT"),
(8,"LBS")
]

root = buildBST(key_val);
i=1

ofile = open('output', 'w')
ofile.write(str(ithOrderStatistic(root,i)))
ofile.close()
