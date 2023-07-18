import turtle as t 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from data_manager import DataManager

class SnakeGame() :
    def __init__(self) :
        pass
    def snakegame(self) :
        screen=t.Screen()
        screen.setup(width=600,height=600)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)
        player_name = screen.textinput(title="Player Name",
                                            prompt="Enter your name to have it registered in rankings : ")

        scoreboard=Scoreboard()

        screen.listen()

        def start_game() :
            screen.resetscreen()

            data_manager=DataManager()
            food=Food()
            snake=Snake()
            scoreboard.write_score()

            screen.onkey(snake.up,"Up")
            screen.onkey(snake.down,"Down")
            screen.onkey(snake.left,"Left")
            screen.onkey(snake.right,"Right")

            # def without_walls():
            #     x_cor = snake.head.xcor()
            #     y_cor = snake.head.ycor()
            #     if x_cor > 295 or x_cor < -295:
            #         snake.head.goto(-x_cor, y_cor)
            #     elif y_cor > 295 or y_cor < -295:
            #         snake.head.goto(x_cor, -y_cor)

            is_game_on=True
            while is_game_on :
                screen.update()
                time.sleep(0.15)
                snake.move()
                # Collision With Food
                if snake.head.distance(food) < 15 :
                    scoreboard.increase_score()
                    scoreboard.write_score()
                    snake.extend()
                    food.refresh_food()
                
                # Collision With Wall
                if snake.head.xcor() > 290 or snake.head.xcor() < -290 or \
                snake.head.ycor() > 290 or snake.head.ycor() < -290 :
                    is_game_on=False
                    data_manager.update_data(player_name=player_name, score=scoreboard.score)
                    scoreboard.game_over()
                
                # Collision With Tail
                for seg in snake.segment[1:] :
                    if snake.head.distance(seg.position()) < 10 :
                        is_game_on=False
                        data_manager.update_data(player_name=player_name, score=scoreboard.score)
                        scoreboard.game_over()


        screen.onkey(start_game,"space")
        t.TurtleScreen._RUNNING = True
        screen.mainloop()
