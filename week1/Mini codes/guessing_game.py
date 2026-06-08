# 3 guesses else you lost
guess = 9
turn = 0
while turn < 3:
    num = int(input("Guess: "))
    if num == guess:
        print("You win !!")
        print(f"You have guessed correct in {turn+1} turn")
        break
    turn+=1
else:
    print("You Lost!!!")