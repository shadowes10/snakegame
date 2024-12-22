from snake import Snake
from turtle import Screen
import time
from food import Food
from scorbord import Score




window=Screen()
window.setup(800,800)
window.bgcolor("black")
window.tracer(0)



snake=Snake()
food=Food()
score=Score()

game_on=True
while game_on:
    snake.move()
    window.update()
    time.sleep(.2)
    window.listen()   
    window.onkeypress(snake.up,"Up")
    window.onkeypress(snake.down,"Down")  
    window.onkeypress(snake.left,"Left")
    window.onkeypress(snake.right,"Right")
    if snake.head.distance(food)<15:
        food.appear()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()> 370 or snake.head.xcor()< -370  or snake.head.ycor()> 370 or snake.head.ycor()< -370:
        game_on= False
        score.game_over()
    
    for x in snake.turtules[:-1]:
        if snake.head.distance(x)<10:
            game_on=False
            score.game_over()



window.exitonclick()
