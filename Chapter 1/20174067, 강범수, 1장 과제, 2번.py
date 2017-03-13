#컴퓨터공학과, 20174067, 강범수
print("컴퓨터공학과, 20174067, 강범수")

from random import randint

while True:
    print("ㅡㅡㅡㅡㅡMENUㅡㅡㅡㅡㅡ")
    print("1. UP & DOWN")
    print("2. Bulls and Cows")
    print("3. Exit")

    choose = int(input("> "))

    # UP & DOWN
    if choose == 1 :
        print("\nㅡㅡㅡUP & DOWN!ㅡㅡㅡ")
        
        value = randint(0, 100)

        while True :
            guess = int(input("input number: "))

            if guess > value :
                print("DOWN")
            elif guess < value :
                print("UP")
            else :
                print("GOOD\n\n")
                break;

    # Bulls and Cows
    elif choose == 2 :
        print("\nㅡㅡㅡBulls and Cowsㅡㅡㅡ")

        computer = [0, 0, 0]
        while True:
            for i in range(0, 3) :  
                computer[i] = randint(0, 9)
                
            if  ( computer[0] != computer[1]
                & computer[0] != computer[2]
                & computer[1] != computer[2]
                ) :
                break

        # HACK: show numbers of computer.
        print(computer[0:3])

        player = [0, 0, 0]
        strike = 0
        ball = 0
        
        while strike != 3 :
            strike = 0
            ball = 0
                
            for i in range(0, 3) :
                player[i] = int(input("input three numbers: "))
                
            for i in range(0, 3) :
                for j in range(0, 3) :
                    if player[i] == computer[j] :
                        if i == j :
                            strike += 1
                            break
                        else :
                            ball += 1
                            break
        
            print(strike, " strike, ", ball, " ball !\n")
        print("GOOD\n\n")

    # Exit
    elif choose == 3 :
        print("\nExit...")
        break
