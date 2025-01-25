import random
print(r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
""")
print("welcome to the number guessing game")
print("I'm thinking of a number between 1 to 100 :)")
num = random.randint(1,100)
lives = input("choose your level? easy or hard : ").lower()
if lives == "easy":
    lives = 10
if lives == "hard":
    lives = 5
found = False
while lives>0:
    print(f"you have {lives} attempts remaining")
    choose = int(input("choose a number : "))
    if choose>num:
        print("Too High ")
    if choose<num:
        print("Too Low")
    if choose==num:
        print(f"you got it the answer was {num} yay!!!! ")
        found = True
        break
    lives-=1
if not found:
    print(f"You have run out of guesses, click run to run again :(")


