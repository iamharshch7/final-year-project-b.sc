import turtle
import random
import time

delay =0.1
score =0
high_score=0

screen=turtle.Screen()
screen.title("Snake game")
screen.bgcolor("black")
screen.setup(width = 600,height=600)
screen.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.shape("square")
food.speed(0)
food.color("red")
food.penup()
food.goto(0,100)

segments = []

pen=turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.color("white")
# function to update score display
def update_score():
    pen.clear()
    pen.write(f"score:{score}   |  high score:{high_score}",
                                                    align = "center",
              font=("courier",20,"normal",))
    update_score()

def go_up ():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    elif head.direction=="down":
         y=head.ycor()
         head.sety(y-20)
    elif head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    elif head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")


def game_loop():
    global score, high_score

    screen.update()

    #border collision
    if head.xcor()>290:
        head.setx(-290)
    elif head.xcor()<-290:
        head.setx(290)

    if head.ycor()>290:
        head.sety(-290)
    elif head.ycor()<-290:
        head.sety(290)



# Food collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score+=10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(
            f"score: {score} high score: {high_score}",
            align="center",
            font=("Courier", 20, "normal"))

    #Move the segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y= segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for self collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"


            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            score = 0
            pen.clear()
            pen.write(
                f"score: {score} high score: {high_score}",
                align="center",
                font=("Courier",20,"normal"))

    #repeat the loop
    screen.ontimer(game_loop,int(delay*1000))

# start the game
game_loop()
screen.mainloop()