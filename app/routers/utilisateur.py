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

@router.post("/", response_model=schemas.Utilisateur)
def create_utilisateur(user: schemas.UtilisateurCreate, db: Session = Depends(get_db)):
    db_user = models.Utilisateur(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[schemas.Utilisateur])
def list_utilisateurs(db: Session = Depends(get_db)):
    return db.query(models.Utilisateur).all()

@router.get("/{user_id}", response_model=schemas.Utilisateur)
def read_utilisateur(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Utilisateur).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user

@router.put("/{user_id}", response_model=schemas.Utilisateur)
def update_utilisateur(user_id: int, user_update: schemas.UtilisateurCreate, db: Session = Depends(get_db)):
    user = db.query(models.Utilisateur).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    for key, value in user_update.dict().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_utilisateur(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Utilisateur).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    db.delete(user)
    db.commit()
    return {"message": "Utilisateur supprimé"}
