import turtle
import os
import pandas as pd

#Get the directory where the script is located
script_dir = os.path.dirname(__file__)

#Build the full path to the CSV file
image = os.path.join(script_dir, "blank_states_img.gif")
file = os.path.join(script_dir, "50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
guessed_states = []
state_df = pd.read_csv(file)
state_list = state_df["state"].to_list()


def write_states():
    data_dict = {"state": []}
    for states in state_list:
        if  states not in guessed_states:
            data_dict["state"].append(states)
            push_df = pd.DataFrame(data_dict)
            push_df.to_csv(script_dir+"/states_to_learn.csv")

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another states name?").title()
    if answer_state == "Exit":
        write_states()
        break
    # for state in state_df["state"]:
    #     if state == answer_state:
    #         move_state(state)
    # This is a better way use "if XX in XX" for the list
    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Speichere die Zeile mit dem Begriff in einer Variable
        state_data = state_df[state_df["state"] == answer_state].squeeze() #klappt super wie Dictionary
        # Überprüfe, ob state_data eine Zeile enthält
        if not state_data.empty:
            # Verwende die Spaltennamen "x" und "y" und extrahiere den Wert
            # Die Funktion "values baut ein Numpy Array, welches immer bei 0 beginnt."
            # x_cord = state_data["x"].values[0]
            # y_cord = state_data["y"].values[0]

            # Nutze .at[] für direkten Zugriff auf den Wert
            # x_cord = state_data.at[state_data.index[0], "x"]
            # y_cord = state_data.at[state_data.index[0], "y"]

            # Mittels squeeze kann ich sofort auf die Werte zugreifen
            x_cord = state_data["x"]  #.item() klappt super ohne die squeeze funktion
            y_cord = state_data["y"]

            t.goto(x_cord, y_cord)
            t.write(f"{answer_state}", False, align="center", font=("Arial", 12, "normal"))
        else:
            print(f"Kein Eintrag für {answer_state} gefunden.")

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()


#screen.exitonclick()