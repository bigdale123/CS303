import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import buildBST, inorder_traversal, search


key_val = []
array = []
root = buildBST(key_val);
array = inorder_traversal(root);

addresult = ""
for i in range(len(array)):
    addresult = addresult+" "+str(array[i])

addresult = addresult+" "+str(search(root, 465345012))
addresult = addresult+" "+str(search(root, 0))
addresult = addresult+" "+str(search(root, 9200194267))
addresult = addresult+" "+str(search(root, 11111))
addresult = addresult+" "+str(search(root, 50201921))
addresult = addresult+" "+str(search(root, 5000008124))

ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
