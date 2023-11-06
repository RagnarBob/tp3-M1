import random
import string

print("******************PATI CHENN*******************")
print("nimewo 1 :")
chenn = "King Ragnar"
print(chenn.lower(),"\n")

print("nimewo 2 :")
var = "ayibobo ayiti"
print(var.split(),"\n")

print("nimewo 3 :")#nimewo 3
let = "the king ragnar"
print(let.title(),"\n")

print("nimewo 4 :")#nimewo 4
chenn_nan = "mwen se yon Viking"
varyab = chenn_nan.split()
new_chenn = ""
for el in varyab:
    new_chenn += el[0]
print(new_chenn,"\n")    

print("nimewo 5 :")#nimewo 5
karak = "madame"
print(karak.replace("a","@"),"\n")

print("nimewo 6 :")#nimewo 6
vvar = "ThamArt"
vvar_inv = vvar[::-1]
print(vvar_inv.upper(),"\n")

print("nimewo 7 :")#nimewo 7
indexo = "Elle est mignone"
ver = indexo.index("e")
print(ver,"\n")

print("nimewo 8 :")#nimewo 8
chaine = "Elle est une amie speciale et je l'aime"
cpt = 0
for karak in chaine:
    if karak == "e":
        cpt+=1
print("kantite (e) ki genyen an se:",cpt,"\n")   

print("nimewo 9 :")#numewo 9
Thamie = "Ayiti kapab avanse"
yes = 0
liste = []
for kar in Thamie:
    if kar == "a":
        liste.append(str(yes))
    yes+=1 
#soti = " , ".join(liste)
print(liste,"\n")   

print("nimewo 10 :")#nimewo 10
bob = "je suis Ragnar Bob the king"
king = bob.replace(" ","")
doll = len(king) 
ragnar = str(doll)
print(king+ragnar+"\n")

print("****************PATI LIS*****************")
print("nimewo 1 :")
n=20
liss = []
for i in range(n+1):
    if i % 2 == 0:
        liss.append(i)
print(liss)        

print("nimewo 2 :")
lis_antye = [1,2,3,4,5,6,7]
lis_chenn = list(map(str,lis_antye))
print(lis_chenn)

print("nimewo 3 :")
list_miniskil = ["king","ragnar","bob"]
list_majiskil = [el.upper() for el in list_miniskil]
print(list_majiskil)

print("nimewo 4 :")
li = [2,3,4,5,6,9,12,15,18,19,22,34,33,60]
new_list = [li[i] for i in range(0,len(li),3)]
print(new_list)

print("nimewo 5:")
list_group = [2,3,4,5,20,40,46,48,50]
new_list_group = [tuple(list_group[i:i+3]) for i in range(0,len(list_group),3)]
print(new_list_group)

print("nimewo 6:")
list_doublon = [1,2,3,2,3,4,4,4,5,6,6,7,2]
lis_san_doublon = list(set(list_doublon))
print(lis_san_doublon)

print("nimewo 7:")
list_1 = [1,2,4,5,6,7,8]
list_2 = [1,5,3,9,10,12]
list_commun = list(set(list_1) & set(list_2))
print(list_commun)

print("nimewo 8:")
list_1 = [1,2,4,5,6,7,8]
list_2 = [1,5,3,9,10,12]
nouvo_liste = list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))
print(nouvo_liste)

print("nimewo 9:")
dict = {'bob':'4','ragnar':'6'}
kle = list(dict.keys())
vale = list(dict.values())
print(kle)
print(vale)

print("nimewo 10:")
list_1 = [1,2,4,5,6,7,8]
list_2 = [1,5,3,9,10,12]
list_3 = [2,3,4,5,12,14]
reunion = set(list_1) | set(list_2) | set(list_3)
new_liste = list(reunion)
print(new_liste,"\n")

print("****************PATI dict*****************")
print("nimewo 1:")
dictio = {'king':'ragnar','bob':'doll'}
valeur = list(dictio.values())
print(valeur)

"""print("nimewo 2:")
user = input("antre yon bgy :")
if user.startswith("{") and user.endswith("}"):
    print("saw antre an gen akolad ni devan ni deye")
else:
    print("li pa gen akolad ni devan ni deye") """

print("nimewo 3:")
dik = {'the':'king','bob':'ragnar'}  
for key in dik.keys():
    print(key) 

print("nimewo 4:")
dikk = {'the':'king','bob':'ragnar'}
for valeur in dikk.values():
    print(valeur)

print("nimewo 5:")
diks = {'the':'king','bob':'ragnar'}  
kopi_diks = diks.copy()
print(kopi_diks)  

print("nimewo 6:")
dic = {'the':'king','bob':'ragnar','doll':12,"maken":34}
nouvo_dict = {key:("_" + vale if isinstance(vale,str) else vale) for key,vale in dic.items()}
print(nouvo_dict)

print("nimewo 7:")
dictt = {'the':'2','bob':'3','doll':'bob',"maken":'king'}
new_dict = {kle : valeu for kle,valeu in dictt.items() if valeu.isdigit()}
print(new_dict)

print("nimewo 8:")
dicttt = {'the':'2','bob':'3','doll':'bob',"maken":'king'}
tipl = list(dicttt.items())
print(tipl)

"""print("nimewo 9:")
tiplll = [('the', '2'), ('bob', '3'), ('doll', 'bob'), ('maken', 'king')]
dikkk = 
print(dikkk)"""

print("nimewo 10:")
diksss = {'the':'king','bob':'ragnar','doll':10,"maken":30}
dictt = {'the':'2','bob':'3','doll':'12',"maken":'6'}
dict_tot = {}
for kle,vale in dictt.items():
    if kle in dict_tot:
        if isinstance(vale,int):
            if isinstance(dict_tot[kle],int): 
                dict_tot[kle] += int(vale)  
            else:
                dict_tot[kle] = int(vale)
        elif isinstance(vale,(list,str,set)):
            if isinstance(dict_tot[kle],(list,str,set)):
                dict_tot[kle] += vale
            else:
                dict_tot[kle] = vale
        else:
            dict_tot[kle] = vale
    else:
        dict_tot[kle] = vale                

print(dict_tot)

print("****************PATI FONCTION*****************")
print("nimewo 1:")
def retounen(mo):
    inves = mo[::-1]
    return inves
inverse = retounen("doll")
print(inverse)

print("nimewo 2:")
def jenere (n):
    kod = ''.join(random.choice(string.ascii_letters) for _ in range(n))
    return kod
n = 10 
kod_aleyatwa = jenere(n)
print(kod_aleyatwa)

print("nimewo 3:")
def aleatwa(n):
    karakte = string.ascii_letters
    kood = ''.join(random.sample(karakte,n))
    return kood
n = 10
ko_ale = aleatwa(n)
print(ko_ale)

print("nimewo 4:")
def aleat(n):
    alphanumerik = string.ascii_letters + string.digits
    num = ''.join(random.choice(alphanumerik) for _ in range(n))
    return num
n = 10 
nime = aleat(n)
print(nime)

print("nimewo 5:")


print("nimewo 6:")
def separ(moo):
    separe = '-'.join(moo)
    return separe
name = "Thamie"
sepa = separ(name)
print(sepa)








