# api_res_framework
#Python 3.8.5
#Probado en Windows 10 con Django 3.1 


#Paso 1 "Instalacion de la Base de Datos"
#Instalar la base de datos de mongo en Django, ingresa al archo api_res_framework\ProyectoRes\ProyectoRes\settings.py
#Una ves ingresado cambias los datos de DATABASES con los de tubase de datos.

#Ejemplo

#DATABASES = {
# 'default': {
#        'ENGINE': 'django',
#        'NAME': 'Mi_Base', # Nombre de la base de datos
#        'HOST':'', # Ruta de la host ejemplo: mongodb://juan:clave123@259144.mlab.com:27001/Mi_Base 
#        'USER': 'juan', # aqui va el usuario con el cual tienes mongodb
#        'PASSWORD':'clave1', # tu contraseña de mongodb
        
#    }
#}

#Guardas los cambios y ingresas a la tu consola y escribes

# python manage.py migrate #Este comado ara que cargue la base de datos que tienes en tu Django

# Solo podras ejecutar este comando si estas dentro de tu proyecto caso contrario no funcionara

# Revisa que los datos que tenias en tu Django se ayan implementado en tu base de datos.


# Paso 2 "Creacion de Super Usuario"

#Es necesario crear un super usuario para eso ingresas el siguiente comando

# createsuperuser

#una ves creado al super usuario ya puedes poner a correr a tu servidor y probar el repositorio

