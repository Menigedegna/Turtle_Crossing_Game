from turtle import Turtle

MOVING_DISTANCE = 20


class Player(Turtle):
    """create turtle object, user can interact with turtle to make it move up"""
    def __init__(self, screen, y_position):
        super().__init__()
        self.screen = screen
        self.shape("turtle")
        self.shapesize(outline=3)
        self.color((255, 97, 3), (34,139,34))
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
