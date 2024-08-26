import random
print("'r' for rock\n'p' for paper\n's' for scissors\n")
u = input("Your choice: ")
c = random.choice(['r', 'p', 's'])
print(f"Computer's choice: {c}")
if (u==c):
    print("draw!")
elif(u == 'r' and c == 'p'):
    print("Paper beats rock. Computer wins!")
elif(u== 'r' and c == 's'):
    print("Rock beats scissors. You win!")

elif (u == 'p' and c == 'r'):
    print("Paper beats rock. You win!")
elif (u == 'p' and c == 's'):
    print("scissors beat paper. Computer wins!")

elif (u == 's' and c == 'r'):
    print("Rock beats scissors. Computer wins!")
elif (u == 's' and c == 'p'):
    print("scissors beat paper. You win!")