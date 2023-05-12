from turtle import *
import time
from food import Food
from scoreboard import ScoreBoard


class Snake():
    def __init__(self):
        self.food = Food()
        self.scoreboard = ScoreBoard()  # Added ScoreBord object
        self.screen = Screen()
        self.direction_timer = time.time()
        self.screen.setup(width=800, height=800)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()
        self.score = 0
        self.speed = 0.05
        self.snake_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_objects = []
        self.screen.title("Snake Game")

        for pos in self.snake_positions:
            sn = Turtle(shape="square")
            sn.color("white")
            sn.penup()
            sn.goto(pos)
            self.snake_objects.append(sn)
        
        self.head = self.snake_objects[0]
        self.current_direction = "up"
        self.head_position = self.head.position()
        
        self.screen.onkeypress(self.turn_right, "Right")
        self.screen.onkeypress(self.turn_left, "Left")
        self.screen.onkeypress(self.turn_down, "Down")
        self.screen.onkeypress(self.turn_up, "Up")

    def move_or_teleport(self):
        x_coordinate = self.snake_positions[0][0]
        y_coordinate = self.snake_positions[0][1]
    
        if not (-415 < x_coordinate < 415) and (not(-415 < y_coordinate < 415)):
            print("bug")
        elif not (-415 < x_coordinate < 415):
            self.snake_objects[0].goto(-x_coordinate,y_coordinate)
            self.head.forward(20)
        elif not (-415 < y_coordinate < 415):
            self.snake_objects[0].goto(x_coordinate,-y_coordinate)
            self.head.forward(20)
        else:
            self.head.forward(20)
    
    def move(self):
        if self.current_direction == "up":
            self.head.setheading(90)
            self.move_or_teleport()
        elif self.current_direction == "down":
            self.head.setheading(270)
            self.move_or_teleport()
        elif self.current_direction == "right":
            self.head.setheading(0) 
            self.move_or_teleport()
        elif self.current_direction == "left":
            self.head.setheading(180)
            self.move_or_teleport()

    def turn_right(self):
        if self.current_direction != "left" and time.time() - self.direction_timer > 0.05:
            self.current_direction = "right"
            self.direction_timer = time.time()

    def turn_left(self):
        if self.current_direction != "right" and time.time() - self.direction_timer > 0.05:
            self.current_direction = "left"
            self.direction_timer = time.time()

    def turn_up(self):
        if self.current_direction != "down" and time.time() - self.direction_timer > 0.05:
            self.current_direction = "up"
            self.direction_timer = time.time()

    def turn_down(self):
        if self.current_direction != "up" and time.time() - self.direction_timer > 0.03:
            self.current_direction = "down"
            self.direction_timer = time.time()
                                    
    def update_snake_positions(self):
        for i in range(len(self.snake_objects) - 1, 0, -1):
            self.snake_objects[i].goto(self.snake_positions[i-1])
            self.snake_positions[i] = self.snake_objects[i].position()
        
        self.snake_positions[0] = self.head_position
           
    def screen_update(self):
        self.screen.update()
        time.sleep(self.speed)
         
    def new_doot(self):
        sn = Turtle(shape="square")
        sn.color("white")
        sn.penup()
        sn.speed("fastest")
        sn.goto(self.snake_positions[-1])
        self.snake_objects.append(sn)
        self.snake_positions.append(sn.position())

    def check_food(self):
        if self.head.distance(self.food)<15:   
             self.food.refresh()
             self.scoreboard.increase_score()
             self.new_doot()
        
    def game_on(self):
        for position in self.snake_positions[1:]:
            if self.head.distance(position) < 10:
                print(f"Game Over score: {self.score}")
                color("White")
                write(f'Game Over', move=False, align='left', font=('Arial', 15, 'normal'))
                return
        self.screen.ontimer(self.continuous_move, 1)
        

    def continuous_move(self):
        self.move()
        self.head_position = self.head.position()
        self.update_snake_positions()
        self.screen_update()
        self.check_food()
        self.game_on()
            
    def start(self):
        self.continuous_move()
        self.screen.exitonclick()
        