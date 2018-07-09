import random


def get_word():
    words = ["surya","ansh","mishti","pooja"]
    return random.choice(words).upper()


def check(word, guesses, guess):
    status = ''
    matches = 0

    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'
        if letter == guess:
            matches += 1
        if matches > 1:
            print("yes! the word have contains", matches, '"' + guess + '"' + 's')
        elif matches == 1:
            print("yes! the word contain the letter '" + guess + '"')
        else:
            print("sorry. THE word does not belongs to here'" + guess)

    return status


def main():
    word = get_word()
    # print(word)
    guesses = []
    guessed = False
    print('the word contains',len(word),'letters.')
    while not guessed:
        text = 'please enter one letter or a {}-letter word '.format(len(word))
        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print("you already guessed'" + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guesses = True
            else:
                print('sorry, incorrect word')
        elif len(guess) == 1:
            guesses.append(guess)
            result =  check(word,guesses,guess)
            if result == word:
                guessed = True
            else:
                print(result)
        else:
            print('invalid entry')

    print("yes, the word id", word + "! you got it in", len(guesses), "tries")


main()
