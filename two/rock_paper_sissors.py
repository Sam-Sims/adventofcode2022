
def main():
    scores_shape = {"X" : 1, "Y" : 2, "Z" : 3}
    scores_outcome = {"loss" : 0, "tie" : 3, "win" : 6}

    # key = opponent plays, value = List of what you must play to lose (Index 0), tie (index 1) or win (Index 2)
    win_map = {"A" : ["Z", "X", "Y"], "B" : ["X", "Y", "Z"], "C" : ["Y", "Z", "X"]}

    with open('input.txt') as f:
        score = 0
        score2 = 0
        for line in f:
            game = line.strip().split(' ')
            
            opponent = game[0]
            you = game[1]
            print(f"Opponent plays {opponent}, you play {you}")

            score = score + scores_shape.get(you)

            if win_map.get(opponent)[2] == you:
                print("You win")
                score = score + scores_outcome.get("win")
            elif win_map.get(opponent)[0] == you:
                print("You lose")
                score = score + scores_outcome.get("loss")
            else:
                print("Tie!")
                score = score + scores_outcome.get("tie")

            # Second Strategy
            if you == "X":
                # Lookup what you need to play based on if you need to win, lose or tie
                to_play = win_map.get(opponent)[0]
                print(f"You need to play {to_play} to lose this game!")
                score2 = score2 + scores_outcome.get("loss") + scores_shape.get(to_play)
            elif you == "Y":
                to_play = win_map.get(opponent)[1]
                print(f"You need to play {to_play} to tie this game!")
                score2 = score2 + scores_outcome.get("tie") + scores_shape.get(to_play)
            elif you == "Z":
                to_play = win_map.get(opponent)[2]
                print(f"You need to play {to_play} to win this game!")
                score2 = score2 + scores_outcome.get("win") + scores_shape.get(to_play)

            print(f"Your final score using the 1st strategy is {score}")
            print(f"Your final score using the 2nd strategy is {score2}")






if __name__ == "__main__":
    main()