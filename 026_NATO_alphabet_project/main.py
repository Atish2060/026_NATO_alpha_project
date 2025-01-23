import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index,row) in nato_dataframe.iterrows()}
play = "T"
def generate_alpha():
    global user_ans_list
    global play
    while play == "T":
        user_input = input("PLease enter a word:\n").upper()
        user_input_list = list(user_input)
        try:
            user_ans_list = [nato_dictionary[letter] for letter in user_input_list]
        except KeyError:
            print("Please only enter the alphabets")
            generate_alpha()
        else:
            print(f"The nato phonetic alphabet is {user_ans_list}.")
            play = input("Press t if you wanna continue else press f to discontinue the play: ").upper()


generate_alpha()