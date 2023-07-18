from tkinter import *
from snakegame import SnakeGame
from scoreboard_ui import ScoreBoardUI

snakegame=SnakeGame()
score_board_ui=ScoreBoardUI()

window=Tk()
window.title=("Snake Game")
window.config(padx=50,pady=50,bg="white")

canvas=Canvas(width=220,height=172,highlightthickness=0,bg="white")
snake_img=PhotoImage(file="snake_logo.png")
canvas.create_image(110,86,image=snake_img)
canvas.grid(row=0,column=0,padx=10,pady=10)

start_button=Button(text="START",width=14,height=1,highlightthickness=0,bg="black",fg="white",border=8,command=snakegame.snakegame)
start_button.grid(row=1,column=0,padx=10,pady=10)

scoreboard_button=Button(text="SCORES",width=8,height=1,highlightthickness=0,bg="black",fg="white",border=8,command=score_board_ui.scoreboard_ui)
scoreboard_button.grid(row=2,column=0,padx=10,pady=10)

exit_button=Button(text="EXIT",width=4,height=1,highlightthickness=0,bg="black",fg="white",border=8,command=window.destroy)
exit_button.grid(row=3,column=0,padx=10,pady=10)

window.mainloop()