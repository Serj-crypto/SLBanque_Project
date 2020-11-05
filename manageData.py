# -*- coding: utf-8 -

import os
#----------------- util vs inutil

import sqlite3
from CClient import Client
from CCompte import Compte
from traitement import lastname, firstname, createIdClient, createIdCompte


#verifBase, createSLBDB, load*

'''
Cree la base de donnees ainsi que les tables
et 4 fichier pour les sauvegardes rapide afin de ne pas 
avoir a filtrer ses informations directement des donnees
a la reouverture du programme
'''
def createSLBDB():
    connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
    curseur = connexion.cursor()
    curseur.execute('''CREATE TABLE IF NOT EXISTS Clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    idClient TEXT,
    Nom TEXT,
    Prenom TEXT,
    Adresse TEXT,
    Tlf INTEGER,
    NIF INTEGER)
                ''')
    curseur.execute('''CREATE TABLE IF NOT EXISTS Comptes(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    idClient TEXT,
    idCompte TEXT,
    Solde INTEGER)
                ''')
    connexion.commit()
    connexion.close()
    
    if not os.path.exists("Sauvegardes/listeCompte.txt"):
        z=open("Sauvegardes/listeCompte.txt", 'w')
        z.close()
    if not os.path.exists("Sauvegardes/listeClient.txt"):
        a=open("Sauvegardes/listeClient.txt", 'w')
        a.close()
    return "Nouvelle base cree avec succes"

# Verifie si la base de donnee existe
def verifbase(): 
    return os.path.exists("Sauvegardes/SLBDB.sqlite")


"""    
def supr(id_compte):#uniquement pour les compte depuis une condition du systeme
    connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
    curseur = connexion.cursor()
    curseur.execute("DELETE from Compte where idCompte = ?", )
    connexion.commit()
    connexion.close()
    if isinstance(element, Client):
        x=element
        i=x.idClient
        
        curseur.execute("DELETE from Clients where idClient = ?", )
        connexion.commit()
        connexion.close()
    if isinstance(element, Compte):
        x=element
        i=x.idCompte
        connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
        curseur = connexion.cursor()
 """       
      
def update(cpt_id, cpt_solde):#uniquement pour les transactions
    el=cpt_id
    c=cpt_solde
    l=(el, c)
    connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Comptes set Solde = ? WHERE idCompte = ?", l)
    
    
        
def add(element):
    if isinstance(element, Client):
        cl=element
        #code pour enregistrer dans la table
        connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
        curseur = connexion.cursor()
        el=(cl.idClient, cl.nom, cl.prenom, cl.adresse, cl.phone, cl.nif)
        curseur.execute('''INSERT INTO Clients(idClient, Nom, Prenom, Adresse, 
                Tlf, NIF) VALUES (?, ?, ?, ?, ?, ?)''', el)
        connexion.commit()
        connexion.close()
    elif isinstance(element, Compte):
        cpt=element
        connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
        curseur = connexion.cursor()
        el=(cpt.idClient, cpt.idCompte, cpt.prenom)
        curseur.execute('''INSERT INTO Comptes(idClient, idCompte, Solde)
                        VALUES (?, ?, ?)''', el)
        connexion.commit()
        connexion.close()
"""       
def saveLastIdClient(lastid):#a mettre dans traitement
    with open("Sauvegardes/idClient.txt", 'w') as iid:
        iid.write(lastid.idClient)
        
def saveLastIdCompte(lastid):#a mettre dans traitement
    with open("Sauvegardes/idCompte.txt", 'w') as iid:
        iid.write(lastid.idCompte)

def getLastIdCompte(v):#la decantation des chiffre sera traite par createIdClient de traitement
    with open("Sauvegardes/idCompte.txt", 'r') as iid:
        return iid.read()
    
def getLastIdClient():#la decantation des chiffre sera traite par createIdClient de traitement
    with open("Sauvegardes/idClient.txt", 'r') as iid:
        return iid.read()
"""    
class acces:
    def __init__(self):
        self._pas=False
        
    def _get_pas(self):
        return self._pas
    def _set_pas(self, val):
        self._pas=val
    pas=property(_get_pas, _set_pas)
    
    # creer une methode dans l'exe qui recupere appres validation la
    #valeur de acces et continue si elle est vraie
    #a l'ouverture
    
def giveAccess(x):
    y=x
    with open("Sauvegardes/acces.txt", 'w') as iid:
        iid.write(y)

