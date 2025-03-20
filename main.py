import turtle
import random
from unicodedata import numeric

screen = turtle.Screen()
screen.screensize(500, 500)
screen.bgcolor("black")
t = turtle.Turtle()

#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("background color ",font=("arial",30,"normal"),align="center")
t.penup()
t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor("tan")
t.write("1.tan ",font=("arial",30,"normal"),align="left")
t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor("azure")
t.write("2.azure ",font=("arial",30,"normal"),align="left")
t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor("aquamarine")
t.write("3. aqua marine ",font=("arial",30,"normal"),align="left")
t.penup()
t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor("darkkhaki")
t.write("4.dark khaki ",font=("arial",30,"normal"),align="left")
t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("white")
t.write("Choose One ",font=("arial",30,"normal"),align="center")

name = input("Enter your name :")
num1 = int(input("Enter a number :"))
num2 = int(input("Enter another number :"))

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("red")
t.write(name,font=("arial",30,"normal"),align="center")


t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("blue")
t.write(num1,font=("arial",30,"normal"),align="center")

t.write(name,font=("arial",30,"normal"),align="center")
t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("red")
t.write(name,font=("arial",30,"normal"),align="center")
choose = int(input(  ))
if choose == 1:

 screen.bgcolor('tan')
elif choose == 2:
 screen.bgcolor('azure')

elif choose == 3:
 screen.bgcolor('aquamarine')
else:
 screen.bgcolor('darkkhaki')
t.clear()
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('black')
t.write("Enter Your Name",font=("arial",30,"normal"),align="center")

name = input("Enter your name: ")
t.clear()

