# Avaliador-de-Score-CPF
Sistema completo de avaliação de score de CPF para aprovação de crédito em vendas

## ✅ Arquitetura do Sistema

1. **Frontend**: React (interface amigável)
2. **Backend (API REST)**: Python com FastAPI (leve, rápido e ideal para APIs)
3. **Banco de Dados**: SQLite (para simplicidade, mas com poder de escalar para PostgreSQL)
4. **Integrações**: Simulação de consulta ao CDL e SERASA - As APIs externas não públicas, então nesse contexto vamos simular.
5. **Validação CPF**: Com regras de negócio - validação de dígitos, formatação.

## 🛠️ Estrutura do Projeto

```
sistema-credito/
│
├── backend/
│   ├── main.py              (FastAPI)
│   ├── database.py          (Conexão com banco)
│   ├── models.py            (Modelos do SQLAlchemy)
│   └── Dockerfile           (Criando imagem Docker para empacotar aplicação backend)
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/api.js
│   │   └── App.js
│   ├── package.json
│   └── Dockerfile          (Criando imagem Docker para empacotar aplicação frontend)
│
├── docker-compose.yml
└── README.md
```
## ✅ Instruções para Execução

bash
```
# Backend
cd backend
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm start
```
Acesse localmente: http://localhost:3000

## ✅ Melhorias Futuras e Contribuição

* Integrar com APIs reais (via parceiros autorizados)
* Autenticação (JWT)
* Histórico de Consultas
* Geração de relatórios PDF
* Dashboards com Gráficos
* Deploy com Docker + Nginx

  
