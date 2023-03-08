from turtle import Turtle

MOVING_DISTANCE = 10


class MainCharacter(Turtle):
    """create turtle object, user can interact with turtle to make it move up"""
    def __init__(self, screen, y_position):
        super().__init__()
        self.screen = screen
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.setheading(90)
        self.y_position = y_position

    def move_up(self):
        self.forward(MOVING_DISTANCE)

    def move_mc(self):
        """move turtle with Up keypad"""
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.move_up)

    def reset_mc(self):
        """reset turtle position"""
        self.goto(0, self.y_position)
