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

@router.post("/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    db_role = models.Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@router.get("/", response_model=list[schemas.Role])
def list_roles(db: Session = Depends(get_db)):
    return db.query(models.Role).all()

@router.get("/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(models.Role).get(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Rôle non trouvé")
    return role

@router.put("/{role_id}", response_model=schemas.Role)
def update_role(role_id: int, role_update: schemas.RoleCreate, db: Session = Depends(get_db)):
    role = db.query(models.Role).get(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Rôle non trouvé")
    for key, value in role_update.dict().items():
        setattr(role, key, value)
    db.commit()
    db.refresh(role)
    return role

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(models.Role).get(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Rôle non trouvé")
    db.delete(role)
    db.commit()
    return {"message": "Rôle supprimé"}
