"""
Write the code which will write excepted data to files below
For example given offices of Google:
1)google_kazakstan.txt
2)google_paris.txt
3)google_uar.txt
4)google_kyrgystan.txt
5)google_san_francisco.txt
6)google_germany.txt
7)google_moscow.txt
8)google_sweden.txt
When the user will say “Hello”
Your code must communicate and give a choice from listed offices. After it
has to receive a complain from user, and write it to file chosen by user.
Hint: Use construction “with open”
"""


user = input()

if user == "Hello":
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/List of countries.txt', 'r') as new:
        content = new.read()
        print(content)

country_complaining = int(input('Please, choose the number of office you are complaining of: ' ))
complain = input('Please, write what are you complaining of: ' )

if country_complaining == 1:
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/1Kazakhstan.txt','a') as new1:
        kaz_complain = new1.write(' ' + complain)
    
elif country_complaining == 2:
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/2Paris.txt', 'a') as new2:
        paris_complain = new2.write(' ' + complain)

elif country_complaining == 3:
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/3UAR.txt', 'a') as new3:
        UAR_complain = new3.write(' ' + complain)

elif country_complaining == 4:
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/4Kyrgyzstan.txt', 'a') as new4:
        KG_complain = new4.write(' ' + complain)

elif country_complaining == 5:
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/5San Francisco.txt', 'a') as new5:
        SF_complain = new5.write(' ' + complain)

elif country_complaining == 6:
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/6Germany.txt', 'a') as new6:
        Germany_complain = new6.write(' ' + complain)

elif country_complaining == 7:
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/7Moscow.txt', 'a') as new7:
        Moscow_complain = new7.write(' ' + complain)

elif country_complaining == 8:
    with open('/Users/maksataitmambetov/Desktop/makers/Tasks/chapter2/task2.17/8Sweden.txt', 'a') as new8:
        Sweden_complain = new8.write(' ' + complain)