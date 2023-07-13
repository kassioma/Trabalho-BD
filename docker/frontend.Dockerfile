FROM node:20-alpine

WORKDIR /src

ADD ./frontend /src

EXPOSE 3000

RUN npm install

CMD npm start