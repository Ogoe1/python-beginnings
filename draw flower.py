import turtle
c = 0
def draw_square():
    c = 0
    window = turtle.Screen()


    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red", "black")
    brad.speed(10)

    brad.right(90)
    brad.forward(300)
    brad.right(180)
    brad.forward(300)
    for x in range(0,110):
        for x in range(0,2):
            brad.forward(100)
            brad.right(30)
            brad.forward(100)
            brad.right(150)
        brad.right(3)


        
    window.exitonclick()

draw_square()
