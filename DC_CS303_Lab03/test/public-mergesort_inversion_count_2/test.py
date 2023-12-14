import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import inversionCount_MergeSort

array = [1,2,3,4,5] 
addresult = str(inversionCount_MergeSort(array))

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
