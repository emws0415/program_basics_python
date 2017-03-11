#컴퓨터공학과, 20174067, 강범수
print("컴퓨터공학과, 20174067, 강범수")

print("Welcome!")

guess = 0

while guess != 5 :
    guess = int(input("Guess the number: "))

    if guess == 5 :
        print("You win!")
    else :
        if guess > 5 :
            print("Too high")
        else :
            print("Too low")

print("Game over!")
