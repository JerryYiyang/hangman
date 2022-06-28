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
    spaces = ['_.'] * len(word)
    spaces[-1] = '_'
    for s in spaces:    
        print(s, end='')
    print("\n")
#getting choices
    tried = []
    choice = get_choice()
    w = []
    for char in word:
        w.append(char)
    index = []
#checking if choice is in word
    for i in range(w):
        if choice == x:
            index.append(i)
        else:
            print("Sorry, this letter is not in the word.")
    for i in index:
        spaces[i] = choice
    print(spaces)


def get_choice():
    choice = input('What letter would you like to try?' )
    if choice.isalpha is False:
        print('You did not choose a letter, please choose again.')
        return get_choice()
    else:
        return choice.lower()

if __name__ == '__main__':
    main()
