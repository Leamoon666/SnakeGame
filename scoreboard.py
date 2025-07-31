from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)
        self.current_score()

    def change_score(self):
        self.clear()
        self.score += 1
        self.current_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def current_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)