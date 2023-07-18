from tkinter import *
from data_manager import DataManager


class ScoreBoardUI:

    def scoreboard_ui(self):
        data_manager = DataManager()

        window_scoreboard = Tk()
        window_scoreboard.config(padx=10, pady=10)

        serial_label = Label(window_scoreboard, text="Serial No.", width=10)
        serial_label.grid(row=2, column=1)

        name_label = Label(window_scoreboard, text="Player Name", width=20)
        name_label.grid(row=2, column=2)

        score_label = Label(window_scoreboard, text="Score", width=10)
        score_label.grid(row=2, column=3)

        serial_no = 0
        for name, score in data_manager.read_data().items():
            serial_no += 1
            row = serial_no + 2
            serial_label = Label(window_scoreboard, text=f"{serial_no}.", width=10)
            serial_label.grid(row=row, column=1)

            name_label = Label(window_scoreboard, text=name.title(), width=20)
            name_label.grid(row=row, column=2)

            score_label = Label(window_scoreboard, text=score, width=10)
            score_label.grid(row=row, column=3)

        window_scoreboard.mainloop()
