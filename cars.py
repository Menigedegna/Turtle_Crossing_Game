from turtle import Turtle
from random import randint

MAX_CAR_LENGTH = 100
MIN_CAR_LENGTH = 20


class Car(Turtle):
    """cars, constantly moving from right to left border"""
    def __init__(self, car_height):
        super().__init__()
        self.shape("square")
        self.car_height = car_height
        self.car_length = randint(MIN_CAR_LENGTH, MAX_CAR_LENGTH)
        self.shapesize(stretch_len=self.car_length / 20, stretch_wid=self.car_height/20, outline=4)
        self.color(random_color(), "")
        self.penup()

    def move_car(self, car_pace):
        self.backward(car_pace)


def random_color():
    """returns a tuple of rgb colors"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b
