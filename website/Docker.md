# docker

## project setup
```
npm install
```
## create docker image
```
docker build -f Dockerfile-prod -t website:prod
```
## initialize nginx server with docker
```
docker run -it -p 8080:8080 --rm website:prod
```
