def check_guess(guess,answer):
    global score
    still_guessing=True
    attempt=0
    while still_guessing and attempt<3:
        if guess.lower()==answer.lower():
            print("Correct Answer")
            score=score+1
            still_guessing=False
        else:
            if attempt<2:
                guess=input("sorry wrong answer,try again")
                attempt=attempt+1
            if attempt==3:
                    print("Correct Answer is",answer)
score=0
print("Guess the Animal name")
guess1=input("Which bear lives at north pole?")
check_guess(guess1,"polar bear")
guess2=input("which is the fastest land animal?")
check_guess(guess2,"cheetah")
guess3=input("which is the largest animal?")
check_guess(guess3,"blue whale")
print("your score is"+str(score))

#colorama importing
import colorama
from colorama import fore,back,style
colorama.init(autoreset=True)

print(For.BLUE+Back.YELLOW+"hi my name is chandru"+For.YELLOW+Back.BLUE+" I am your machin lerning programer")
print(Back.CYAN+"Hi my name is chandanatha")
print(For.RED+Back.GREEN+"hi my name is")

      
