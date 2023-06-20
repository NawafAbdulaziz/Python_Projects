# import turtle moudel that help us to drew in scaraner
import turtle
wind=turtle.Screen() #creat first window in my life
wind.title("ping pong nawaf") # name the widow
wind.bgcolor("black")
wind.setup(width=800,height=600) #Screen size
wind.tracer(0) # block Screen from update tomatcly

# madreb1
madreb1=turtle.Turtle() #creat object Turtle
madreb1.shape("square")
madreb1.speed(0) #Screen drawing speed
madreb1.color("blue")
madreb1.shapesize(stretch_wid=5,stretch_len=1)# mul the oringnal zize(20,20)
madreb1.penup() # to stope draw
madreb1.goto(-350,0) # postion
# madreb2
madreb2=turtle.Turtle() #creat object Turtle
madreb2.shape("square")
madreb2.speed(0)
madreb2.color("red")
madreb2.shapesize(stretch_wid=5,stretch_len=1)# mul the oringnal zize
madreb2.penup() # to stope draw
madreb2.goto(350,0) # postion

#ball
ball=turtle.Turtle() #creat object Turtle(shep)
ball.shape("square")
ball.speed(0) #set speed of animation drawing
ball.color("white")
ball.penup() # to stope draw line when moving
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

# ruslit socer
socer1=0
socer2=0
socer=turtle.Turtle()
socer.speed(0)
socer.hideturtle() # hide the object from scrnner
socer.penup()
socer.color("white")
socer.goto(0,260)
socer.write("player1 :0 player2 :0  " ,align="center",font=("courier",24,"normal")) # write on scrnne


#funection
def madreb1_up():
    y=madreb1.ycor() #rutern position
    y+=20 #increc y  like ycor=340 +20
    madreb1.sety(y) #cheng  position  madreb1.ycor to new y
def madreb1_down():
    y=madreb1.ycor()
    y-=20
    madreb1.sety(y)

def madreb2_up():
    y=madreb2.ycor()
    y+=20
    madreb2.sety(y)

def madreb2_down():
    y=madreb2.ycor()
    y-=20
    madreb2.sety(y)

# keyboard binding
wind.listen() # tell the widow expet keyboard input
wind.onkeypress(madreb1_up,"a") # when press a call funection madreb1_up
wind.onkeypress(madreb1_down,"z")
wind.onkeypress(madreb2_up,"Up")# when press ArrowUp  call funection madreb2_up
wind.onkeypress(madreb2_down,"Down")


while True: # min game
    wind.update() # we update  Screen by my self
    ball.sety(ball.ycor() + ball.dy) #  time ball start with 0.2 then +dy=0.2
    ball.setx(ball.xcor() + ball.dx)

    #border check
    if ball.ycor()>290:#the end border is 290 +10(border up of ball) =300
        ball.sety(290)
        ball.dy*=-1 #to chaneg path ball to Reverse

    if ball.xcor() > 400: # if ball out the border
        ball.goto(0,0)
        socer1+=1
        socer.clear()  # clear last writ (ruslt)
        socer.write("player1 :{}  player2 : {}  ".format(socer1,socer2), align="center", font=("courier", 24, "normal"))
        ball.dx *= -1

    if ball.ycor() < -290:  # the end border is 290 +10(border up of ball) =300
        ball.sety(-290)
        ball.dy *= -1  # to chaneg path ball to Reverse

    if ball.xcor()<-400:
        ball.goto(0,0)
        socer2 += 1
        socer.clear()
        socer.write("player1 :{}  player2 : {}  ".format(socer1, socer2), align="center", font=("courier", 24, "normal"))

        ball.dx *= -1
        # +10
    if (ball.xcor()+10>340 and ball.xcor()<340) and (ball.ycor()+10 < madreb2.ycor()+50 and ball.ycor()+10 >madreb2.ycor()-50 ):
        ball.dx *= -1
        # ball.dy *= -1  # to chaneg path ball to Reverse
    if (ball.xcor()+10> -350 and ball.xcor()<-340) and (ball.ycor()+10 <madreb1.ycor()+50 and ball.ycor()+10 >madreb1.ycor()-50 ):
        ball.dx *= -1
        # ball.dy *= -1  # to chaneg path ball to Reverse