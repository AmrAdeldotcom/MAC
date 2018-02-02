import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    count = 0
    while count < 4:
        brad.speed(2)
        brad.forward(100)
        brad.right(90)
        count += 1
    '''
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    '''
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    tom = turtle.Turtle()
    tom.backward(100)
    tom.left(120)
    tom.backward(100)
    tom.left(120)
    tom.backward(100)

    window.exitonclick()
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    count = 0
    while count < 4:
        brad.speed(0)
        brad.forward(100)
        brad.right(90)
        count += 1
    #window.exitonclick()
    return brad
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")
    flower = turtle.Turtle()
    flower.color("white")
    i=0
    while i < 180:
        flower.right(i)
        count = 0
        while count < 4:
            flower.speed(0)
            flower.forward(100)
            flower.right(90)
            count += 1
        i += 1
    window.exitonclick()
#draw_square()
#draw()
draw_flower()
