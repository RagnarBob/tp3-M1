#nimewo 1
chenn = "King Ragnar"
print(chenn.lower())

#nimewo 2
var = "ayibobo ayiti"
print(var.split())

#nimewo 3
let = "the king ragnar"
print(let.title())

#nimewo 4
chenn_nan = "mwen se yon Viking"
varyab = chenn_nan.split()
new_chenn = ""
for el in varyab:
    new_chenn += el[0]
print(new_chenn)    

#nimewo 5
karak = "madame"
print(karak.replace("a","@"))

#nimewo 6
vvar = "ThamArt"
vvar_inv = vvar[::-1]
print(vvar_inv.upper())

#nimewo 7
indexo = "Elle est mignone"
ver = indexo.index("e")
print(ver)

#nimewo 8
chaine = "Elle est une amie speciale et je l'aime"
cpt = 0
for karak in chaine:
    if karak == "e":
        cpt+=1
print("kantite e ki genyen an se:",cpt)   

#numewo 9
Thamie = "Ayiti kapab avanse"
yes = 0
liste = []
for kar in Thamie:
    if kar == "a":
        liste.append(str(yes))
    yes+=1 
#soti = " , ".join(liste)
print(liste)   



"""fruit = "Ayiti kapab avanse"
liste_fruit = []

for i in range(len(fruit)):
    if fruit[i] == "a":
        liste_fruit.append(i)

print(liste_fruit)"""

"""fru="Ayiti kapab avanse"
lis=[]
ele="a"
compt=0
for el in fru:
    compt = fru.index(ele)
    lis.append(compt)
compt+=1
print(lis) """  

#nimewo 10
bob = "je suis Ragnar Bob the king"
king = bob.replace(" ","")
doll = len(king) 
ragnar = str(doll)
print(king+ragnar)



