def get_random_word():
    return"pizza"

def play_word_games():
    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()

    while playing:
        strikes += 1

        if strikes >= max_strikes:
            playing = False
        
    if strikes >= max_strikes:
        print("Sorry, game over dude.")
    else:
        print("winner winner!")

print ("Start the Game!")
play_word_games()
print("End the Game")
