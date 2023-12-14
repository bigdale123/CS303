import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import Merge

L = [] 
R = [130,131,133,135,138]
combined = [None] * (len(R) + len(L))
Merge(L, R, combined)

addresult = ""
for i in range(len(combined)):
    addresult = addresult+" "+str(combined[i])

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
