from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = file.read()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.refresh_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} - High Score:{self.high_score}', False, align='center',
                   font=("Courier", 20, "bold"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.refresh_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER BITCH', False, align='center', font=("Courier", 30, "bold"))
