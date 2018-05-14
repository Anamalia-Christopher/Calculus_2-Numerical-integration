import datetime
start= datetime.datetime.now()
import turtle
import kivy

s = turtle.Screen()
t = turtle.Turtle()
print(s.window_width())
print(s.window_height())


def set_graph_window(a, b):
    s.setup(a, b, 0, 0)


def axis():
    # drawing the y-axis
    t.up()
    t.goto(0, s.window_height()/2.5)
    t.left(90)
    t.stamp()
    t.down()
    t.goto(0, -s.window_height() / 2.5)

    # coming back to (0,0)
    t.up()
    t.goto(0, 0)
    
    # drawing the x-axis
    t.goto(s.window_width()/2.5, 0)
    t.right(90)
    t.stamp()
    t.down()
    t.goto(-s.window_width() / 2.5, 0)

    # reset and come back to origin
    t.up()
    t.goto(0, 0)



    s.exitonclick()


def function_input():
    #     will later change the from input to parameter
    f = input("Function: ")
    variable = input("variable of the function: ")
    print(f)
    return f, variable


def correct_input_form():
    function_to_return = ''
    f = function_input()
    if "^" in f[0]:
        f.replace("^", "**")

    for i in range(len(f[0])):
        try:
            if i > 0 and f[0][i] ==f[1] and isinstance(int(f[0][i-1]), int):
                function_to_return += "*"
        except Exception as e:
            pass
        finally:
            function_to_return += f[0][i]

    print(function_to_return)



correct_input_form()

# x = function_input()
# print(x[0])
stop = datetime.datetime.now()

print(stop-start)
