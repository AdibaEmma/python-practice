import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

guessed_states = []
total_states = len(all_states)
while len(guessed_states) < total_states:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_states} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state = states_data[states_data.state == answer_state]
        coordinates = (int(state.x), int(state.y))
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(coordinates)
        new_turtle.write(answer_state.title())


turtle.mainloop()

