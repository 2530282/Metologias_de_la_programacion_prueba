# Simple dictionary
alien_0 = {'color': 'green', 'points': 5}
 
# The simpliest dictionary
alien_1 = {'color': 'yellow'}

# Accessing values in a dictionary
print(alien_1['color'])
print(alien_0['points'])

# Empty dictionary
alien_2 = {}

# Modifying values in a dictionary
alien_2 = {'color': 'yellow'}
alien_2['color'] = 'blue'

# Adding new key-value pairs
alien_2['x_position'] = 0
alien_2['y_position'] = 25

print(alien_2)

## Dictionary to store similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby',
    'phil': 'python',
}

# print(f"Sarah favorite language is {favorite_languages['sarah']}")

# Looping through all key-value pairs
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite\
           language is {value.title()}.") 

# Looping through all keys or values
for key in favorite_languages.keys():
    print(key)

# Looping through all values
for value in favorite_languages.values():
    print(value)

# Nesting dictionaries (investigarlo)

## Listas de diccionarios
## Listas en diccionarios
## Diccionarios en diccionarios

covenant_jackal = {
    'color': 'gray',
    'weapon': 'plasma-gun',
    'strength': 75,
    'weakness': 'shields',
}

## Listas en diccionarios
students = {
    'alice': ['math', 'science'],
    'bob': ['history', 'art'],
    'carol': ['math', 'art', 'science'],
}

## Diccionarios en diccionarios
sensors = {
    'temperature':{
        'value': 22.5,
        'unit': 'Celsius',
        'location': 'living room',
    },
    'humidity':{
        'value': 45,
        'unit': '%',
        'location': 'living room',
    }
}

print(sensors['temperature']['value'])  # Output: 22.5
print(sensors['humidity']['unit'])      # Output: % 
