from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",21,"normal")
FONT_2=("Arial",15,"normal")

class Scoreboard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.score=0
        self.highscore=0
        with open("highscores.txt","r") as file:
            self.highscore=file.read()
            self.highscore=int(self.highscore)
        self.color("white")
        self.write(arg=f"Press 'space' to start the Game.",align=ALIGNMENT,font=FONT_2)
    
    def write_score(self) :
        self.clear()
        self.penup()
        self.goto(-90,250)
        self.color("white")
        self.write(arg=f"Score : {self.score}",align=ALIGNMENT,font=FONT)
        self.goto(90,250)
        self.write(arg=f"High Score : {self.highscore}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
    
    def increase_score(self) :
        self.score += 1
    
    def update_highscore(self) :
        self.highscore=self.score
        with open("Scores/highscores.txt","w+") as file:
            file.write(str(self.highscore))

    def game_over(self) :
        self.color("red")
        self.penup()
        self.goto(0,10)
        self.write(arg=f"GAME OVER",align=ALIGNMENT,font=FONT)
        if self.score > self.highscore :
            self.update_highscore()
        self.goto(0,-30)
        self.write(arg=f"Press 'space' to start the game again.",align=ALIGNMENT,font=FONT_2)
        self.hideturtle()
        self.score=0