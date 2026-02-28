#simple pong game (badminton like)
# by atul game 1 in vs code 
import turtle

wn = turtle.Screen()
wn.title("pong game by ATUL\n")   
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)#stop the windows and 

#score
scorea = 0
scoreb = 0


# paddle left
paddlea = turtle.Turtle()
paddlea.speed(0)#sets the speed 
paddlea.shape("square")
paddlea.color("white")
paddlea.shapesize(stretch_wid= 5,stretch_len=1)
paddlea.penup()
paddlea.goto(-350, 0 )


# paddle right
paddleb = turtle.Turtle()
paddleb.speed(0)#sets the speed 
paddleb.shape("square")
paddleb.color("white")
paddleb.shapesize(stretch_wid= 5,stretch_len=1)
paddleb.penup()
paddleb.goto(350, 0 )

# ball game
ball = turtle.Turtle()
ball.speed(0)#sets the speed 
ball.shape("square")
ball.color("white")
#paddlea.shapesize(stretch_wid= 5,stretch_len=1)
ball.penup()
ball.goto(0, 0 )
ball.dx = 2
ball.dy = -2


# score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font= ("Courier", 24, 'normal'))



#funtion to move 
def paddleaup():
    y=paddlea.ycor()
    y += 20 # add the 20 pix in the 
    paddlea.sety(y)

def paddleadown():
    y=paddlea.ycor()
    y -= 20 # add the 20 pix in the 
    paddlea.sety(y)
    
def paddlebup():
    y=paddleb.ycor()
    y += 20 # add the 20 pix in the 
    paddleb.sety(y)

def paddlebdown():
    y=paddlea.ycor()
    y -= 20 # add the 20 pix in the 
    paddleb.sety(y)



#keyboard typing binding 
wn.listen()
wn.onkeypress(paddleaup, "w")
wn.onkeypress(paddleadown, "s")
wn.onkeypress(paddlebup, "p")
wn.onkeypress(paddlebdown, "l")




while True:
    wn.update()


    #movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #broder checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy += -1
    
    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx += -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx += -1 
        scorea += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scorea, scoreb), align="center", font= ("Courier", 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx += -1 
        scoreb += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scorea, scoreb), align="center", font= ("Courier", 24, 'normal'))


    # paddle and ball collisona
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddleb.ycor() + 50 and ball.ycor() > paddleb.ycor() -40):
        ball.setx(340)
        ball.dx += -1

    if (ball.xcor() > -340 and ball.xcor() < -350 ) and (ball.ycor() < paddlea.ycor() + 50 and ball.ycor() > paddlea.ycor() -40):
        ball.setx(-340)
        ball.dx += -1

