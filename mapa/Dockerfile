# syntax=docker/dockerfile:1

FROM node:18-alpine
ENV NODE_ENV=production

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install --production
# RUN npm install

COPY . .

RUN apk add curl
# EXPOSE 5173

CMD ["node", "server.js"]