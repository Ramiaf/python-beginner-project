import random
import time

def print_table(L):
    print(f"\n| {L[0]} | {L[1]} | {L[2]} |\n| {L[3]} | {L[4]} | {L[5]} |\n| {L[6]} | {L[7]} | {L[8]} |")

def updateH(h, choice, user):
    for i in range(len(h)):
        if(choice in h[i]):
            for j in range(len(h[i])):
                if(choice == h[i][j]):
                    h[i][j] = user
                    break
    return h

def updateV(v, choice, user):
    for i in range(len(v)):
        if(choice in v[i]):
            for j in range(len(v[i])):
                if(choice == v[i][j]):
                    v[i][j] = user
                    break
    return v

def updateD(d, choice, user):
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

def check_List(list, user1):
    x = 0
    y = -1
    if(len(list) == 2):
        for i in range(len(list)):
            if(user1 in list[i]):
                count = 0
                for j in range(len(list[i])):
                    if(list[i][j]) == user1:
                        count+=1
                if(count==2):
                    x = i
                    break
        for j in range(len(list[x])):
            if(type(list[x][j]) == int):
                y = list[x][j]
        if(y == -1):
            if(x == 0):
                count = 0
                for i in range(len(list[x+1])):
                     if(list[x+1][i] == user1):
                          count+=1
                if(count == 2):
                    for j in range(len(list[x+1])):
                        if(type(list[x+1][j]) ==int):
                            return list[x+1][j]
        else:
            return y

    else:
        for i in range(len(list)):
            if(user1 in list[i]):
                count = 0
                for j in range(len(list[i])):
                    if(list[i][j]) == user1:
                        count+=1
                if(count==2):
                    x = i
                    break
        for j in range(len(list[x])):
            if(type(list[x][j]) == int):
                return list[x][j]

def max(a, b):
    if(a>=b):
        return a
    else:
        return b
    
def boolean_check(list, user1):
    x = 0
    flag = False
    if(len(list) == 2):
         for i in range(len(list)):
              if(user1 in list[i]):
                count = 0
                for j in range(len(list[i])):
                   if(list[i][j] == user1):
                        count+=1
                if(count == 2):
                     x = i
                     break
         #print("This is x: " + str(x))
         for j in range(len(list[x])):
              if(type(list[x][j]) == int):
                    flag = True
         if(flag == True):
            return True
         else:
              if(x == 0):
                count = 0
                for i in range(len(list[x+1])):
                     if(list[x+1][i] == user1):
                          count+=1
                if(count == 2):
                    for j in range(len(list[x+1])):
                        if(type(list[x+1][j]) ==int):
                            return True
              return False
    else:
        for i in range(len(list)):
            if(user1 in list[i]):
                count = 0
                for j in range(len(list[i])):
                    if(list[i][j]) == user1:
                        count+=1
                if(count==2):
                    x = i
                    break
        for j in range(len(list[x])):
            if(type(list[x][j]) == int):
                return True
        return False

def choice(list, user2, max):
    x = 0
    for i in range(len(list)):
        count=0
        if(user2 in list[i]):
            for j in range(len(list[i])):
                if(list[i][j] == user2):
                        count+=1
            if(count == max):
                 x = i
                 break
    for j in range(len(list[x])):
         if(type(list[x][j]) == int):
              return list[x][j]


print("\nLet's play Tic Tac Toe!\n")

L =[]
for i in range(9):
    L.append(i)

user1 = input("\nPlease choose whether you are X(X) or O(O): ")
while(user1 != 'X' and user1 != 'O'):
    user1 = input("Invalid choice. Please choose either X(X) or O(O): ")
if(user1 == 'X'):
    user2 = 'O'
else:
    user2 = 'X'

