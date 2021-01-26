from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.refresh_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.write(f'Score : {self.score}', False, align='center', font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER BITCH', False, align='center', font=("Courier", 30, "bold"))