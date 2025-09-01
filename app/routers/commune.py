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

@router.post("/", response_model=schemas.Commune)
def create_commune(commune: schemas.CommuneCreate, db: Session = Depends(get_db)):
    db_commune = models.Commune(**commune.dict())
    db.add(db_commune)
    db.commit()
    db.refresh(db_commune)
    return db_commune

@router.get("/", response_model=list[schemas.Commune])
def list_communes(db: Session = Depends(get_db)):
    return db.query(models.Commune).all()

@router.get("/{commune_id}", response_model=schemas.Commune)
def read_commune(commune_id: int, db: Session = Depends(get_db)):
    commune = db.query(models.Commune).get(commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")
    return commune

@router.put("/{commune_id}", response_model=schemas.Commune)
def update_commune(commune_id: int, commune_update: schemas.CommuneCreate, db: Session = Depends(get_db)):
    commune = db.query(models.Commune).get(commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")
    for key, value in commune_update.dict().items():
        setattr(commune, key, value)
    db.commit()
    db.refresh(commune)
    return commune

@router.delete("/{commune_id}")
def delete_commune(commune_id: int, db: Session = Depends(get_db)):
    commune = db.query(models.Commune).get(commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")
    db.delete(commune)
    db.commit()
    return {"message": "Commune supprimée"}
