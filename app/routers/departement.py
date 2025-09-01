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

@router.post("/", response_model=schemas.Departement)
def create_departement(dep: schemas.DepartementCreate, db: Session = Depends(get_db)):
    db_dep = models.Departement(**dep.dict())
    db.add(db_dep)
    db.commit()
    db.refresh(db_dep)
    return db_dep

@router.get("/", response_model=list[schemas.Departement])
def list_departements(db: Session = Depends(get_db)):
    return db.query(models.Departement).all()

@router.get("/{code_dept}", response_model=schemas.Departement)
def read_departement(code_dept: str, db: Session = Depends(get_db)):
    dep = db.query(models.Departement).get(code_dept)
    if not dep:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    return dep

@router.put("/{code_dept}", response_model=schemas.Departement)
def update_departement(code_dept: str, dep_update: schemas.DepartementCreate, db: Session = Depends(get_db)):
    dep = db.query(models.Departement).get(code_dept)
    if not dep:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    for key, value in dep_update.dict().items():
        setattr(dep, key, value)
    db.commit()
    db.refresh(dep)
    return dep

@router.delete("/{code_dept}")
def delete_departement(code_dept: str, db: Session = Depends(get_db)):
    dep = db.query(models.Departement).get(code_dept)
    if not dep:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    db.delete(dep)
    db.commit()
    return {"message": "Département supprimé"}
