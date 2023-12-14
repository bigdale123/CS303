import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import buildBST, inorder_traversal, search


key_val = [
(9800910632,"ct"),
(4700007710,"LB"),
(8811323523,"The"),
(9400000351,"oz"),
(251052483,5248),
(416001042,"Andrea"),
(1000001639,"tt"),
(9200114241,"FLAT"),
(8291001263,"LBS"),
(888884051,"lbs"),
(50755592,"Celery"),
(772005456,"Make-Your-Own"),
(40615868,"3"),
(6129003793,"oz"),
(9200014749,"Greeting"),
(50285662,"Dove"),
(2062672676,"x"),
(3126006284,"LBS"),
(416013878,"Daniel Janke, Holly Cole - Big Dance - CD"),
(9281026273,"Bass"),
(8100000340,"OZ"),
(416002704,"Favorite"),
(649370939,"OTB"),
(9200124943,"HANDLE"),
(2034980,"PORK"),
(4300957774,"KOOL"),
(9531103419,"FO"),
(416014387,"Anthea"),
(2550006846,"oz."),
(8888320050,"Rayman"),
(9200057579,"ct"),
(416012215,"Bozart"),
(8236495171,"pieces"),
(5000008124,"ct"),
(10086510645,"Dreamcast"),
(4183110402,"oz"),
(42077091,"OZ"),
(9200086333,"Greeting"),
(870209435,"oz"),
(8888651611,"FarCry"),
(111000005,"CH."),
(8925381280,"66-100"),
(9034200059,"Hub"),
(6269857010,"SMC7004BR"),
(4000042084,"ct"),
(7954161344,"B/B"),
(621250,"1X2X36"),
(8346045747,"OZ"),
(318647089,"CT"),
(9200220461,"WHT"),
(836200322,"ct"),
(7120308740,"Gallon"),
(768234792,"AC-Shout"),
(1620002658,"oz"),
(4835812227,"MANAGER"),
(7323115824,"MUSCLAEMAN"),
(152314505,"HARDCOVER"),
(7195934509,"ct"),
(9200189812,"Home"),
(3338118546,"GRAPRFRUIT"),
(8811290528,"MOS"),
(7201879077,"*8388"),
(9100220,"CA"),
(9200069480,"ct"),
(251760036,"76003"),
(2600006161,"oz"),
(9200189980,"Home"),
(9200194267,"GREETING"),
(9281028963,"HAIRDO"),
(10086640328,"Otogi:"),
(8236682427,"zinc"),
(8132002503,"Paperback"),
(8457003407,"ml"),
(2058101555,"CHOICE"),
(50201921,"Trebor"),
(9200193581,"LARGE"),
(55280396,"ct"),
(7199077950,"oz"),
(50011339,"Pukka"),
(8811068523,"SOUNDTRACK"),
(253005005,"0.75"),
(296128570,"ct"),
(8811166823,"IMMATURE"),
(9200022386,"ct"),
(1439900411,"ML"),
(4835255420,"MANAGER"),
(8888610274,"Anne"),
(9200059108,"ct"),
(450295841,"ct"),
(921000066,"Reach"),
(45466939,"PRTY"),
(1691852602,"Novopen"),
(9200201248,"Christmas"),
(9202559,"PL"),
(8590499501,"MD"),
(450470156,"S"),
(3350000201,"Little"),
(10000209679,"oz"),
(465345012,"Falcon"),
(2200008695,"Count"),
(9200095908,"GREETING"),
(9200011618,"ct"),
(416000083,"Hitchhiker"),
(42069775,"Extra, sweet mint sugarfree gum"),
(8888652137,"The"),
(810082203,"ct"),
(200059006,"ct"),
(46934611,"SHEET"),
(0,"SHEET1"),
(2,"SHEET2"),
]

root = buildBST(key_val);
array = inorder_traversal(root);

addresult = ""
for i in range(len(array)):
    addresult = addresult+" "+str(array[i])

addresult = addresult+" "+str(search(root, 465345012))
addresult = addresult+" "+str(search(root, 9200022386))
addresult = addresult+" "+str(search(root, 9200194267))
addresult = addresult+" "+str(search(root, 8236682427))
addresult = addresult+" "+str(search(root, 50201921))
addresult = addresult+" "+str(search(root, 5000008124))
addresult = addresult+" "+str(search(root, 46934611))
addresult = addresult+" "+str(search(root, 0))

ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
