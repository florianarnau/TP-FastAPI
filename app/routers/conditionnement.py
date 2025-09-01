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

@router.post("/", response_model=schemas.Conditionnement)
def create_conditionnement(cond: schemas.ConditionnementCreate, db: Session = Depends(get_db)):
    db_cond = models.Conditionnement(**cond.dict())
    db.add(db_cond)
    db.commit()
    db.refresh(db_cond)
    return db_cond

@router.get("/", response_model=list[schemas.Conditionnement])
def list_conditionnements(db: Session = Depends(get_db)):
    return db.query(models.Conditionnement).all()

@router.get("/{cond_id}", response_model=schemas.Conditionnement)
def read_conditionnement(cond_id: int, db: Session = Depends(get_db)):
    cond = db.query(models.Conditionnement).get(cond_id)
    if not cond:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")
    return cond

@router.put("/{cond_id}", response_model=schemas.Conditionnement)
def update_conditionnement(cond_id: int, cond_update: schemas.ConditionnementCreate, db: Session = Depends(get_db)):
    cond = db.query(models.Conditionnement).get(cond_id)
    if not cond:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")
    for key, value in cond_update.dict().items():
        setattr(cond, key, value)
    db.commit()
    db.refresh(cond)
    return cond

@router.delete("/{cond_id}")
def delete_conditionnement(cond_id: int, db: Session = Depends(get_db)):
    cond = db.query(models.Conditionnement).get(cond_id)
    if not cond:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")
    db.delete(cond)
    db.commit()
    return {"message": "Conditionnement supprimé"}
