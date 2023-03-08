from turtle import Turtle

MOVING_DISTANCE = 10


class MainCharacter(Turtle):
    def __init__(self, screen, y_position):
        super().__init__()
        '''create PC= the turtle'''
        self.screen = screen
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVING_DISTANCE)

    def move_mc(self):
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.move_up)

    def reset_mc(self, y_position):
        self.goto(0, y_position)