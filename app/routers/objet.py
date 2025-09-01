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

@router.post("/", response_model=schemas.Objet)
def create_objet(objet: schemas.ObjetCreate, db: Session = Depends(get_db)):
    db_objet = models.Objet(**objet.dict())
    db.add(db_objet)
    db.commit()
    db.refresh(db_objet)
    return db_objet

@router.get("/", response_model=list[schemas.Objet])
def list_objets(db: Session = Depends(get_db)):
    return db.query(models.Objet).all()

@router.get("/{objet_id}", response_model=schemas.Objet)
def read_objet(objet_id: int, db: Session = Depends(get_db)):
    objet = db.query(models.Objet).get(objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return objet

@router.put("/{objet_id}", response_model=schemas.Objet)
def update_objet(objet_id: int, objet_update: schemas.ObjetCreate, db: Session = Depends(get_db)):
    objet = db.query(models.Objet).get(objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    for key, value in objet_update.dict().items():
        setattr(objet, key, value)
    db.commit()
    db.refresh(objet)
    return objet

@router.delete("/{objet_id}")
def delete_objet(objet_id: int, db: Session = Depends(get_db)):
    objet = db.query(models.Objet).get(objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    db.delete(objet)
    db.commit()
    return {"message": "Objet supprimé"}
