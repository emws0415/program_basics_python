#컴퓨터공학과, 20174067, 강범수
print("컴퓨터공학과, 20174067, 강범수")

evenSum = 0
oddSum = 0

for i in range(1, 101) :
    if i % 2 == 0 :
        evenSum += i
    else :
        oddSum += i

print("짝수: ", evenSum)
print("홀수: ", oddSum)
print("전체 합: ", evenSum + oddSum)
