""" import math

bill = input('What is your total bill ')

tip = input('what is your tip ')

people = input('how many people would like to split the bill ')

bill_converted = int(bill)

sub_total = ((int(tip) / 100) * bill_converted) + bill_converted

total = sub_total / int(people) 

print(round(total, 2)) """


