from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from schemas import EmpresaCreate, Empresa, ObrigacaoAcessoriaCreate, ObrigacaoAcessoria


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool
    
class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]
    
def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
# CRUD para Empresa
@app.post("/empresas/", response_model=Empresa, status_code=status.HTTP_201_CREATED)
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = models.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/", response_model=List[Empresa])
def read_empresas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    empresas = db.query(models.Empresa).offset(skip).limit(limit).all()
    return empresas

@app.get("/empresas/{empresa_id}", response_model=Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.put("/empresas/{empresa_id}", response_model=Empresa)
def update_empresa(empresa_id: int, empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    for key, value in empresa.dict().items():
        setattr(db_empresa, key, value)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.delete("/empresas/{empresa_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    db.delete(db_empresa)
    db.commit()

# CRUD para ObrigacaoAcessoria
@app.post("/obrigacoes/", response_model=ObrigacaoAcessoria, status_code=status.HTTP_201_CREATED)
def create_obrigacao(obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.get("/obrigacoes/", response_model=List[ObrigacaoAcessoria])
def read_obrigacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    obrigacoes = db.query(models.ObrigacaoAcessoria).offset(skip).limit(limit).all()
    return obrigacoes

@app.get("/obrigacoes/{obrigacao_id}", response_model=ObrigacaoAcessoria)
def read_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return db_obrigacao

@app.put("/obrigacoes/{obrigacao_id}", response_model=ObrigacaoAcessoria)
def update_obrigacao(obrigacao_id: int, obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    for key, value in obrigacao.dict().items():
        setattr(db_obrigacao, key, value)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.delete("/obrigacoes/{obrigacao_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    db.delete(db_obrigacao)
    db.commit()
        
    