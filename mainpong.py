import turtle

wd = turtle.Screen()
wd.title("Ping Pong")
wd.bgcolor("black")
wd.setup(width=800, height=600)
wd.tracer(0)

#score
score1 = 0
score2 = 0

#player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

#player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#pen
tur = turtle.Turtle()
tur.speed(0)
tur.color("white")
tur.penup()
tur.hideturtle()
tur.goto(0, 260)
tur.write("Player 1: {}     Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

#ball movement
ball.dx = 0.1
ball.dy = 0.1


#functions
def player1Up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1Down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2Up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2Down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)

#key binding
wd.listen()
wd.onkeypress(player1Up, "w")
wd.onkeypress(player1Down, "s")
wd.onkeypress(player2Up, "Up")
wd.onkeypress(player2Down, "Down")

#While game is running
while True:
    wd.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() <  -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        tur.clear()
        tur.write("Player 1: {}     Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        tur.clear()
        tur.write("Player 1: {}     Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    #paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
