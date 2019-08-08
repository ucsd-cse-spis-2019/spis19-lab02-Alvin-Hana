def word_guessing_game(word):
    counter = 1
    win = len(word)
    while counter <= 7:
        check_in_word = False
        guess = input("Guess a letter: ")
        for letter in word:
            if guess == letter:
                check_in_word = True
                print ("That is in index " + str(word.index(letter)) + " of the word")
                win -= 1
        if check_in_word == False:
            counter += 1
            print ("That letter is not in the word! :(")
        print (win)

        if win == 0:
            print ("YOU WIN!!! The word was " + word + "! :)")
        if counter == 7:
            print ("You lose mofo!")
            return
            
word_guessing_game("curling")
            
