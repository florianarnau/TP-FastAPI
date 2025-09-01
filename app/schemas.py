from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal


# ----------------- Departement -----------------
class DepartementBase(BaseModel):
    nom_dept: Optional[str] = None
    ordre_aff_dept: Optional[int] = 0

class DepartementCreate(DepartementBase):
    code_dept: str

class Departement(DepartementBase):
    code_dept: str
    class Config:
        from_attributes = True


# ----------------- Commune -----------------
class CommuneBase(BaseModel):
    dep: Optional[str] = None
    cp: Optional[str] = None
    ville: Optional[str] = None

class CommuneCreate(CommuneBase):
    pass

class Commune(CommuneBase):
    id: int
    class Config:
        from_attributes = True


# ----------------- Client -----------------
class ClientBase(BaseModel):
    genrecli: Optional[str] = None
    nomcli: Optional[str] = None
    prenomcli: Optional[str] = None
    adresse1cli: Optional[str] = None
    adresse2cli: Optional[str] = None
    adresse3cli: Optional[str] = None
    villecli_id: Optional[int] = None
    telcli: Optional[str] = None
    emailcli: Optional[str] = None
    portcli: Optional[str] = None
    newsletter: Optional[int] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    codcli: int
    class Config:
        from_attributes = True


# ----------------- Commande -----------------
class CommandeBase(BaseModel):
    datcde: Optional[date] = None
    codcli: Optional[int] = None
    timbrecli: Optional[float] = None
    timbrecde: Optional[float] = None
    nbcolis: Optional[int] = 1
    cheqcli: Optional[float] = None
    idcondit: Optional[int] = 0
    cdeComt: Optional[str] = None
    barchive: Optional[int] = 0
    bstock: Optional[int] = 0

class CommandeCreate(CommandeBase):
    pass

class Commande(CommandeBase):
    codcde: int
    class Config:
        from_attributes = True


# ----------------- Conditionnement -----------------
class ConditionnementBase(BaseModel):
    libcondit: Optional[str] = None
    poidscondit: Optional[int] = None
    prixcond: Optional[Decimal] = 0
    ordreimp: Optional[int] = None

class ConditionnementCreate(ConditionnementBase):
    pass

class Conditionnement(ConditionnementBase):
    idcondit: int
    class Config:
        from_attributes = True


# ----------------- Objet -----------------
class ObjetBase(BaseModel):
    libobj: Optional[str] = None
    tailleobj: Optional[str] = None
    puobj: Optional[Decimal] = 0
    poidsobj: Optional[Decimal] = 0
    indispobj: Optional[int] = 0
    o_imp: Optional[int] = 0
    o_aff: Optional[int] = 0
    o_cartp: Optional[int] = 0
    points: Optional[int] = 0
    o_ordre_aff: Optional[int] = 0

class ObjetCreate(ObjetBase):
    pass

class Objet(ObjetBase):
    codobj: int
    class Config:
        from_attributes = True


# ----------------- Utilisateur -----------------
class UtilisateurBase(BaseModel):
    nom_utilisateur: Optional[str] = None
    prenom_utilisateur: Optional[str] = None
    username: Optional[str] = None
    couleur_fond_utilisateur: Optional[int] = 0
    date_insc_utilisateur: Optional[date] = None

class UtilisateurCreate(UtilisateurBase):
    pass

class Utilisateur(UtilisateurBase):
    code_utilisateur: int
    class Config:
        from_attributes = True


# ----------------- Role -----------------
class RoleBase(BaseModel):
    librole: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    codrole: int
    class Config:
        from_attributes = True
