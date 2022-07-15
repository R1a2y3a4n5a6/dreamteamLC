# Task 1

def sum_range(a,b): 
 
   if b >= a: 
 
       sum = 0 
 
       for i in range(a,b+1): 
 
           sum += i 
 
       return sum 
 
   else: 
 
       return 0 
 
c1,c2 = int(input()), int(input()) 
 
print(sum_range(c1,c2))

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

# Task 3

print(sum(map(int, list(input()))))


# Task 4

a = input()
print(a[a.rfind('.') + 1:] if '.' in a else 'Что-то с файликом не так')


# Task 5

nums = [45, 55, 60, 37, 100, 105, 220] 
result = list(filter(lambda x: not x % 15, nums)) 
print (result)

# Task 6

n = int(input()) 
print('детство' if n <= 13 else 'молодость' if n <= 24 else 'зрелость' if n <= 59 else 'старость')


# Task 7

def num():
    n = int(input('Введите число: '))
    if n >= -1 and n <= 17:
        print('Принадлежит!')
    else:
        print('Не принадлежит!')
#num()


# Task 8

def year():
    ir = int(input('Введите год: '))
    if ir % 4 == 0 or ir % 400 == 0 and ir % 100 != 0:
        print('YES!')
    else:
        print('NO!')
year()


# Task 9

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
three()


# Task 10

def age():
    age1 = int(input('Введите возраст собаки: '))
    s_y = age1 - 2
    f_y = age1 - s_y
    final = s_y * 4 + f_y * 10.5
    print(final)
age()

