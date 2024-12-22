from turtle import Turtle, turtles

class Snake:
    def __init__(self):
        self.turtules=[]
        self.position=[(-40,0),(-20,0),(0,0)]
        self.creat_snake()
        self.head=self.turtules[-1]
        self.dirc=4

    def creat_snake(self):
        for i in range(len(self.position)):
            new_trtule=Turtle("square")
            new_trtule.color("white")
            new_trtule.penup()
            new_trtule.goto(self.position[i])
            self.turtules.append(new_trtule)
    def move(self):
        for i in range(len(self.turtules)-1):
            self.turtules[i].goto(self.turtules[i+1].pos())
        self.head.forward(20)

    def extend(self):
        new_segment =Turtle("square")   
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtules[0].pos())
        self.turtules.insert(0,new_segment )
        
    def up(self):   
        
        if self.dirc!=2:
         self.head.setheading(90)
         self.dirc=1
    def down(self):
        
        if self.dirc!=1:
         self.head.setheading(270)
         self.dirc=2
    def left(self):
        
        if self.dirc!=4:
         self.head.setheading(180)
         self.dirc=3
    def right(self):
        
        if self.dirc!=3:
         self.head.setheading(0)
         self.dirc=4
        
