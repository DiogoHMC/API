from pydantic import BaseModel
from typing import Optional
from enum import Enum

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int

    class Config:
        from_attributes = True  

# Enum para Periodicidade
class PeriodicidadeEnum(str, Enum):
    MENSAL = "mensal"
    TRIMESTRAL = "trimestral"
    ANUAL = "anual"

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: PeriodicidadeEnum
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int

    class Config:
        from_attributes = True