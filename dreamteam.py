#def spisok()
#spisok = lambda: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#for i in spisok:
    #if 15 % i == 0:
        #print(i)




#def age():
    #age1 = int(input('Введите возраст собаки: '))
    #s_y = age1 - 2
    #f_y = age1 - s_y
    #final = s_y * 4 + f_y * 10.5
    #print(final)
#age()

#def year():
    #ir = int(input('Введите год: '))
    #if ir % 4 == 0 or ir % 400 == 0 and ir % 100 != 0:
        #print('YES!')
    #else:
        #print('NO!')
#year()

#Task 2

#Это делала сама
def is_palindrome():
    palindrome = (input('Enter: '))
    if palindrome [::-1] == palindrome:
        print(True)
    else:
        print(False)
#is_palindrome()

#Этот нашла в интернете

def pn():
    n=int(input("Enter number:"))
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print(True)
    else:
        print(False)
#pn()


# Task 7

def num():
    n = int(input('Введите число: '))
    if n >= -1 and n <= 17:
        print('Принадлежит!')
    else:
        print('Не принадлежит!')
#num()

def three():
    f = int(input('Введите верх треугольника: '))
    s = int(input('Введите правый бок: '))
    t = int(input('Введите левый бок: '))
    if f != s and f != t and s != t:
        print('Треугольник разносторонний')
    elif f  ==s and f == t and s == t:
        print('Треугольник равносторонний')
    elif f == s and f != t and s != t:
        print('Треугольник равнобедренный')
    elif f != s and f == t and s != t:
        print('Треугольник равнобедренный')
    elif f != s and f != t and s == t:
        print('Треугольник равнобедренный')
#three()

#print(sum(map(int, list(input()))))

n = (int, list(input()))
print (n)# dreamteamLC
