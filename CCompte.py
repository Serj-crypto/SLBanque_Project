# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:31:01 2020

@author: paryajpam
"""
from traitement import verifRetrait

class Compte:
    def __init__(self, proprio, idCpt, sld):
        self._idClient= proprio
        self._idCompte= idCpt
        self._solde= sld
        
    def _get_idClient(self):
        return self._idClient
    def _set_idClient(self, element):
        self._idClient=element
        
    idClient=property(_get_idClient, _set_idClient)
    
    def _get_idCompte(self):
        return self._idCompte
    def _set_idCompte(self, element):
        self._idCompte=element
        
    idCompte=property(_get_idCompte, _set_idCompte)
    
    def _get_solde(self):
        return self._solde
    def _set_solde(self, element):
        self._solde=element
        
    solde=property(_get_solde, _set_solde)
    
    def deposer(self, montant):
        self._solde += montant
        return self._solde
        
    def retirer(self, montant):
        self._solde -= montant
        x= self._solde
        y=bool()
        if x<10:
            y=True
        else:
            y=False
        return self._solde, y, self.idClient #ne pas oublier de capt del si vrai
        
    def transferer(self, Cpt2, montant):
        benef = Cpt2
        self.retirer(montant)
        benef.deposer(montant)
        return "Transfer effectue avec succes"