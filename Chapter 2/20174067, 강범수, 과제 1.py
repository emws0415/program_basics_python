#컴퓨터공학과, 20174067, 강범수
print("컴퓨터공학과, 20174067, 강범수")

import urllib.request
import time

price = 99.99
desirePrice = float(input("input desired price: "))

while True :
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    
    where = text.find(">$")
    startOfPrice = where + 2
    endOfPrice = startOfPrice + 4

    price = float(text[startOfPrice:endOfPrice])

    if price <= desirePrice :
        priceTime = time.strftime("%H:%M:%S", time.localtime())
        break

    time.sleep(900)

print("time: ", priceTime)
print("price: ", price)
