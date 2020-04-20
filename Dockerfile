FROM node:12.2.0-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json home/user3/app/package.json
RUN npm install
RUN npm install @vue/cli@3.7.0 -g

# start app
CMD npm run start