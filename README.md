# Dotfiles-Helying-Vallejos
Mis Dotfiles y personalizacion de Arch Linux

## Repositorio

1. Clona el repositorio a nueva carpeta ~/.dotfiles
```zsh
# HTTPS
git clone https://github.com/Li7ewire/Dotfiles-Helying-Vallejos.git ~/.dotfiles
 
# SSH
git clone git@github.com:Li7ewire/Dotfiles-Helying-Vallejos.git ~/.dotfiles
```


## Usar git desde la terminal

1. Agregar un nuevo archivo local a github

``` zsh
# Para enviar nuevos archivos
git add "nombre_del_archivo"

# Para actualizar todos los archivos en github
git add -u 
```


2. Revisa el estado de los archivos modificados

```zsh
git status 
```


3. Agrega el comentario con los nuevos cambios 

``` zsh
git commit -m "Texto"
```


4. Envia los nuevos archivos o actualizaciones

```zsh
# Pedira usuario y clave de github
git push

# Si tienes llaves SSH pedira la clave correspondiente
git push git@github.com:Li7ewire/Dotfiles-Helying-Vallejos
```

5. Agregar actualizaciones de github a tus disco local
```zsh
git pull
```






