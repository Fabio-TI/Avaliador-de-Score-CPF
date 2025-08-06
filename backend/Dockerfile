# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copia o requirements.txt
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do backend
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar a API FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]