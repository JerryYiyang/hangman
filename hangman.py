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
    del(w[-1])
#checking if choice is in word
    check(w)
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


def check(word):
    check = False
    for i in range(len(w)):
        if choice == w[i]:
            index.append(i)
            check = True
    if check == False:
        print("Sorry, this letter is not in the word.")




if __name__ == '__main__':
    main()
