import random

x = int(input("Pick a number (inclusively between 1 and 1000) that the computer will try to guess: "))
low = 0
high = 1001
feedback = ""
flag = False
while(feedback != "C"):
    if low+1 >= high:
        print(f"The number should be {Cguess} based on the answers provided.")
        flag = True
        break
    Cguess = random.randint(low+1, high-1)
    print(f"Is {Cguess} too high(H), too low(L), or correct(C)?")
    feedback = input()
    if(feedback == "H"):
        high = Cguess
    elif feedback == "L":
        low = Cguess
    else:
        while(feedback != "H" and feedback != "L" and feedback != "C"):
            print(f"This answer doesn't help me.. Is {Cguess} too high(H), too low(L), or correct(C)?")
            feedback = input()
            if(feedback == "H"):
                high = Cguess
            elif feedback == "L":
                low = Cguess
if(flag == False):
    print("I guessed it!")
