import random


# MAIN FUNCTION FOR THE GAME
def game(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False

# Computer's turn to choose rnadom number between 1 and 3

print("Computers turn : ROCK(r), PAPER(p), SCISSORS(s)????")
randNO=random.randint(1,3)

if randNO == 1:
    comp='r'
elif randNO == 2:
    comp='p'
elif randNO == 3:
    comp='s'

# User's turn to choose between r,p and s

you=input("Your Turn : ROCK(r), PAPER(p), SCISSORS(s)????  : ")
a=game(comp,you)

print(f"Computer chose : {comp}")
print(f"You chose : {you}")

if a==None:
    print("Its a TIE !")
elif a:
    print(" !!! You Win !!!")
else:
    print("%% You Lose %%")

    # ****************THANK YOU*****************