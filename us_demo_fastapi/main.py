from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from config import models
from config import schemas
from config import crud
from config.db import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Us Demographics api"}

@app.post("/createuser/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user_name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="user already registered")
    return crud.create_user(db=db, user=user)


@app.get("/getusers/")
def get_users():
    all_users=crud.get_all_users()

