from datetime import date
from app import models, database

# Créer la base si pas déjà faite
models.Base.metadata.create_all(bind=database.engine)

db = database.SessionLocal()

# Nettoyage des tables (⚠️ uniquement pour les tests)
db.query(models.RoleUtilisateur).delete()
db.query(models.Role).delete()
db.query(models.Utilisateur).delete()
db.query(models.DetailObjet).delete()
db.query(models.Detail).delete()
db.query(models.Commande).delete()
db.query(models.Client).delete()
db.query(models.Commune).delete()
db.query(models.Departement).delete()
db.query(models.ObjetCond).delete()
db.query(models.Objet).delete()
db.query(models.Conditionnement).delete()
db.query(models.Poids).delete()
db.query(models.Vignette).delete()
db.commit()

# ----------------------
# Départements & Communes
# ----------------------
dep1 = models.Departement(code_dept="75", nom_dept="Paris", ordre_aff_dept=1)
dep2 = models.Departement(code_dept="69", nom_dept="Rhône", ordre_aff_dept=2)
db.add_all([dep1, dep2])
db.commit()

comm1 = models.Commune(dep="75", cp="75001", ville="Paris")
comm2 = models.Commune(dep="69", cp="69001", ville="Lyon")
db.add_all([comm1, comm2])
db.commit()

# ----------------------
# Clients
# ----------------------
client1 = models.Client(
    genrecli="H",
    nomcli="Dupont",
    prenomcli="Jean",
    adresse1cli="10 rue de Paris",
    villecli_id=comm1.id,
    telcli="0101010101",
    emailcli="jean.dupont@example.com",
    portcli="0606060606",
    newsletter=1,
)

client2 = models.Client(
    genrecli="F",
    nomcli="Martin",
    prenomcli="Sophie",
    adresse1cli="20 rue de Lyon",
    villecli_id=comm2.id,
    telcli="0202020202",
    emailcli="sophie.martin@example.com",
    portcli="0707070707",
    newsletter=0,
)
db.add_all([client1, client2])
db.commit()

# ----------------------
# Objets & Conditionnements
# ----------------------
cond1 = models.Conditionnement(libcondit="Carton", poidscondit=200, prixcond=2.5, ordreimp=1)
cond2 = models.Conditionnement(libcondit="Caisse bois", poidscondit=500, prixcond=5.0, ordreimp=2)
db.add_all([cond1, cond2])
db.commit()

obj1 = models.Objet(libobj="Camembert", tailleobj="250g", puobj=3.5, poidsobj=250)
obj2 = models.Objet(libobj="Comté", tailleobj="500g", puobj=7.0, poidsobj=500)
db.add_all([obj1, obj2])
db.commit()

# Relation objet/conditionnement
rel1 = models.ObjetCond(codobj=obj1.codobj, codcond=cond1.idcondit, qteobjdeb=1, qteobjfin=10)
rel2 = models.ObjetCond(codobj=obj2.codobj, codcond=cond2.idcondit, qteobjdeb=1, qteobjfin=5)
db.add_all([rel1, rel2])
db.commit()

# ----------------------
# Commandes & Détails
# ----------------------
commande1 = models.Commande(
    datcde=date.today(),
    codcli=client1.codcli,
    timbrecli=0.5,
    timbrecde=1.0,
    nbcolis=2,
    cheqcli=20.0,
    idcondit=cond1.idcondit,
    cdeComt="Première commande",
)

commande2 = models.Commande(
    datcde=date.today(),
    codcli=client2.codcli,
    timbrecli=0.5,
    timbrecde=1.5,
    nbcolis=1,
    cheqcli=10.0,
    idcondit=cond2.idcondit,
    cdeComt="Deuxième commande",
)
db.add_all([commande1, commande2])
db.commit()

# Détails commande
detail1 = models.Detail(codcde=commande1.codcde, qte=2, colis=1, commentaire="Livraison rapide")
detail2 = models.Detail(codcde=commande2.codcde, qte=1, colis=1, commentaire="A emballer avec soin")
db.add_all([detail1, detail2])
db.commit()

# Associer objets aux détails
dobj1 = models.DetailObjet(detail_id=detail1.id, objet_id=obj1.codobj)
dobj2 = models.DetailObjet(detail_id=detail2.id, objet_id=obj2.codobj)
db.add_all([dobj1, dobj2])
db.commit()

# ----------------------
# Utilisateurs & Rôles
# ----------------------
role_admin = models.Role(codrole=1, librole="Admin")
role_colis = models.Role(codrole=2, librole="OP-colis")
role_stock = models.Role(codrole=3, librole="OP-stock")
db.add_all([role_admin, role_colis, role_stock])
db.commit()

user1 = models.Utilisateur(
    code_utilisateur=1,
    nom_utilisateur="Germain",
    prenom_utilisateur="Christophe",
    username="cgermain",
    couleur_fond_utilisateur=0,
    date_insc_utilisateur=date.today(),
)
db.add(user1)
db.commit()

# Associer utilisateur au rôle Admin
user_role = models.RoleUtilisateur(utilisateur_id=user1.code_utilisateur, role_id=role_admin.codrole)
db.add(user_role)
db.commit()

print("✅ Données de test insérées avec succès !")

db.close()