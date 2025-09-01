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

@router.post("/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/", response_model=list[schemas.Client])
def list_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()

@router.get("/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client

@router.put("/{client_id}", response_model=schemas.Client)
def update_client(client_id: int, client_update: schemas.ClientCreate, db: Session = Depends(get_db)):
    client = db.query(models.Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    for key, value in client_update.dict().items():
        setattr(client, key, value)
    db.commit()
    db.refresh(client)
    return client

@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    db.delete(client)
    db.commit()
    return {"message": "Client supprimé"}
