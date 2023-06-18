import turtle
def exit_program():
    window.bye()
def close():
    global stopped
    global mess_turtle
    stopped = True
    mess_turtle.goto(-330, 320)
    mess_turtle.write("Press ESC again to exit", align="center", font=("Courier", 12, "bold"))
    window.listen()
    window.onkeypress(exit_program, "Escape")
stopped = False
window = turtle.Screen()
window.tracer(n=2)
window.listen()
window.onkeypress(close, "Escape")
mess_turtle = turtle.Turtle()
mess_turtle.color("red")
mess_turtle.hideturtle()
mess_turtle.penup()
intern_angle_advance = 17
intern_radius = 100
intern = turtle.Turtle()
intern.hideturtle()
intern.setheading(0)
intern.penup()
extern_angle_advance = 1
extern_radius = 350
extern = turtle.Turtle()
extern.hideturtle()
extern.setheading(138)
extern.penup()
while not stopped:
    extern.forward(extern_radius)
    intern.forward(intern_radius)
    intern.pendown()
    intern.goto(extern.pos())
    intern.penup()
    extern.goto(0, 0)
    extern.left(extern_angle_advance)
    intern.goto(0, 0)
    intern.left(intern_angle_advance)
turtle.done()