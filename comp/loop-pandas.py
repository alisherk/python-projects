from distutils.util import split_quoted
import pandas

student_dic = {
    "student": ["Bob", "Jon"], 
    "score": [55, 56]
}

student_data_frame = pandas.DataFrame(student_dic)


""" for(key, value) in student_data_frame.items():
   print(value) """

#Loop thru rows in pandas 
""" for (index, row) in student_data_frame.iterrows():
  print(row.score) """

#TODO 1. CREATE A dictionary in 

{"A": "Alfa"}

#TODO 2: Give alphae number prompts based on the word typed 

data = pandas.read_csv('nato_phonetic_alphabet.csv')

print(data)

dict ={ row.letter: row.code for (index, row) in data.iterrows() }

word = input('Type a word ').upper()

output = [dict[letter] for letter in word]

print(output)





