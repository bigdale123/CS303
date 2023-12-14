import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import climbStairs

ofile = open('output', 'w')
ofile.write(str(climbStairs(0)) + " ")
ofile.write(str(climbStairs(1)) + " ")
ofile.write(str(climbStairs(2)) + " ")
ofile.write(str(climbStairs(3)) + " ")
ofile.close()
