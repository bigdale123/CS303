import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import inversionCount_Merge

L = [3,7,10,14,18,19] 
R = [20,211,216,217,223,225]
combined = [None] * (len(R) + len(L))
ic = str(inversionCount_Merge(L, R, combined))


# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(ic)
ofile.close()
