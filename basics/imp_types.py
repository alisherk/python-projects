
# 1
import turtle 

tim = turtle.Turtle()


# 2
from turtle import Turtle
tim = Turtle()
terry = Turtle()

# 3 
from turtle import *
#this can be confusing because now we can just pull methods like this from turtle module
forward(100) #becuase we might not know where this is coming from 
# this above way of importing is more obvious as where Tutle class is coming from 

# 3 aliase import 
import turtle as t

tim = t.Turtle()  # this as conveninient as we are importing all modules 

# but we can not import all modules like this for example heros module
