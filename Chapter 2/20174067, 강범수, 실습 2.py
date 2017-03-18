#컴퓨터공학과, 20174067, 강범수
print("컴퓨터공학과, 20174067, 강범수")

import urllib.request

page = urllib.request.urlopen("http://cs.sch.ac.kr/prices.py")

text = page.read().decode("utf8")

price = text[172:176]

print(price)
