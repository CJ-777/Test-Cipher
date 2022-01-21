import random

wordlist=['hello', 'world', 'stars', 'class', 'night']

def hangman():
    global wordlist
    # word = random.choice(wordlist)
    word='hello'
    guessed=[]
    wrongGuess=[]
    numOfGuesses=3
    win=False
    while numOfGuesses>0 and win==False:
        for letter in word:
            if letter in guessed:
                print(letter, end=' ')
            else:
                print("_",end=" ")
        
        l=input("Guess letter : ")
        l=l[0]
        if l in word:
            if l in guessed:
                print("Alredy guessed")
            else:
                guessed.append(l)
                print("Correct guess!")
        else:
            if l in wrongGuess:
                print("Alredy guessed")
            else:
                wrongGuess.append(l)
                print("Wrong guess!")
                numOfGuesses -= 1
                print(numOfGuesses," turns remaining.")
        flag=0
        for letter in word:
            if letter not in guessed:
                flag=1
        if flag==0:
            win=True

    if win==True:
        print("You Win")
        print("Word was : ", word)
    else:
        print("Out of Guesses")
    

hangman()