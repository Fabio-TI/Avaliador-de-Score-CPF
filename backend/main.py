from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database, models
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Criação das tabelas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Sistema de Avaliação de Crédito")

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência do banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo Pydantic
class ClienteCreate(BaseModel):
    cpf: str
    nome: str
    telefone: str
    cep: str

# Validação simples de CPF
def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    # Validação dos dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = (soma * 10) % 11
        digito = 0 if digito == 10 else digito
        if digito != int(cpf[i]):
            return False
    return True

# Simulação de consulta a SERASA e CDL
def consultar_serasa(cpf: str) -> dict:
    # Simulação: CPF terminado em 00 → negativado
    if cpf.endswith('00'):
        return {"aprovado": False, "motivo": "Restrição no SERASA"}
    return {"aprovado": True}

def consultar_cdl(cpf: str) -> dict:
    # Simulação: CPF terminado em 11 → negativado
    if cpf.endswith('11'):
        return {"aprovado": False, "motivo": "Restrição na CDL"}
    return {"aprovado": True}

@app.post("/clientes/")
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    if not validar_cpf(cliente.cpf):
        raise HTTPException(status_code=400, detail="CPF inválido")

    db_cliente = db.query(models.Cliente).filter(models.Cliente.cpf == cliente.cpf).first()
    if db_cliente:
        raise HTTPException(status_code=400, detail="Cliente já cadastrado")

    novo_cliente = models.Cliente(**cliente.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return {"mensagem": "Cliente cadastrado com sucesso", "cliente": novo_cliente}

@app.get("/clientes/{cpf}")
def buscar_cliente(cpf: str, db: Session = Depends(get_db)):
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    if len(cpf_limpo) != 11:
        raise HTTPException(status_code=400, detail="CPF inválido")

    cliente = db.query(models.Cliente).filter(models.Cliente.cpf == cpf_limpo).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    # Simular consultas
    serasa = consultar_serasa(cpf_limpo)
    cdl = consultar_cdl(cpf_limpo)

    score_total = 0
    restricoes = []

    if serasa["aprovado"]:
        score_total += 50
    else:
        restricoes.append(serasa["motivo"])

    if cdl["aprovado"]:
        score_total += 50
    else:
        restricoes.append(cdl["motivo"])

    status = "Aprovado" if score_total >= 80 else "Restrito"

    return {
        "cliente": cliente,
        "score": score_total,
        "status": status,
        "restricoes": restricoes if restricoes else ["Nenhuma"]
    }