import random

def print_table(L):
    print(f"\n| {L[0]} | {L[1]} | {L[2]} |\n| {L[3]} | {L[4]} | {L[5]} |\n| {L[6]} | {L[7]} | {L[8]} |")

def checkH(h, choice, user):
    for i in range(len(h)):
        if(choice in h[i]):
            for j in range(len(h[i])):
                if(choice == h[i][j]):
                    h[i][j] = user
                    break
    return h

def checkV(v, choice, user):
    for i in range(len(v)):
        if(choice in v[i]):
            for j in range(len(v[i])):
                if(choice == v[i][j]):
                    v[i][j] = user
                    break
    return v

def checkD(d, choice, user):
    for i in range(len(d)):
        if(choice in d[i]):
            for j in range(len(d[i])):
                if(choice == d[i][j]):
                    d[i][j] = user
                    break
    return d

def counter(list, user):
    max = 0
    for i in range(len(list)):
        count = 0
        for j in range(len(list[i])):
            if(list[i][j] == user):
                count+=1
        if(count>max):
            max = count
    return max

def check_List(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if(type(list[i][j]) == int):
                return list[i][j]

def max(a, b):
    if(a>b):
        return a
    else:
        return b
    
def boolean_check(list):
    for i in range(len(list)):
        if(user1 in list[i]):
            for j in range(len(list[i])):
                if(type(list[i][j]) == int):
                    return True
    return False

L =[]
for i in range(9):
    L.append(i)

print("Let's play Tic Tac Toe!\n")


user1 = input("\nPlayer1 gets to choose whether they are X(X) or O(O): ")
while(user1 != 'X' and user1 != 'O'):
        user1 = input("Invalid choice. Please choose either X(X) or O(O): ")
if(user1 == 'X'):
        user2 = 'O'
else:
        user2 = 'X'
print(f"\nThis makes Player2: {user2}")

flag1 = False
flag2 = False
count = 0

h = []
x = 0
for i in range(3):
        h.append([x, x+1, x+2])
        x+=3

v = []
x = 0
for i in range(3):
        v.append([x, x+3, x+6])
        x+=1

d = []
d.append([0, 4, 8])
d.append([2, 4, 6])

print_table(L)
while(flag2 == False):
        flag11 = False
        while(flag11 == False):
            try:
                choice1 = int(input("\nTurn of Player1. Please choose a number from the table: "))
                while(choice1 not in L):
                    choice1 = int(input("Invalid number. Try again: "))
                flag11 = True
            except ValueError:
                print("The input must be an integer.")
        
        L[choice1] = user1
        count+=1
        
        print_table(L)
        h = checkH(h, choice1, user1)
        v = checkV(v, choice1, user1)
        d = checkD(d, choice1, user1)

        x = counter(h, user1)
        y = counter(v, user1)
        z = counter(d, user1)
        if(x == 3 or y == 3 or z == 3):
            flag1 = True
            break
        if(count == 9):
            
            break

        flag22 = False
        while(flag22 == False):
            try:
                choice2 = int(input("\nTurn of Player2. Please choose a number from the table: "))
            
                while(choice2 not in L):
                    choice2 = int(input("Invalid number. Try again: "))
                flag22 = True
            except ValueError:
                print("The input must be an integer.")
        L[choice2] = user2
        print_table(L)
        count+=1
        h = checkH(h, choice2, user2)
        v = checkV(v, choice2, user2)
        d = checkD(d, choice2, user2)
        
        x = counter(h, user2)
        y = counter(v, user2)
        z = counter(d, user2)
        if(x == 3 or y == 3 or z == 3):
            flag2 = True

if(count == 9 and flag1 != True):
        print("\nIt's a draw!")

if(flag1 == True):
        print("\nPlayer1 wins!")
elif(flag2 == True):
        print("\nPlayer2 wins!")

s = input("\nPress any character to terminate the program: ")
