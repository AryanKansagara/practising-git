import turtle

screen=turtle.Screen()

trtl=turtle.Turtle()

screen.setup(620,620)

screen.bgcolor('white')

clr=['red','green','blue','yellow','purple']

trtl.pensize(4)

trtl.shape('turtle')

trtl.penup()

trtl.pencolor('red')

trtl.write(str(),align="center",font=("Arial", 12, "normal")) 

trtl.home()

trtl.setpos(0,-250)

trtl.pendown()

trtl.pensize(10)

trtl.pencolor('blue')

trtl.circle(400)

trtl.penup()

trtl.setpos(-370,100)

trtl.pendown()

trtl.pencolor('green')

trtl.write('Happy friendship day',font=("Arial", 14,"normal"))

trtl.color("red")

trtl.begin_fill()

trtl.penup()

trtl.setpos(-70,200)

trtl.pensize(5)

trtl.left(50)

trtl.forward(133)

trtl.circle(50,200)

trtl.right(140)

trtl.circle(50,200)

trtl.forward(133)

trtl.end_fill()

trtl.hideturtle()

turtle.done()