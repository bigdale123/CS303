import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import climbStairs

ofile = open('output', 'w')
ofile.write(str(climbStairs(0)) + " ")
ofile.write(str(climbStairs(1)) + " ")
ofile.write(str(climbStairs(2)) + " ")
ofile.write(str(climbStairs(3)) + " ")
ofile.write(str(climbStairs(10)) + " ")
ofile.write(str(climbStairs(20)) + " ")
ofile.write(str(climbStairs(30)) + " ")
ofile.write(str(climbStairs(40)) + " ")
ofile.write(str(climbStairs(50)) + " ")
ofile.write(str(climbStairs(60)) + " ")
ofile.write(str(climbStairs(70)) + " ")
ofile.write(str(climbStairs(80)) + " ")
ofile.close()
