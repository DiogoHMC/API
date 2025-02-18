from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from enum import Enum as PyEnum
from database import Base

class Empresa(Base):
    __tablename__ = 'Empresa'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique= True, index=True)
    endereco = Column(String, index=True)
    email = Column(String, index=True)
    telefone = Column(String, index=True)
    
class PeriodicidadeEnum(PyEnum):
    MENSAL = "mensal"
    TRIMESTRAL = "trimestral"
    ANUAL = "anual"
    
class ObrigacaoAcessoria(Base):
    __tablename__ = 'ObrigacaoAcessoria'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    periodicidade = Column(Enum(PeriodicidadeEnum), nullable=False)
    empresa_id = Column(Integer, ForeignKey("Empresa.id"))