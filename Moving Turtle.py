
import turtle

#Screen Setup
window = turtle.Screen()
window.title("Moving Turtle by Soumitro")
window.bgcolor('lightblue')
window.setup(width=800, height=600)

#Pointer head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.turtlesize(.5)
head.color("black")
head.goto(0,0)
head.direction="stop"

#Text Printing Window
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Start!", align="center", font=("Courier", 17, "normal"))

#Moving Function
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)

#Direction and others
def go_up():
        pen.clear()
        head.direction="up"
        move()
        pen.write("Up!", align="center", font=("Courier", 17, "normal"))

def go_down():
        pen.clear()
        head.direction="down"
        move()
        pen.write("Down!", align="center", font=("Courier", 17, "normal"))

def go_left():
        pen.clear()
        head.direction="left"
        move()
        pen.write("Left!", align="center", font=("Courier", 17, "normal"))

def go_right():
        pen.clear()
        head.direction="right"
        move()
        pen.write("Right!", align="center", font=("Courier", 17, "normal"))

def go_penup():
        pen.clear()
        head.penup()
        pen.write("Pen up!", align="center", font=("Courier", 17, "normal"))
        
def go_pendown():
        pen.clear()
        head.pendown()
        pen.write("Pen down!", align="center", font=("Courier", 17, "normal"))

def go_clear():
        pen.clear()
        head.clear()
        pen.write("Start!", align="center", font=("Courier", 17, "normal"))

#Key Inputs
window.listen()
#Key Bindings
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")
window.onkeypress(go_penup,"u")
window.onkeypress(go_pendown,"d")
window.onkeypress(go_clear,"c")

#Runs without restrictions
window.mainloop()
