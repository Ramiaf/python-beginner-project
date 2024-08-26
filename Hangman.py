from words import w
import random

word = random.choice(w)
while("-" in word or ' ' in word):
    word = random.choice(w)
print()
print("Welcome to Hangman!")
print(f"The word is of {len(word)} letters")
print("You initially get 6 chances for your misguesses of the letters. Good luck!")
chances = 6
count = 0
l = input("Guess a letter: ")
while(count != len(word)):
    L = [0] * len(word)
    if(l in word):
        for i in range(len(word)):
            if(word[i] == l):
                L[i] = 1
        print("Yes. This letter is at position(s):", end = " ")
        for i in range(len(L)):
            if(L[i] == 1):
                print(i+1, end = " ")
                count+=1
    else:
        chances -=1
        if chances == 0:
            break
        else:
            if(chances>1):
                print(f"This letter is not found. You have {chances} more chances to try again.", end = "")
            else:
                print(f"This letter is not found. You have {chances} more chance to try again.", end = "")
        
    if(count==len(word)):
        break
    if(chances == 0):
        break
    else:
        l = input("\n\nGuess a letter: ")

if(chances == 0):
    print(f"\nYou have been hanged! The word was: {word}.\nBetter luck next time!")
else:
    g = input("\nYou have found all the letters of the word. What is the word of the hangman?\n")
    while (g != word):
        print("Oops! Try again.")
        g = input()
    print("Yes! Well done.")        
            
        