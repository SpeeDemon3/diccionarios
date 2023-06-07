### Diccionarios -> pares CLAVE - VALOR ###
# Un diccionario va entre {}
# Diccionario simple
dog_1 = {'name': 'chula', 'color': 'brown'} # Diccionario simple con nombre y color de un perro

print(dog_1['name']) # Imprimo el nombre
print(dog_1['color']) # Imprimo el color

print(dog_1) # Imprimo toda la informacion

# Añadir nuevos valores clave valor
dog_1 ['x_position'] = 0 # Añado una nueva clave valor
dog_1 ['y_position'] = 33 # Añado una nueva clave valor

print(dog_1) # Ahora imprimira las claves valor que ya tenia mas las nuevas que he añadido

# Empezar con un diccionario vacio
dog_2 = {} # Creo el diccionario vacio

dog_2 ['name'] = 'nala' # Añado una nueva clave valor
dog_2 ['color'] = 'red' # Añado una nueva clave valor

print(dog_2)

# Eliminar pares clave-valor
del dog_2['color'] # Utilizando la sentencia del elimino la clave color y su valor asociado a esa clave

print(dog_2)

# Diccionario de objetos
favorite_lenguages = {
    'Antonio' : 'Java',
    'Arya' : 'JavaScript',
    'Chula' : 'Python',
    'Patricia' : 'C++'
}

lenguage = favorite_lenguages['Antonio'].title() # Asigno a la variable el valor de la clave 'Antonio'

print(f"Antonio's favorite lenguage is {lenguage}")

# Usar el metodo get() para acceder a los valores
chula_lenguage = favorite_lenguages.get('chula'.title()) # Al condicir el nombre de la clave gracias al metodo title() me devuelve el valor asociado a la clave 'Chula'
print(chula_lenguage)

spiderman_lenguage = favorite_lenguages.get('Spiderman') # Al no encontrar la clave 'Spiderman'
print(spiderman_lenguage) # Imprimira en consola 'none' indicando que no existe

# Como segundo parametro podemos indicar que imprimir si la clava no existe
batman_lenguage = favorite_lenguages.get('Batman', 'Not exists')
print(batman_lenguage) # Al no existir imprimira 'Not exists'

# Personas
spiderman = {
    'first_name' : 'Peter',
    'last_name' : 'Parker',
    'age' : 18,
    'city' : 'Manhattan',
}

print(spiderman)

# Dicionario persona
person = {
    'name' : 'Antonio',
    'age' : 36,
    'country' : 'Madrid'
}

name = person.get('name')
print(name)

### Recorrer el diccionario con un bucle for
## Pasando 2 variables, una para la clave y otra para el valor
for key, value in person.items(): # El metodo item() devuelve una lista de clave : valor
    print(f"Key -> {key} || Value -> {value}\n")


favorite_lenguages2 = {
    'Antonio' : 'Java',
    'Arya' : 'JavaScript',
    'Chula' : 'Python',
    'Patricia' : 'C++'
}

for name, lenguage in favorite_lenguages2.items():
    print(f"Name: {name} || Favorite Lenguage: {lenguage}")

### Recorrer con un bucle for todas las claves del diccionario 'favorite_lenguage2'
# Utilizando el metodo keys()
for name in favorite_lenguages2.keys():
    print(name)

# SIN utilizar el metodo keys() el resultado seria el mismo
for name in favorite_lenguages2:
    print(name)

pet_and_child = ['Chula', 'Arya'] # Lista con los usuarios que recibiran un mensaje especial

# Utilizando un bucle for recorro el diccionario
for name in favorite_lenguages2.keys():
    print(f"Hi {name}") # Imprimo un saludo a cada usuario

    if name in pet_and_child: # Si el usuario esta dentro de la lista pet_and_child
        lenguage = favorite_lenguages2[name] # Guardo el valor de la clave en una variable
        print(f"{name}, I see you love {lenguage}") # Imprimo un mensaje personalizado


### Comprovar si un usuario realizo la encuesta
if 'Peter' not in favorite_lenguages2.keys(): # Si 'Peter' no esta en favorite_lenguages2
    print('Peter, please take our poll')

### Recorrer el diccionario por las claves en un orden particular

favorite_lenguages3 = {
    'Phuniser' : 'C',
    'Antonio' : 'Java',
    'Lobezno' : 'Ruby',
    'Arya' : 'JavaScript',
    'Chula' : 'Python',
    'AntMan' : 'Java',
    'Patricia' : 'C++'
}

# Utilizando la funcion sorted se ordenan en orden alfabetico las claves del diccionario
for name in sorted(favorite_lenguages3.keys()):
    print(name)

# Recorrer el bucle solo obteniendo los valores del diccionario utilizando el metodo values()
for lenguage in favorite_lenguages3.values():
    print(lenguage)

# Sacar los elementos sin repeticiones utilizando el metodo set()
for lenguage in set(favorite_lenguages3.values()):
    print(f"\t{lenguage}")

# Soccer_player
# Diccionario de jugadores
soccer_player = {
    'vinicius' : 'real madrid',
    'oblak' : 'atletico de madrid',
    'mbappe' : 'paris'
}

for player in soccer_player:
    team = soccer_player[player]
    print(f"{player.title()} playing in {team.title()}")

for player in soccer_player.keys():
    print(player.title())

for values in set(soccer_player.values()):
    print(values.title())

the_best_players = ['messi', 'vinicius']

for player in soccer_player.keys():
    print(player)

    if player not in the_best_players:
        print(f'{player} is not among the best')


# Personas

# Creo 3 diccionarios con la informacion de personas
person_1 = {
    'first_name': 'Antonio',
    'last_name': 'Ruiz',
    'city': 'Madrid',
    'age': 36
}
person_2 = {
    'first_name': 'Arya',
    'last_name': 'Ruiz',
    'city': 'Madrid',
    'age': 4
}
person_3 = {
    'first_name': 'Patricia',
    'last_name': 'Luengo',
    'city': 'Madrid',
    'age': 39
}

# Añado los diccionarios a una lista
list_people = [person_1, person_2, person_3]

# Recorro la lista
for person in list_people:
    print(person)


