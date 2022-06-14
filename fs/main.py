""" with open("my_file.txt") as file:

contents = file.read(); 

print(contents)

#closin is importaant
file.close() """

""" with open("my_file.txt", mode="a") as file: 
    file.write("\nNew next 2") """


#if file does not exist mode=w will create a new file
""" with open("new_file.txt", mode="w") as file: 
    file.write("This is a new file") """

PLACEHODER = "[name]"

with open("./names.txt") as names_file: 
   names = names_file.readlines()
   print(names)

with open('./letter.txt') as letter_file: 
    letter_contents = letter_file.read()
    for name in names: 
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHODER, stripped_name)
        with open(f'./letters/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
          completed_letter.write(new_letter)


   