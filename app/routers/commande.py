from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Commande)
def create_commande(commande: schemas.CommandeCreate, db: Session = Depends(get_db)):
    db_commande = models.Commande(**commande.dict())
    db.add(db_commande)
    db.commit()
    db.refresh(db_commande)
    return db_commande

@router.get("/", response_model=list[schemas.Commande])
def list_commandes(db: Session = Depends(get_db)):
    return db.query(models.Commande).all()

@router.get("/{commande_id}", response_model=schemas.Commande)
def read_commande(commande_id: int, db: Session = Depends(get_db)):
    commande = db.query(models.Commande).get(commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return commande

@router.put("/{commande_id}", response_model=schemas.Commande)
def update_commande(commande_id: int, commande_update: schemas.CommandeCreate, db: Session = Depends(get_db)):
    commande = db.query(models.Commande).get(commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    for key, value in commande_update.dict().items():
        setattr(commande, key, value)
    db.commit()
    db.refresh(commande)
    return commande

@router.delete("/{commande_id}")
def delete_commande(commande_id: int, db: Session = Depends(get_db)):
    commande = db.query(models.Commande).get(commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    db.delete(commande)
    db.commit()
    return {"message": "Commande supprimée"}
