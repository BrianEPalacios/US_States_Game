import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# add new shape to turtle to create background
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# get dataframe
df = pd.read_csv("50_states.csv", index_col=False)
# create a list of states
states = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Returns state mini Dataframe for example Texas x , y
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




