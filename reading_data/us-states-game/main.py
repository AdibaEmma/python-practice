import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

all_states = states_data.state.to_list()
lower_cased_states = [x.lower() for x in all_states]

total_guessed_right = 0
total_states = len(all_states)
while total_guessed_right < total_states:
    answer_state = screen.textinput(title=f"{total_guessed_right}/{total_states} States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state.lower() in lower_cased_states:
        state = states_data[states_data.state == answer_state]
        coordinates = (int(state.x), int(state.y))
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(coordinates)
        new_turtle.write(answer_state.title())
        total_guessed_right += 1


turtle.mainloop()

