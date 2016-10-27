
from functools import reduce
from functools import wraps
import time

# 1


def is_prime(number):
    p = True
    for element in range(2, number):
        if number % element == 0:
            p = False
            break
    return p

# 2


def prime_numbers_smaller_than(number):
    for element in range(2, number):
        if is_prime(element):
            print("Prime number = {0}".format(element))

# 3


def fibonacci_sequence(number_of_elements):
    current_element = 1
    previous_element = 0
    for _ in range(number_of_elements):
        next_element = current_element + previous_element
        print(current_element)
        previous_element = current_element
        current_element = next_element


def fibonacci(number_of_elements):
    if number_of_elements < 2:
        return number_of_elements
    else:
        result = (fibonacci(number_of_elements-1) +
                  fibonacci(number_of_elements-2))
        return result


# fibonacci_sequence(7)
#
# for i in range(8):
#     print(fibonacci(i))

# 4

numbers = range(1, 11)
# print  numbers


def my_sqare(number):
    return number ** 2


def my_map(func, iterable):
    result = []
    for element in iterable:
        result.append(func(element))

    return result


def exercise_4():
    print(my_map(my_sqare, numbers))


# 5

def is_even(number):
    return number % 2 == 0


def my_filter(func, iterable):
    result = []
    for element in iterable:
        if func(element):
            result.append(element)
    return result


def exercise_5():
    print(my_filter(is_even, numbers))

# 6


def my_sum(a, b):
    return a + b


def my_reduce(func, iterable, initializer):
    for element in iterable:
        initializer = func(initializer, element)
    return initializer


def exercise_6():
    print(my_reduce(my_sum, numbers, 0))


# 7

def sum_of_special_numbers_smaller_than(number):
    special_numbers = map(lambda x: x*x - 1, range(number))
    filtered_numbers = filter(lambda x: x % 3 == 0, special_numbers)
    return reduce(lambda x, y: x + y, filtered_numbers, 0)


# 8

def sort(elements):
    return sorted(elements)

# print(sort([4, 2, 3, 1]))

# 9


def element_in_list(element, elements):
    return element in elements

# print(element_in_list(0, [1, 4, 5]))

# 10
# def get_text(name):
#     return "something {0} something".format(name)
#
# print(get_text("Norbert"))
#
# def p_decorate(func):
#     def func_wrapper(name):
#         return "<p>{0}</p>".format(func(name))
#     return func_wrapper
#
# my_get_text = p_decorate(get_text)
# print(my_get_text("John"))


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@strong_decorate
@p_decorate
def get_text(name):
    return "something {0} something".format(name)

# print(get_text("John"))


def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family

# my_person = Person()
# print(my_person.get_fullname)


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello " + name

# 10


class State:
    def __init__(self):
        pass


def stateful_func(state=State()):
    if hasattr(state, "index"):
        state.index += 1
    else:
        state.index = 0

    return state.index


# 11


def time_duration(func):
    def func_wrapper():
        interval1 = time.time()
        func()
        interval2 = time.time()
        return "Execution time =" + str(interval2-interval1) + "\n"
    return func_wrapper


@time_duration
def my_func():
    for i in range(5):
        print(i)
        time.sleep(1)
