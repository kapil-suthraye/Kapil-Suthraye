import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
bcolorlist = [ 'yellow' , 'blue', 'orange' ,'green', 'red']
k = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
wn.setup(width = 600, height = 600)
wn.tracer(0)

head = turtle.Turtle()
hshape = random.choice(['circle', 'square'])
bshape = hshape
head.shape(hshape)
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "Stop"

food = turtle.Turtle()
colors = ['gray','purple','pink','brown']
shapes = ['oval' ,'circle']
food.speed(0)
food.shape(random.choice(shapes))
food.color(random.choice(colors))
food.penup()
food.goto(0,100)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0   HighScore : 0", align = "center", font = ("candara",24,"bold"))

def goup():
    if head.direction != "down" :
        head.direction = "up"
def godown():
    if head.direction != "up":
        head.direction = 'down'

def goright():
    if head.direction != "left":
        head.direction = "right"

def goleft() :
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down" :
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "left" :
        x = head.xcor()
        head.setx(x-20)

wn.listen()
wn.onkeypress(goup , "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goright, "d")
wn.onkeypress(goleft, "a")
segments = []

while True :
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {}   HighScore : {} ".format(score,high_score), align = "center", font = ("candara", 24, "bold"))
    if head.distance(food) < 20 :
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(bshape)
        if len(segments) % 10 == 0:
            bcolor = bcolorlist[k]
            k = k+1
        new_segment.color(bcolor)
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {}   HighScore : {} ".format(score,high_score), align = "center" , font = ("candara", 24, "bold"))
    for index in range(len(segments)-1,0,-1) :
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments :
        if segment.distance(head) < 20:
            time.sleep(0)
            head.goto(0,0)
            head.direction = "stop"
            colors = random.choice(bcolorlist)
            shapes = random.choice(shapes)
            for segment in segments:
                segment.goto(1000,1000)
            segment.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score = {}   HighScore = {}".format(score,high_score), align = "center", font = ("candara", 24, "bold"))
    time.sleep(delay)
wn.mainloop()