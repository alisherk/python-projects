""" import csv

with open('./weather_data.csv') as data_file: 
    data = csv.reader(data_file)
    temps = []
    for row in data: 
        if row[1] != 'temp':
         temps.append(int(row[1]))
    print(temps)
 """
 

import pandas

data = pandas.read_csv('weather_data.csv')

print(data)

# print(type(data)) #data frame in pandas

# print(type(data['temp'])) #series in pandas

# data_dict = data.to_dict() converts to dictinary

temp_list = data['temp'].to_list()

""" temp_sum = 0
for temp in temp_list: 
    temp_sum =+ temp

print(temp_sum / len(temp_list)) """

# print(data['temp'].mean())

# get max print(data['temp'].max())

# print(data[data.temp == data.temp.max()]) 

""" monday = data[data.day == 'Monday']

monday_temp = int(monday.temp)

F = monday_temp * 9/5 + 32

data_dict = {
    'students': ['Amy']
}

data = pandas.DataFrame(data_dict)

data.to_csv('test_csv.csv') """


data = pandas.read_csv('squirrel_data.csv')
grey_squirels_cnt = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirels_cnt = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirels_cnt = len(data[data['Primary Fur Color'] == 'Black'])

data_dic = {
    "Fur Color": ["Gray", "Cinammon", "Black"], 
    "Count": [grey_squirels_cnt, red_squirels_cnt, black_squirels_cnt]
}

df = pandas.DataFrame(data_dic)

df.to_csv('squirrel_counts.csv')


