import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import computeFibonacci

ofile = open('output', 'w')
ofile.write(str(computeFibonacci(0)) + " ")
ofile.write(str(computeFibonacci(2)) + " ")
ofile.write(str(computeFibonacci(5)) + " ")
ofile.write(str(computeFibonacci(31)) + " ")
ofile.write(str(computeFibonacci(11)) + " ")
ofile.write(str(computeFibonacci(21)) + " ")
ofile.write(str(computeFibonacci(31)) + " ")
ofile.write(str(computeFibonacci(41)) + " ")
ofile.write(str(computeFibonacci(51)) + " ")
ofile.write(str(computeFibonacci(61)) + " ")
ofile.write(str(computeFibonacci(71)) + " ")
ofile.write(str(computeFibonacci(79)) + " ")
ofile.close()