print(f"\nThis makes the computer: {user2}")

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
count2 = 0
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
    h = updateH(h, choice1, user1)
    v = updateV(v, choice1, user1)
    d = updateD(d, choice1, user1)

    x = counter(h, user1)
    y = counter(v, user1)
    z = counter(d, user1)
    if(x == 3 or y == 3 or z == 3):
        flag1 = True
        break
    if(count == 9):
        break
        
    print("\nNow the computer gets to choose a number.")
    print("\n...")
    time.sleep(1)
    a = counter(h, user2)
    b = counter(v, user2)
    c = counter(d, user2)

    if (x <= 1 and y <= 1 and z <= 1 and count2 == 0):
        choice2 = random.randint(0,8)
        while(L[choice2] == user2 or L[choice2] == user1):
                choice2 = random.randint(0,8)
        #print("Fuck")
        L[choice2] = user2

    elif(x == 2 or y == 2 or z == 2):
        if(a == 2):
            #print("Hello")
            choice2 = choice(h, user2, a)
            #print(f"Choice2 = {choice2}")
            if(choice2 == None):
                # print(f"Bool h: {boolean_check(h, user1)}")
               #  print(f"Bool v: {boolean_check(v, user1)}")
                # print(f"Bool d: {boolean_check(d, user1)}")
                 if(x == 2 and boolean_check(h, user1) == True):
                    choice2 = check_List(h, user1)
                    L[choice2] = user2
                 elif(y == 2 and boolean_check(v, user1) == True):
                    choice2 = check_List(v, user1)
                    L[choice2] = user2
                 elif(z == 2 and boolean_check(d,user1) == True):
                    choice2 = check_List(d, user1)
                    L[choice2] = user2
                 else:
                    choice2 = random.randint(0,8)
                    while(choice2 not in L):
                        choice2 = random.randint(0,8)
                    L[choice2] = user2   
            else:
                L[choice2] = user2
        elif(b == 2):
            #print("Helloo")
            choice2 = choice(v, user2, b)
            #print(f"Choice2 = {choice2}")
            if(choice2 == None):
                 #print(f"Bool h: {boolean_check(h, user1)}")
                 #print(f"Bool v: {boolean_check(v, user1)}")
                # print(f"Bool d: {boolean_check(d, user1)}")
                 if(x == 2 and boolean_check(h, user1) == True):
                    choice2 = check_List(h, user1)
                    L[choice2] = user2
                 elif(y ==2 and boolean_check(v, user1) == True):
                    choice2 = check_List(v, user1)
                    L[choice2] = user2
                 elif(z ==2 and boolean_check(d,user1) == True):
                    choice2 = check_List(d, user1)
                    L[choice2] = user2
                 else:
                    choice2 = random.randint(0,8)
                    while(choice2 not in L):
                        choice2 = random.randint(0,8)
                    L[choice2] = user2
            else:
                L[choice2] = user2
        elif(c == 2):
             #print("Hell")
             choice2 = choice(d, user2, c)
             if(choice2 == None):
                # print(f"Bool h: {boolean_check(h, user1)}")
                # print(f"Bool v: {boolean_check(v, user1)}")
                 #print(f"Bool d: {boolean_check(d, user1)}")
                 if(x ==2 and boolean_check(h, user1) == True):
                    choice2 = check_List(h, user1)
                    L[choice2] = user2
                 elif(y ==2 and boolean_check(v, user1) == True):
                    choice2 = check_List(v, user1)
                    L[choice2] = user2
                 elif(z ==2 and boolean_check(d,user1) == True):
                    choice2 = check_List(d, user1)
                    L[choice2] = user2
                 else:
                    choice2 = random.randint(0,8)
                    while(choice2 not in L):
                        choice2 = random.randint(0,8)
                    L[choice2] = user2
             else:
                L[choice2] = user2

       
        elif(x == 2 and (boolean_check(h, user1) == True)):
                    choice2 = check_List(h, user1)
                    #print("Hello 1")
                    L[choice2] = user2
        elif(y == 2 and boolean_check(v, user1) == True):
                   # print("Hello 2")
                    choice2 = check_List(v, user1)
                    L[choice2] = user2
        elif(z == 2 and boolean_check(d, user1) == True):
                   # print("Hello 3")
                    choice2 = check_List(d, user1)
                    L[choice2] = user2
        else:
           # print(f"bool check d: {boolean_check(d,user1)}")
            #print(a)
            #print(b)
            #print(c)
            f = (a-x)
            g = (b-y)
            a1 = (c-z)

            if(max(f, g) == f and max(f, a1) == f):
                
                choice2 = choice(h, user2, a)
                L[choice2] = user2
            elif(max(f, g) == f and max(f, a1) == a1):
                
                choice2 = choice(d, user2, c)
                L[choice2] = user2
            elif(max(f, g) == g and max(f, a1) == f):
                
                choice2 = choice(v, user2, b)
                L[choice2] = user2
            elif(max(f, g) == g and max(f, a1) == a1):
                
                if(max(g, a1) == g):
                    
                    choice2 = choice(v, user2, b)
                    L[choice2] = user2
                else:
                    
                    choice2 = choice(d, user2, c)
                    L[choice2] = user2

    else:
            #print("Hey you")
            #print(a)
            #print(b)
            #print(c)
            f = abs(a-x)
            g = abs(b-y)
            a1 = abs(c-z)

            if(max(f, g) == f and max(f, a1) == f):
            #    print("Hello a")
                choice2 = choice(h, user2, a)
                L[choice2] = user2
            elif(max(f, g) == f and max(f, a1) == a1):
             #   print("Hello b")
                choice2 = choice(d, user2, c)
                L[choice2] = user2
            elif(max(f, g) == g and max(f, a1) == f):
              #  print("Hello c")
                choice2 = choice(v, user2, b)
                L[choice2] = user2
            elif(max(f, g) == g and max(f, a1) == a1):
               # print("Hello d")
                if(max(g, a1) == g):
                #    print("Hello e")
                    choice2 = choice(v, user2, b)
                    L[choice2] = user2
                else:
                 #   print("hello f")
                    choice2 = choice(d, user2, c)
                    L[choice2] = user2

        
    print(f"\nThe computer chooses: {choice2}")
    h = updateH(h, choice2, user2)
    v = updateV(v, choice2, user2)
    d = updateD(d, choice2, user2)

    x = counter(h, user2)
    y = counter(v, user2)
    z = counter(d, user2)
    count+=1
    count2+=1
    print_table(L)

    if(x == 3 or y ==3 or z == 3):
         flag2 = True

if(count == 9 and flag1 != True):
        print("\nIt's a draw!")

if(flag1 == True):
        print("\nPlayer1 wins!")
elif(flag2 == True):
        print("\nComputer wins!")

s = input("\nType in anything to terminate the program: ")