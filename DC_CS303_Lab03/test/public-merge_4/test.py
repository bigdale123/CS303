import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import Merge

L = [130,131,133,135,138,140,150,160] 
R = [1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150]
combined = [None] * (len(R) + len(L))
Merge(L, R, combined)

addresult = ""
for i in range(len(combined)):
    addresult = addresult+" "+str(combined[i])

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
