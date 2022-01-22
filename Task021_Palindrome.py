# 21. Программа проверяет пятизначное число на палиндромом.


def IsPalindrome(value):
    original = value
    inverted = 0
    while original != 0:
        inverted = inverted * 10 + (original % 10)
        original //= 10
    return value == inverted


print('Введите число')
num = int(input())
print(IsPalindrome(num))
