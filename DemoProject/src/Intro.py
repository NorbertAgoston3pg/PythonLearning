# 1

name = input("Enter your name =")
print(name)

for char in name[::-1]:
    print(char.upper())


# 2

def reverse_number(number):
    reversed_number = 0
    while number > 0:
        last_number = number % 10
        reversed_number = reversed_number * 10 + last_number
        number //= 10

    # print(reversed_number)
    return reversed_number


def is_palindrome(number):
    return reverse_number(number) == number


print(is_palindrome(41314))


# 3

def palindromes_lower_than(number: int):
    for i in range(number):
        o = "{} palindrome: {}".format(i, is_palindrome(i))
        print(o)


palindromes_lower_than(20)
