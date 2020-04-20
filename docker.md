Pour être capable d'utiliser le docker mis en place, et de se servir du server Nginx, il va falloir taper ces commandes dans un terminal

docker build -f Dockerfile-prod -t (le nom de l'app):prod

Ensuite, une fois que cette commande est réalisé, il faudra taper celle-ci:

docker run -it -p 8080:8080 --rm my-app:prod

Une fois cette commande réalisé, il faudra se rendre dans votre navigateur et taper http://IP_machine_docker:8080/
