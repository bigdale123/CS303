import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import majorityElement


array=[]


ofile = open('output', 'w')
ofile.write(str(majorityElement(array)))
ofile.close()
