FROM node:12.2.0-alpine

WORKDIR /website

ENV PATH /website/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /home/camille/projet/AuBonBeurre/website/package.json
RUN npm install
RUN npm install @vue/cli@3.7.0 -g

# start app
CMD ["npm","run","serve"]
