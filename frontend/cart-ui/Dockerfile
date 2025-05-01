FROM node:18

WORKDIR /app

RUN apt-get update && apt-get install -y python3 make g++

COPY ./frontend/cart-ui/package.json ./frontend/cart-ui/package-lock.json /app/

RUN rm -rf node_modules package-lock.json && npm install

COPY ./frontend/cart-ui /app

EXPOSE 3000:3000

CMD ["npm", "run", "dev"]