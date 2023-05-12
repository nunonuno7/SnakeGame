from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("White")
        self.penup()
        self.speed("fastest")
        self.goto(-390, 370)
        self.score = 0
        self.update_score()
       

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', move=False, align='left', font=('Arial', 15, 'normal'))
     
    def increase_score(self):
        self.score += 1
        self.update_score()

        
       


