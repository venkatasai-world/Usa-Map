import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()

gussed_states = []

while len(gussed_states) < 50:
    answer_state = screen.textinput(title=f"{len(gussed_states)}/50 states", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        break

    if answer_state in all_states and answer_state not in gussed_states:
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# Fixing the logic to save missing states
missing_states = [state for state in all_states if state not in gussed_states]
print(missing_states)
# Optional: Save to file
# pd.DataFrame(missing_states).to_csv("states_to_learn.csv")

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
# screen.exitonclick() is not needed since mainloop() handles it
