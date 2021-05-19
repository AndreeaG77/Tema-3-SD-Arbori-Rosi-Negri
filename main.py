class nod:
    def __init__(self,val):
        self.left= None
        self.right= None
        self.color= None
        self.val= val


# Functia de inserare intr-un arbore binar de cautare
def inserare(root, val):
        if val<root.val:
            if root.left == None:
                root.left=nod(val)
                root.left.color="red"
            else:
                inserare(root.left, val)
        else:
            if root.right == None:
                root.right=nod(val)
                root.right.color="red"
            else:
                inserare(root.right, val)


# Functia de afisare a elementelor unui arbore binar de cautare in ordine crescatoare
def inordine(root):
    if root!=None:
        inordine(root.left)
        if root.val!=None:
            print(root.val)
        inordine(root.right)

# Functia de afisare a elementelor dintr-un anumit interval in ordine crescatoare
def inordine_interval(root, x, y):
    if root!=None:
        inordine_interval(root.left,x,y)
        if root.val!=None and root.val>=x and root.val<=y:
            print(root.val)
        inordine_interval(root.right,x,y)


# Functia de cautarea a unui nod in arborele binar care returneaza nodul
def cauta_val(root, val):
    if root.val==val:
        return root
    else:
        if val<root.val:
            cauta_val(root.left, val)
        else:
            cauta_val(root.right, val)


# Functia de cautare a parintelui unui nod intr-un arbore binar de cautare
def cauta_parinte(root,val):
    if val < root.val:
        if val==root.left.val:
            return root
        cauta_parinte(root.left, val)
    else:
        if val==root.right.val:
            return root
        cauta_parinte(root.right, val)


# Functia de cautare a predecesorului intr-un arbore binar de cautare
def cauta_predecesor(root,val):
    parinte=cauta_parinte(root,val)
    if parinte.val<=val:
        return parinte
    else:
        parinte=cauta_parinte(root,parinte.val)
        return parinte

# Functia de cautare a succsesorului intr-un arbore binar de cautare
def cauta_succesor(root, val):
    nod_curent= cauta_val(root,val)
    if nod_curent.right==None:
        parinte=cauta_parinte(root, val)
        if parinte.val<val:
            parinte = cauta_parinte(root, parinte.val)
        return parinte
    else:
        nod_curent=nod_curent.right
        while nod_curent.left!=None:
            nod_curent=nod_curent.left
        return nod_curent


# Functia de stergere a unui nod dintr-un arbore binar de cautare
# Aceasta functie returneaza radacina pentru cazul in care dorim sa stergem fix radacina arborelui
# In acest caz vrem sa returnam noua radacina pentru a actualiza variabila root cu care apelam toate functiile
def stergere(root, val):
    nod_curent=cauta_val(root,val)
    if nod_curent.left==None and nod_curent.right==None:
        nod_curent.val=None
    else:
        succesor=cauta_succesor(root,val)
        nod_curent.val=succesor.val
        succesor.val=None
    if root.val==val:
        return nod_curent
    else:
        return root


# Functia de inserare a unui nod intr-un arbore rosu negru
def inserare_rbt(root,val):
    inserare(root,val)
    fiu=cauta_val(root,val)
    nod_curent=fiu
    parinte=cauta_parinte(root,val)
    while nod_curent!=root and parinte.color=="red":
        k=0
        bunic=cauta_parinte(root,parinte.val)
        if bunic==root:
            k=1
        if bunic.left==parinte:
            aux=bunic.right
            if aux.color=="red":
                bunic.color="red"
                parinte.color="black"
                aux.color="black"
                nod_curent=bunic
            else:
                if nod_curent==parinte.right:
                    bunic.left=fiu
                    parinte.right=fiu.left
                    fiu.left=parinte
                    nod_curent=fiu.left
                bunic.color="red"
                bunic.left.color="black"
                bunic.left=fiu.right
                fiu.right=bunic
                nod_curent=fiu
        else:
            aux=bunic.left
            if aux.color=="red":
                bunic.color = "red"
                parinte.color = "black"
                aux.color = "black"
                nod_curent = bunic
            else:
                if nod_curent==parinte.left:
                    bunic.right = fiu
                    parinte.left = fiu.right
                    fiu.right = parinte
                    nod_curent = fiu.right
                bunic.color = "red"
                bunic.right.color = "black"
                bunic.right = fiu.left
                fiu.left = bunic
                nod_curent = fiu
        if k==1:
            root=fiu

    root.color="black"

# Functie de cautare care returneaza 0 sau 1 daca a gasit sau nu nodul in arborele binar de cautare
def cauta_val1(root,val):
    if root==None:
        return 0
    if root.val==val:
        return 1
    else:
        if val<root.val:
            cauta_val1(root.left, val)
        else:
            cauta_val1(root.right, val)



# Citesc operatiile dintr-un fisier
# 1: operatie de inserare a valorii x
# 2: operatie stergere a valorii x
# 3: operatia afiseaza 0 sau 1 daca valoarea x exista in arbore
# 4: operatia de cautare a predecesorului valorii x in arbore
# 5: operatia de cautare a succesorului valorii x in arbore
# 6: operatia de afisare a elementelor sortate din arbore cu proprietatea ca x<=element<=y
f=open("intrare")
n = int(f.readline())
lista_op=[]
for i in range(0,n):
    aux=[int(x) for x in f.readline().split()]
    lista_op.append(aux)
f.close()
ok=0
for element in lista_op:
    if element[0]==1:
        if ok==0:
            ok=1
            rad=nod(element[1])
            rad.color="black"
        else:
            #inserare_rbt(rad, element[1])
            inserare(rad,element[1])
    if element[0]==2:
        if cauta_val1(rad,element[1])==1:
            rad=stergere(rad,element[1])
    if element[0]==3:
        if ok==0:
            print("Rezultatul cautarii elementului ", element[1], ": ", 0)
        else:
            print("Rezultatul cautarii elementului ", element[1], ": ", cauta_val1(rad,element[1]))
    if element[0]==4:
        inserare(rad,element[1])
        predecesor=cauta_predecesor(rad,element[1])
        rad=stergere(rad,val)
        print("Predecesorul elementului ", element[1], ": ", predecesor.val)
    if element[0]==5:
        inserare(rad,element[1])
        succesor=cauta_succesor(rad,element[1])
        rad=stergere(rad,element[1])
        print("Succesorul elementului ", element[1], ": ", succesor.val)
    if element[0]==6:
        print("Afisare inordine cu elemente intre ", element[1], "si ", element[2])
        inordine_interval(rad,element[1],element[2])


#print("\nexemplu")
#n=nod(10)
#n.left=nod(7)
#n.right=nod(12)
#inserare(n, 4)
#inserare(n, 11)
#inordine(n)

#ok1=cauta_val1(n,10)
#print("ok1=", ok1)

#ok2=cauta_val1(n,14)
#print("ok2=", ok2)