import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import majorityElement


array = [11,12,11,11,11,13,13,13,13,14,14,14,15,15,15,15,673,673,673,673]



ofile = open('output', 'w')
ofile.write(str(majorityElement(array)))
ofile.close()
