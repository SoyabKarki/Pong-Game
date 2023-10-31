from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.x = x_pos
        self.y = y_pos
        self.create_paddle()

    def create_paddle(self):
        self.color("white")
        self.speed(0)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=self.x, y=self.y)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)
