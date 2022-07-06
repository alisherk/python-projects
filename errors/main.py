
try:
 file = open('a_file.txt')
 a_dict = {"key": "value"}
 print(a_dict['asd'])
except FileNotFoundError: 
  file = open('a_file.txt', 'w')
  file.write('Hello')

except KeyError as error_message: 
  print(f"The key {error_message} does not exist")
finally:
  raise TypeError("This is the error I made up")


