# TODO game doesn't detect car collision very well : not whole body of cars anyway
# TODO feat: when turtle gets to top, restart at the bottom and increase speed of cars


from turtle import Screen, Turtle
from cars import Car
from random import randint
import time
from crossing_turtle import MainCharacter

# screen variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"
MARGIN = 30

# car variables
CAR_LANE_NUMBER = 20
MAX_NUMBER_CARS = 10
GAP_BN_CARS = 5

# variables for game status display
STATUS_BG_COLOR = "black"
STATUS_TXT_COLOR = "white"
STATUS_FONT = ("Times New Roman", 15, "normal")
STATUS_ALERT_WIDTH = 100
STATUS_ALERT_HEIGHT = 100


class CrossingGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(SCREEN_BG_COLOR)
        self.screen.colormode(255)
        self.screen.tracer(0)

        # get corner coordinates
        self.y_min = -1 * round(SCREEN_HEIGHT/2) + MARGIN
        self.y_max = -1 * self.y_min
        self.x_min = -1 * round(SCREEN_WIDTH/2) + MARGIN
        self.x_max = -1 * self.x_min

        '''create turtle'''
        self.crossing_turtle = MainCharacter(screen=self.screen, y_position=self.y_min - MARGIN)
        self.screen.update()

        '''create cars'''
        self.car_height = round((SCREEN_HEIGHT - 2 * MARGIN) / CAR_LANE_NUMBER)
        self.cars = [Car(car_height=self.car_height) for _ in range(CAR_LANE_NUMBER)]
        self.screen.update()

        '''create turtle to display game status'''
        self.status = Turtle(shape="square")
        self.status.hideturtle()
        self.status.shapesize(stretch_wid=STATUS_ALERT_WIDTH / 20, stretch_len=STATUS_ALERT_HEIGHT / 20)

        # keep track of game status
        self.game_is_on = True

    def display_status(self, text):
        """display status of the game: game is on, reset game or game over"""
        self.status.color(STATUS_BG_COLOR)
        self.status.stamp()
        self.status.color(STATUS_TXT_COLOR)
        self.status.write(f"{text}", align="center", font=STATUS_FONT)

    def start_game(self):
        self.screen.update()
        time.sleep(0.06)
        self.crossing_turtle.move_mc()
        for car in self.cars:
            car.move_car()

            # if car reaches left border => loops back from right border
            if car.xcor() <= self.x_min:
                car.goto(self.x_max, car.ycor())

            # if collision with car => game over
            distance_from_cars = [self.crossing_turtle.distance(car) for car in self.cars]
            if min(distance_from_cars) <= 10:
                self.display_status("GAME OVER")
                self.game_is_on = False

    def set_game(self):
        # position crossing turtle
        self.crossing_turtle.reset_mc(y_position=self.y_min - MARGIN)
        # position cars
        random_position_list = create_random_position(self.car_height, self.y_min, self.x_min, self.x_max)
        self.cars = position_cars(self.cars, random_position_list)
        # clear display
        self.status.clear()
        self.screen.update()
        self.game_is_on = True
        # start game
        while self.game_is_on:
            self.start_game()
        self.screen.listen()
        self.screen.onkey(key="space", fun=self.set_game)


def create_random_position(lane_height, y_min, x_min, x_max):
    """return list of random positions"""
    half_lane_height = round(lane_height / 2)
    all_car_y_positions = [y_min + a * half_lane_height for a in range(1, 2 * CAR_LANE_NUMBER, 2)]
    position_list = []
    for y_position in all_car_y_positions:
        x_position = randint(x_min, x_max)
        position = (x_position, y_position)
        position_list.append(position)
    return position_list


def position_cars(car_list, position_list):
    result = []
    for car, position in zip(car_list, position_list):
        car.goto(position)
        result.append(car)
    return result
