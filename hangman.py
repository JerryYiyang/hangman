import sys
import random

def main():
    print("Let's play hangman!")
#initial hangman image
    print("  +---+ \n" + "  |   | \n" + "      | \n" +  "      | ")
    print("      | \n" +  "      | \n" + "=========") 
#opens and reads file with words
    f = open(sys.argv[1], 'r')
    words = f.readlines()
    f.close()
#picks random word and prints corresponding 'empty' spaces
    word = random.choice(words)
    word.rstrip('\n')
    spaces = ['._'] * len(word)
    for s in spaces:    
        print(s, end='')
    print("\n")
#getting choices
    tried = []
    w = []
    for char in word:
        w.append(char)
    del(w[-1])
    wrong = 0
    print(w)
    while '._' in spaces:
        choice = get_choice()
#checking if choice is in word
        c = check(w, choice)
#if choice is in word then it replaces the "._" in spaces with the letter
        if c is not False:
            print(c)
            for x in c:
                spaces[x] = choice
            for s in spaces:
                print(s, end='')
            print("\n")
#if it's not in the word then a part of the hangman is added
        elif c is False:
            print("Sorry, your choice is not in the word.")
            wrong += 1
            print_hangman(wrong)


def get_choice():
    choice = input('What letter would you like to try? ')
    if choice.isalpha() is False:
        print('You did not choose a letter, please choose again.')
        return get_choice()
    else:
        return choice.lower()


def check(word, choice):
    check = False
    index = []
    for i in range(len(word)):
        if choice == word[i]:
            index.append(i)
        check = True
        return index
    if check == False:
        return False


def print_hangman(w):
    if w == 1:
        print("  +---+ \n" + "  |   | \n" + "  o   | \n" +  "      | ")
        print("      | \n" + "      | \n" + "=========")
    if w == 2:
        print("  +---+ \n" + "  |   | \n" + "  o   | \n" +  "  |   | ")
        print("      | \n" + "      | \n" + "=========")
    if w == 3:
        print("  +---+ \n" + "  |   | \n" + "  o   | \n" +  "  |   | ")
        print(" /|   | \n" + "      | \n" + "=========")
    if w == 4:
        print("  +---+ \n" + "  |   | \n" + "  o   | \n" +  "  |   | ")
        print(" /|\  | \n" + "      | \n" + "=========") 
    if w == 5:
        print("  +---+ \n" + "  |   | \n" + "  o   | \n" +  "  |   | ")
        print(" /|\  | \n" + " /    | \n" + "=========")
    if w == 6:
        print("  +---+ \n" + "  |   | \n" + "  o   | \n" +  "  |   | ")
        print(" /|\  | \n" + " / \  | \n" + "=========")
        print("Oh no! The hangman was hung! You lost :(")
        quit()


if __name__ == '__main__':
    main()
