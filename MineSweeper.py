import random
import copy
def print_table(L):
    for i in range(10):
        if(i == 0):
             print(f"   {i}", end ="")
        else:
            print(f"   {i}", end = "")
    print()
    for i in range(10):
        print(f"{i}", end ="")
        for j in range(10):
           if(j == 9):
                print(f" {L[i][j]} |", end = "")
           elif(j%2 == 0):
                print(f"| {L[i][j]} |", end = "")
           else:
                print(f" {L[i][j]} ", end = "")
        print()

def print_table_user(L_user):
    for i in range(10):
        if(i == 0):
             print(f"   {i}", end ="")
        else:
            print(f"   {i}", end = "")
    print()
    for i in range(10):
        print(f"{i}", end ="")
        for j in range(10):
           if(j == 9):
                if(type(L_user[i][j]) == int):
                    print(f" {L_user[i][j]} |", end ="")
                else:
                    print(f"   |", end = "")
           elif(j%2 == 0):
                if(type(L_user[i][j]) == int):
                    print(f"| {L_user[i][j]} |", end ="")
                else:
                    print(f"|   |", end = "")
           else:
                if(type(L_user[i][j]) == int):
                    print(f" {L_user[i][j]} ", end ="")
                else:
                    print(f"   ", end= "")
        print()

def insertBombs(L):
    for i in range(10):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        
        while(L[x][y] == '*'):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        L[x][y] = '*'

def updateList(L):
    for i in range(len(L)):
        for j in range(len(L)):
            #top left corner
            if(L[i][j] == '*' and i ==0 and j == 0):
                if(L[i][j+1] != '*'):
                    L[i][j+1]+=1
                if(L[i+1][j+1] != '*'):
                    L[i+1][j+1]+=1
                if(L[i+1][j] != '*'):
                    L[i+1][j]+=1

            #top right corner
            elif L[i][j] == '*' and i == 0 and j == 9:
                if L[i][j-1] != '*':
                    L[i][j-1]+=1
                if L[i+1][j-1] != '*':
                    L[i+1][j-1]+=1
                if L[i+1][j] != '*':
                    L[i+1][j]+=1

            #bottom left corner
            elif L[i][j] == '*' and i == 9 and j == 0:
                if L[i-1][j] != '*':
                    L[i-1][j]+=1
                if L[i-1][j+1] != '*':
                    L[i-1][j+1]+=1
                if L[i][j+1] != '*':
                    L[i][j+1]+=1

            #bottom right corner
            elif L[i][j] == '*' and i == 9 and j == 9:
                if L[i][j-1] != '*':
                    L[i][j-1]+=1
                if L[i-1][j-1] != '*':
                    L[i-1][j-1]+=1
                if L[i-1][j] != '*':
                    L[i-1][j]+=1

            #first row
            elif(L[i][j] == '*' and i == 0):
                if L[i][j-1] != '*':
                    L[i][j-1]+=1
                if L[i+1][j-1] != '*':
                    L[i+1][j-1]+=1
                if L[i+1][j] != '*':
                    L[i+1][j]+=1
                if(L[i+1][j+1] != '*'):
                    L[i+1][j+1]+=1
                if(L[i][j+1] != '*'):
                    L[i][j+1]+=1

            #first column
            elif(L[i][j] == '*' and j == 0):
                if L[i-1][j] != '*':
                    L[i-1][j]+=1
                if L[i-1][j+1] != '*':
                    L[i-1][j+1]+=1
                if L[i][j+1] != '*':
                    L[i][j+1]+=1
                if(L[i+1][j+1] != '*'):
                    L[i+1][j+1]+=1
                if(L[i+1][j] != '*'):
                    L[i+1][j]+=1

            #last row
            elif L[i][j] == '*' and i == 9:
                if(L[9][j-1]!='*'):
                    L[9][j-1] +=1
                if(L[9-1][j-1] != '*'):
                    L[9-1][j-1] +=1
                if(L[9-1][j] != '*'):
                    L[9-1][j] +=1
                if(L[9-1][j+1] != '*'):
                    L[9-1][j+1] +=1
                if(L[9][j+1] != '*'):
                    L[9][j+1] +=1
            
            #last column
            elif L[i][j] == '*' and j == 9:
                if(L[i-1][9]!='*'):
                    L[i-1][9] +=1
                if(L[i-1][9-1] != '*'):
                    L[i-1][9-1] +=1
                if(L[i][9-1] != '*'):
                    L[i][9-1] +=1
                if(L[i+1][9-1] != "*"):
                    L[i+1][9-1] +=1
                if(L[i+1][9] != '*'):
                    L[i+1][9] +=1

           #anywhere in the middle
            elif(L[i][j] == '*'):
                if(type(L[i][j-1]) == int):
                    L[i][j-1]+=1
                if(type(L[i][j+1]) == int):
                    L[i][j+1]+=1
                if(type(L[i-1][j]) == int):
                    L[i-1][j]+=1
                if(type(L[i-1][j-1]) == int):
                    L[i-1][j-1]+=1
                if(type(L[i-1][j+1]) == int):
                    L[i-1][j+1]+=1
                if(type(L[i+1][j]) == int):
                    L[i+1][j]+=1
                if(type(L[i+1][j-1]) == int):
                    L[i+1][j-1]+=1
                if(type(L[i+1][j+1]) == int):
                    L[i+1][j+1]+=1

def check_choice(x, y):
    if x == 0 and y == 0:
        flag = 1
    elif x == 0 and y == 9:
        flag = 8
    elif x == 9 and y == 0:
        flag = 9
    elif x == 0:
        flag = 2
    elif y == 0:
        flag = 3
    elif x == 9 and y == 9:
        flag = 4
    elif y == 9:
        flag = 5
    elif x == 9:
        flag = 6
    else:
        flag = 7
    return flag

