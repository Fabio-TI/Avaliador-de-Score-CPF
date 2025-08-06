# frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app

# Copia package.json e instala dependências
COPY package*.json ./
RUN npm install

# Copia o código-fonte
COPY . .

# Expõe a porta 3000
EXPOSE 3000

# Inicia o app React
CMD ["npm", "start"]