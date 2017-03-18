#컴퓨터공학과, 20174067, 강범수
print("컴퓨터공학과, 20174067, 강범수")

import urllib.request

month = ''

while month != "exit" :
    print("ㅡㅡㅡㅡㅡCalendarㅡㅡㅡㅡㅡ")

    print("exit: exit")
    print("format: two-digits\n")
    
    month = input("input: ")
    

    page = urllib.request.urlopen("https://homepage.sch.ac.kr/_custom/sch/_common/board/schedule/skin/list/year_list.jsp?yearmonth=201703&board_no=20110224223754285127")
    text = page.read().decode("utf8")

    for i in range(1, 32) :
        if i < 10:
            date = "2017-" + month +"-" + '0' + str(i)
        else :
            date = "2017-" + month +"-" + str(i)
            
        startOfDate = text.find(date)    # if not found the date, returned -1.
        startOfDate = text[startOfDate:].find("\">") + startOfDate + 2
        endOfDate = text[startOfDate:].find("</") + startOfDate
        
        if startOfDate != 0 :
            print(date, ": ", text[startOfDate:endOfDate], "\n")