def update_list_user(L, L_user, flag, x, y):
    a1 = x-1
    a2 = y-1
    b1 = x-1
    b2 = y
    c1 = x-1
    c2 = y+1
    d1 = x
    d2 = y+1
    e1 = x+1
    e2 = y+1
    f1 = x+1
    f2 = y
    g1 = x+1
    g2 = y-1
    h1 = x
    h2 = y-1
    L_temp =[]
    match flag:
        case 1:
            L_temp = ['d', 'e', 'f']
        case 2:
            L_temp = ['d', 'e', 'f', 'g', 'h']
        case 3:
            L_temp = ['b', 'c', 'd', 'e', 'f']
        case 4:
            L_temp = ['a', 'b', 'h']
        case 5:
            L_temp = ['a', 'b', 'f', 'g', 'h']
        case 6:
            L_temp = ['a', 'b', 'c', 'd', 'h']
        case 7:
            L_temp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        case 8:
            L_temp = ['f', 'g', 'h']
        case 9:
            L_temp = ['b', 'c', 'd']
    #print(f"L_temp: {L_temp}")
    if type(L[x][y]) == int:
        if L[x][y] > 0:
            L_user[x][y] = L[x][y]
            return L_user
        else:
            L_user[x][y] = L[x][y]
            for i in range(len(L_temp)):
                if i == len(L_temp)-1:
                    match L_temp[i]:
                        case 'h':
                            flag = check_choice(h1, h2)
                            update_list_user(L, L_user, flag, h1, h2)
                            return L_user
                        case 'd':
                            flag = check_choice(d1, d2)
                            update_list_user(L, L_user, flag, d1, d2)
                            return L_user
                        case 'f':
                            flag = check_choice(f1, f2)
                            update_list_user(L, L_user, flag, f1, f2)
                            return L_user
                else:    
                    if L_temp[i] == 'a':
                        if L_user[a1][a2] == '':
                            flag = check_choice(a1, a2)
                            update_list_user(L, L_user, flag, a1, a2)
                    elif L_temp[i] == 'b':
                        if L_user[b1][b2] == '':
                            flag = check_choice(b1, b2)
                            update_list_user(L, L_user, flag, b1, b2)
                    elif L_temp[i] == 'c':
                        if L_user[c1][c2] == '':
                            flag = check_choice(c1, c2)
                            update_list_user(L, L_user, flag, c1, c2)
                    elif L_temp[i] == 'd':
                        if L_user[d1][d2] == '':
                            flag = check_choice(d1, d2)
                            update_list_user(L, L_user, flag, d1, d2)
                    elif L_temp[i] == 'e':
                        if L_user[e1][e2] == '':
                            flag = check_choice(e1, e2)
                            update_list_user(L, L_user, flag, e1, e2)
                    elif L_temp[i] == 'f':
                        if L_user[f1][f2] == '':
                            flag = check_choice(f1, f2)
                            update_list_user(L, L_user, flag, f1, f2)
                    elif L_temp[i] == 'g':
                        if L_user[g1][g2] == '':
                            flag = check_choice(g1, g2)
                            update_list_user(L, L_user, flag, g1, g2)
                    elif L_temp[i] == 'h':
                        if L_user[h1][h2] == '':
                            flag = check_choice(h1, h2)
                            update_list_user(L, L_user, flag, h1, h2)
            return L_user
    
    elif L[x][y] == '*':
        return L_user
   
    
print("""\nLet's play Mine Sweeper!\n\nThere are 10 buried bombs. 
Your mission is to uncover the mine field (the table below) without triggering any of the bombs.
      \nGood luck!\n""")
L = []
L_user = []
for i in range(10):
    l = [""]*10
    L_user.append(l)

for i in range(10):
    L2 = [0]*10
    L.append(L2)

insertBombs(L)
updateList(L)
print_table_user(L_user)
flag = False
flag1 = False

# print_table_user(L)
while(flag == False):
    flag7= False
    while flag7 == False:
        try:
            s = input("\nPlease choose a row and a column to dig up, respectively(r c): ")
            L1 = s.split(' ')
            L1[0] = int(L1[0])
            L1[1] = int(L1[1])
            while L1[0] > 9 or L1[0] < 0 or L1[1] <0 or L1[1] >9:
                s = input("\nPlease choose a valid row and column from the table(r c): ")
                L1 = s.split(' ')
                L1[0] = int(L1[0])
                L1[1] = int(L1[1])
            flag7 = True
            while L_user[L1[0]][L1[1]] != '':
                s = input("\nPlease choose a valid row and column from the table(r c): ")
                L1 = s.split(' ')
                L1[0] = int(L1[0])
                L1[1] = int(L1[1])
        except ValueError:
            print("Invalid input.")

    flag2 = check_choice(L1[0], L1[1])
        
    L_temp1 = copy.deepcopy(L_user)
    L_user = update_list_user(L, L_user, flag2, L1[0], L1[1])
    
    #print(f"L_temp1 = {L_temp1}")
    #print(f"L_user = {L_user}")
    if(L_user == L_temp1):
        print_table(L)
        print("\nYou dug up a bomb!\nBetter luck next time.")
        flag = True
    else:
       # print(f"L_user: {L_user}")
        print_table_user(L_user)
        count=0
        for i in range(len(L_user)):
            for j in range(len(L_user[i])):
                if type(L_user[i][j]) == int:
                    count+=1
        if count==90:
            flag1 = True
            break
if(flag1 == True):
    print("\nYou win!")

s = input("\nType in anything to terminate the program: ")