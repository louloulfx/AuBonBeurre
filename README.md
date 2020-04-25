# AuBonBeurre

Ce projet est réalisé par : 

- Camille Guerin
- Valentin Guibert
- Elouan Lafréchoux

## Préambule  
  
L'application est dockerisée. Elle est découpée en neufs containers : les unités qui effectuent le script python (6 unités), l'api qui permet ensuite au site web d'utiliser les données, la base de donnée mysql et le serveur web (Vuejs/Nginx).
  
## Pré-requis  
  
Installer docker / docker-compose /  net-tools
  
## Commandes utiles   
À lancer idéalement depuis les containers ou depuis votre machine si vous disposez des librairies nécessaires dans les bonnes versions.  
  
### Monter l'environnement  

Pour commencer placer vous dans le dossier website et effectuer :
```
npm install
```
Ensuite revenez à la racine du projet et lancer les container:
  
```  
docker-compose up 
```  
Il faut penser à kill les services en cours sur les ports que le projet utilise comme le port :80 et le port :3306
Pour vérifier qu'ils sont utilisable il faut utiliser cette commande : 
```  
sudo netstat -plnt | grep ':3306' (ou :80 en fonction du port qui convient)
```  
Et il faut supprimer le service en cours :
```  
sudo kill id_service
```  
L'id du service se trouve avant le /nom_du_service
  
  ### Liens des outils

Vous pouvez maintenant accéder à l'api à cette adresse: [localhost:5000](localhost:5000).

Et au site web ici : [localhost:80](localhost:80).

Vous pouvez aussi installer mysql sur votre machine et avoir accès à la base de donnée accessible sur le port 3306.