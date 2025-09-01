from fastapi import FastAPI
from app import models, database
from app.routers import client, commande, objet, conditionnement, commune, departement, utilisateur, role

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="API Fromagerie DIGICHEESE")

# Inclure les routes
app.include_router(client.router, prefix="/clients", tags=["clients"])
app.include_router(commande.router, prefix="/commandes", tags=["commandes"])
app.include_router(objet.router, prefix="/objets", tags=["objets"])
app.include_router(conditionnement.router, prefix="/conditionnements", tags=["conditionnements"])
app.include_router(commune.router, prefix="/communes", tags=["communes"])
app.include_router(departement.router, prefix="/departements", tags=["departements"])
app.include_router(utilisateur.router, prefix="/utilisateurs", tags=["utilisateurs"])
app.include_router(role.router, prefix="/roles", tags=["roles"])

@app.get("/")
def root():
    return {"message": "Bienvenue sur l’API DIGICHEESE"}