def setListIdCpt():
    with open("Sauvegardes/listeCompte.txt", 'r') as iid:
        u=iid.readlines()
        cpt_set=list()
        if u != "":
            for c in u:
                cpt_set.append(c.strip())
    return cpt_set

def setListIdCl():
    with open("Sauvegardes/listeClient.txt", 'r') as iid:
        u=iid.readlines()
        cl_set=list()
        if u != "":
            for c in u:
                cl_set.append(c.strip())
    return cl_set

#a la fermeture
def updateListId(l1, l2):
    l3 = list()
    l4 = list()
    for el in l1:
        l3.append(el.idClient)
        
    for el in l2:
        l4.append(el.idCompte)
            
    return l3, l4
            
def saveListId(lu, lv):
    l3=lu
    l4=lv
    with open("Sauvegardes/listeClient.txt", 'w') as iid:
        for c in l3:
            iid.write(c+"\n")
    with open("Sauvegardes/listeCompte.txt", 'w') as iid:
        for c in l4:
            iid.write(c+"\n")
    

def loadSLBDBClients():#prend une liste vide en parametre
    SLBDB_temp=[]
    connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM Clients")
    r=curseur.fetchall()
    connexion.close()
    r=list(r)
    for  r1 in r:
        i1=r1[1]
        i2=r1[2]
        i3=r1[3]
        i4=r1[4]
        i5=r1[5]
        i6=r1[6]
        c = Client(i1, i2, i3, i4, i5, i6)
        SLBDB_temp.append(c)
    return SLBDB_temp

def loadSLBDBComptes():
    SLBDB_temp=[]
    connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM Comptes")
    r=curseur.fetchall()
    connexion.close()
    r=list(r)
    for  r1 in r:
        i1=r1[1]
        i2=r1[2]
        i3=r1[3]
        c = Compte(i1, i2, i3)
        SLBDB_temp.append(c)
    return SLBDB_temp

def saveSLBDBClients(liste):
    l=liste
    connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
    curseur=connexion.cursor()
    curseur.execute("DROP TABLE Clients")
    curseur.execute('''CREATE TABLE IF NOT EXISTS Clients(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            idClient TEXT,
            Nom TEXT,
            Prenom TEXT,
            Adresse TEXT,
            Tlf INTEGER,
            NIF INTEGER)
                ''')
    for c_1 in l:
        element=(c_1.idClient, c_1.nom, c_1.prenom, c_1.adresse, c_1.phone, c_1.nif)
        curseur.execute('''INSERT INTO Clients(idClient, Nom, Prenom, Adresse, 
                Tlf, NIF) VALUES (?, ?, ?, ?, ?, ?)''', element)
        connexion.commit()
    connexion.close()

def saveSLBDBComptes(liste):
    l=liste
    connexion = sqlite3.connect("Sauvegardes/SLBDB.sqlite")
    curseur=connexion.cursor()
    curseur.execute("DROP TABLE Comptes")
    curseur.execute('''CREATE TABLE IF NOT EXISTS Comptes(
           id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
           idClient TEXT,
           idCompte TEXT,
           Solde INTEGER)
        ''')
    for c_1 in l:
        element=(c_1.idClient, c_1.idCompte, c_1.solde)
        curseur.execute('''INSERT INTO Comptes(idClient, idCompte, Solde)
                        VALUES (?, ?, ?)''', element)
        connexion.commit()
    connexion.close()
    
def supprimerCompte(SLBDB1_temp, SLBDB2_temp, idToDel):#1-compte, 2-client
    l1=SLBDB1_temp
    l2=SLBDB2_temp
    y=list()
    for r in l1:
        if r.idClient== idToDel:
            y=y.append(l1.index(r))
        else:
            pass
    if len(y)==1:
        x=l1[y[0]].idClient
        for r in l2:
            if r.idClient== x:
                l2.remove(l2.index(r))
            else:
                pass
    else:
        pass
    l1.remove(y[0])
        
    return l1, l2

def createClient(u, v, l1, l2, b, c, d, e, f, g):
    lu=l1
    lv=l2
    b = lastname(b)
    c = firstname(c)
    x = createIdClient(b, c, lu)
    z = Client(x, b, c, d, e, f)
    u.append(z)
    lu.append(x)
    y = createIdCompte(lv)
    w = Compte(x, y, g)
    lv.append(y)
    v.append(w)
    return u, v, lu, lv