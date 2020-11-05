# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:14:24 2020

@author: paryajpam
"""
def firstname(name):
	n_1=str(name)
	decom2=list()
	decom=n_1.split(" ")
	for el in decom :
		decom2.append(el.capitalize().strip())
	n_1=" ".join(decom2)
	return n_1

def lastname(name):#Pour prenom et adresse
    name=str(name)
    n_1=name.upper().strip()
    return n_1
	
def capital(name):
    name=str(name)
    n_1=name.capitalize().strip()
    return n_1

def createIdClient(n_1, n_2, u):
    idc1=n_1[0]+n_2[0]+"-"
    idc2=""
    i_2=""
    i_3=u # u est la liste des idClient
    if i_3==[]:
        idc2="0001"
    else:
        i_2=i_3[len(i_3)-1]
        i_2=int(i_2[3:])
        i_2+=1
        i_2=str(i_2)
        c=len(i_2)
        if c==1:
            idc2="000"+i_2
        elif c==2:
            idc2="00"+i_2
        elif c==3:
            idc2="0"+i_2
        elif c==4:
            idc2=i_2
    return str(idc1+idc2)

def createIdCompte(v):
    i=v 
    # v etant la liste des idComptes
    idc2=""
    if i==[]:
        idc2="0001"
    else:
        i_2=i[len(i)-1]
        i_0=int(i_2)
        i_0+=1
        i_0=str(i_0)
        c=len(i_0)
        if c==1:
            idc2="000"+i_0
        elif c==2:
            idc2="00"+i_0
        elif c==3:
            idc2="0"+i_0
        elif c==4:
            idc2=i_0
    return idc2

def verifIntPosit(x):
    try:
        x=int(x)
        assert x>10
    except ValueError:
        return "Ce n'es pas un entier"#code to 1
    except AssertionError:
        return "Montant superieur a 10 unite"# code o 2
    return x

def verifRetrait(x, y):
    if x<y-10:
        return True
    else:
        return False
