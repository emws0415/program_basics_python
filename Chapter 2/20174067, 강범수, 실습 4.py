#컴퓨터공학과, 20174067, 강범수
print("컴퓨터공학과, 20174067, 강범수")

import urllib.request

price = 99.99

while price > 4.74 :
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.html")
    text = page.read().decode("utf8")
    
    where = text.find(">$")
    startOfPrice = where + 2
    endOfPrice = startOfPrice + 4
    
    price = float(text[startOfPrice:endOfPrice])

print(price)
