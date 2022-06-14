""" enemies = 1

def inscrease_enemies(): 
    enemies = 2
    print(f'enemies inside function: {enemies}')

inscrease_enemies()
print(f'enemies outside function: {enemies}');

# Local scope 

def drink_potion(): 
    potion_strength = 2
    print(potion_strength)

drink_potion(); 

# there is no Block scope in python 

game_level = 3; 

enemies = ['skeleton', 'zombie', 'alient']

if game_level < 5: 
    new_enemy = enemies[0]

# we can access new_enemy however we can't access it in the function
print(new_enemy) """


#Modify global scope 

""" enemies = 1

def increase_enemies(): 
    global enemies  # should not do this normally
    enemies += 1
    print(f'enemies inside function: {enemies}') """

# Capitalize global vars in Python 
PI = 3.14159 
URL ='https://www.google.com'

""" def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable) """

i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)


