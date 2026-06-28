# =====================================================
# AI Empire Pro V8
# Dockerfile
# =====================================================

FROM node:20-alpine

LABEL maintainer="AI Empire Pro"
LABEL version="8.0.0"

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN mkdir -p \
    uploads \
    logs \
    backups \
    storage

EXPOSE 3000

ENV NODE_ENV=production

CMD ["npm", "start"]
