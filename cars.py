from turtle import Turtle
from random import randint

MAX_CAR_LENGTH = 100
MIN_CAR_LENGTH = 20
MOVING_DISTANCE = 10


class Car(Turtle):
    """ball for game, is constantly moving and bounces off paddles and horizontal borders"""
    def __init__(self, car_height):
        super().__init__()
        self.shape("square")
        self.car_height = car_height
        self.car_length = randint(MIN_CAR_LENGTH, MAX_CAR_LENGTH)
        self.shapesize(stretch_len=self.car_length / 20, stretch_wid=self.car_height/20)
        self.color(random_color(), "")
        self.penup()

    def move_car(self):
        self.backward(MOVING_DISTANCE)


def random_color():
    """returns a tuple of rgb colors"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b
