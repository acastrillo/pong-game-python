from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"P1 Score: {self.left_score} - {self.right_score} :P2 Score", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self, score_side):
        if score_side == "left":
            self.left_score += 1
            self.clear()
            self.update_scoreboard()
        elif score_side == "right":
            self.right_score +=1
            self.clear()
            self.update_scoreboard()

        
