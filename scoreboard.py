from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)
        self.current_score()

    def change_score(self):
        self.clear()
        self.score += 1
        self.current_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as high:
                high.write(str(self.high_score))
        self.score = 0
        self.current_score()

    def current_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)