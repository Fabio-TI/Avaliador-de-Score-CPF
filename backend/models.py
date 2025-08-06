from sqlalchemy import Column, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(14), unique=True, index=True)
    nome = Column(String(100))
    telefone = Column(String(15))
    cep = Column(String(9))
    