#list comprehension simplies list iteration and new var creation
# we can use them for any sequence 
# list 
# range

from ast import Num
from numpy import square


numbers = [1, 2, 3]

# patterns expression for varName in existing list
new_numbers = [n + 1 for n in numbers]

name = "Jon"

new_name = [letter + 'bang' for letter in name]
 
new_range = [n * 2 for n in range(1, 5)]

#addition if check can be added to list comprehention
long_names = [name.upper() for name in ['ali', 'kenney'] if len(name) > 5]

squared_numbers = [n ** 2 for n in [2, 4]]

even_nums = [n for n in [2, 3, 4] if n % 2 == 0]

sentence = 'Velocity goes fast'

#covernt string to array
word_list = sentence.split()

value = { word: len(word) for word in word_list }


def convert_to_f (num: Num):
    return (num * 9/5) + 32

day_temps = {
    'Monday': 55,
    "Tuesday": 44
}

f_temps = { day: convert_to_f(temp) for (day, temp) in day_temps.items() }

print(f_temps)