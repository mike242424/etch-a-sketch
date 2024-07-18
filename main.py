import turtle as t

my_turtle = t.Turtle()
my_screen = t.Screen()


def move_forward():
    my_turtle.speed(2)
    my_turtle.forward(10)


def move_backward():
    my_turtle.speed(2)
    my_turtle.backward(10)


def turn_left():
    my_turtle.speed(20)
    my_turtle.left(10)


def turn_right():
    my_turtle.speed(20)
    my_turtle.right(10)


def start_over():
    my_turtle.teleport(x=0, y=0)
    my_screen.resetscreen()


my_screen.listen()
my_screen.onkey(fun=move_forward, key='Up')
my_screen.onkey(fun=move_backward, key='Down')
my_screen.onkey(fun=turn_left, key='Left')
my_screen.onkey(fun=turn_right, key='Right')

my_screen.onkey(fun=move_forward, key='w')
my_screen.onkey(fun=move_backward, key='s')
my_screen.onkey(fun=turn_left, key='a')
my_screen.onkey(fun=turn_right, key='d')

my_screen.onkey(fun=start_over, key='c')
my_screen.exitonclick()
