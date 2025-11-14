# SLICING
players = ["cr7", 'messi', 'Travis Kelce', 'chicharito', 'corona']
print(players[0:3]) # desde donde quiero, : , hasta donde -1.
# Slice es trabajar con un grupo especifico de elementos de una lista

print(players[1:4]) # ['messi', 'Travis Kelce', 'chicharito']
print(players[:4]) # players = ["cr7", 'messi', 'Travis Kelce', 'chicharito']
print(players[2:])

print(players[-3:])

print(players[-3:-1])
print(players[4:2])

# Slicing en for
players = ["axel", 'ignacio', 'Travis', 'chicha', 'corona', 'jorge']
first_three_player = players[0:3]
print("First three player: ", first_three_player)

print("Aqui vienen los 3 mejores del salon: ")
for player in players[0:3]:
    print(player)

# Copiar de lista
my_food = ['pizza', 'gorditas de jaumave', 'machacado']
# copy_of_food = my_food # Manera erronea de copiar una lista
copy_of_food_1 = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)

# Modificando elementos
cars = ['bwm', 'porch', 'masda', 'toyota', 'ford']
cars[0] = "bwm"
cars[1] = 'porch'
cars[2] = 'mazda'
cars[3] = 'toyota'

""" listas son datos mutables, tuplas no mutables """