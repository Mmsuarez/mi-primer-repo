# mi-primer-repo
Repositorio clase Coder Django 01

## Mi primer commit remoto
Esto es un commit remoto

## Configuracion
git init
git remote add origin  + URL del repositorio (lo copio de github) # - vincula el repositorio local con el remoto -#
git pull origin main # Trae lo que tenga el remoto #
git branch -M main # cambia el nombre de la branch que trae por defecto, en lugar de master se usa main ahora #

history # veo el historial #

git add README.md # git add + nombre del archivo (readme en este caso, con terminacion .md) 
git commit -m "esto es mi primer commit"
git push -u origin main # con esto actualizo el readme de github con lo que tengo en mi archivo local #

#para lo anterior, probablemente me pida autorizacion en la web para sincronizar. una vez hecho, ya queda sincronizado
