# -*- coding: utf-8 -*-


class Client:
    def __init__(self, idCl, nm, prnm, ad, ph, nf):
        self._idClient=idCl
        self._nom=nm
        self._prenom=prnm
        self._adresse=ad
        self._phone=ph
        self._nif=nf
        
    def _set_nom(self, element):                       #on passe l'objet et la nouvelle valeur en param.
        self._nom=element

    def _get_nom(self):
        return self._nom

    nom=property(_get_nom, _set_nom)

    def _set_prenom(self, element):                       #on passe l'objet et la nouvelle valeur en param.
        self._prenom=element

    def _get_prenom(self):
        return self._prenom

    prenom=property(_get_prenom, _set_prenom)

    def _set_adresse(self, element):                       #on passe l'objet et la nouvelle valeur en param.
        self._adresse=element

    def _get_adresse(self):
        return self._adresse

    adresse=property(_get_adresse, _set_adresse)

    def _set_phone(self, element):                       #on passe l'objet et la nouvelle valeur en param.
        self._phone=element

    def _get_phone(self):
        return self._phone

    phone=property(_get_phone, _set_phone)

    def _set_nif(self, element):                       #on passe l'objet et la nouvelle valeur en param.
        self._adresse=element

    def _get_nif(self):
        return self._nif

    nif=property(_get_nif, _set_nif)

    def _set_idClient(self, element):
        self._idCLient=element
        
    def _get_idClient(self):
        return self._idClient
    
    idClient=property(_get_idClient, _set_idClient)
