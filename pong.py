import turtle
import winsound
import easygui


window=turtle.Screen()
window.title("PONG by TRINA")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)   #stop the window from updating manually have to update


#paddle  A
paddle_a=turtle.Turtle()
paddle_a.speed(0)#the speed of animation;sets the speed the max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)#5 times 20
paddle_a.penup()
paddle_a.goto(-350,0)




#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)#the speed of animation;sets the speed the max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



#Ball
ball=turtle.Turtle()
ball.speed(0)#the speed of animation;sets the speed the max possible speed
ball.shape("square")
ball.color("white")
#paddle_a.shapesize(stretch_wid=5,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=-0.5


 #scoring system
 #pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B : 0",align="center",font=("Courier",24,"normal"))
#score
score_a=0
score_b=0


#function
#for paddle_a

def paddle_a_up():
    y=paddle_a.ycor() #from turtle module y cordinate
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor() #from turtle module y cordinate
    y-=20
    paddle_a.sety(y)
#keyboard binding

#for paddle_b
def paddle_b_up():
    y=paddle_b.ycor() #from turtle module y cordinate
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor() #from turtle module y cordinate
    y-=20
    paddle_b.sety(y)

#for ball
#     
#keyboard binding
window.listen()
#window.listen()
window.onkeypress(paddle_a_up,"u")
window.onkeypress(paddle_a_down,"d")

window.onkeypress(paddle_b_up,"h")
window.onkeypress(paddle_b_down,"l")




#main game loop
while True:
    window.update() #everytime loop runs screen update

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #boder checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1  
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {} Player B : {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {} Player B : {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    #paddle and ball collision
    if (ball.xcor()> 340  and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50) :
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if (ball.xcor()<-340  and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50) :
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
     
    if max(score_b,score_a)>=10:
        yn = easygui.ynbox('Game over', 'Continue?', ('Yes', 'No'))
        if yn == 'Yes':
            score_b=score_a=0
            pen.clear()
            pen.write("Player A: {} Player B : {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
            window.update()#  need to fix the yes catagory


        else :
            break
            
            

            

        
            

