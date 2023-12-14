import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import twoSum

ofile = open('output', 'w')
ofile.write(str(twoSum([2, 7, 11, 15], 9)))
ofile.close()
