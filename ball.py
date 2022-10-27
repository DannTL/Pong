from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setposition(position)
        self.move_speed = .1
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed = self.move_speed * .9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = .1
        self.bounce_x()

    def bounce_x_l_paddle(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    def bounce_x_r_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9
