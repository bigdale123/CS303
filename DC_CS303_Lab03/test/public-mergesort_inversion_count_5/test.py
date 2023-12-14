import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import inversionCount_MergeSort

array = [100,90,80,70,60,50,40,30,20,10,9,8,7,6,5,4,3,2,1] 
addresult = str(inversionCount_MergeSort(array))

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
