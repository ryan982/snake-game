import turtle as t
import random

wn = t.getscreen()
wn.setup(width = 1000, height = 800)
wn.bgcolor("light blue")

head = t.Turtle()
head.shape("square")
head.setpos(0, 0)
x = head.xcor()
y = head.ycor()

def forward():
    head.penup()
    x = head.xcor()
    if head.xcor() >= 400:
        head.setx(400)    
        print("over")
    else:
        head.setx(x+10)


def up():
    head.penup()
    y = head.ycor()
    if head.ycor() >= 390:
        head.sety(390)    
        print("over")
    else:
        head.sety(y+10)
   

def down():
    head.penup()
    y = head.ycor()
    if head.ycor() <= -390:
        head.sety(-390)    
        print("over")
    else:
        head.sety(y-10)

def left():
    head.penup()
    x = head.xcor()
    if head.xcor() <= -400:
        head.setx(-400)    
        print("over")
    else:
        head.setx(x-10)
   
wn.onkey(forward, "Right")
wn.listen()

wn.onkey(up,"Up")
wn.listen()

wn.onkey(down, "Down")
wn.listen()

wn.onkey(left, "Left")
wn.listen()

#food
food = t.Turtle()
food.shape("circle")
food.color("green") 
food.speed(100)

#body 

#body = t.Turtle()
#body.shape("circle")
#body.color("blue")
#body.penup()

body = []

while True:
    wn.update()

    if head.distance(food) <= 15: 
                
        food.penup()
        xf = random.randint(-400,400)
        yf = random.randint(-400,400)
        food.goto(xf, yf)

        ibody = t.Turtle()
        ibody.shape("circle")
        ibody.color("black")   
        ibody.penup()
        ibody.speed(1000)
        body.append(ibody)
        
    for index in range(len(body)-1, 0 ,-1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x,y)
        
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

t.Screen().exitonclick()