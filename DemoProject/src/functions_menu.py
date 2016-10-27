import functions


def launch_functions_menu():
    print("Functions Section - Enter the exercise number you want to run")
    selection = 0

    while selection != 12:
        print("exercise #1")
        print("exercise #2")
        print("exercise #3")
        print("exercise #4")
        print("exercise #5")
        print("exercise #6")
        print("exercise #7")
        print("exercise #8")
        print("exercise #9")
        print("exercise #10")
        print("exercise #11")
        print("exit #12")

        selection = int(input("Insert Selection = "))

        if selection == 1:
            number = int(input("Enter a number to see if it's prime "))
            print(functions.is_prime(number))
        elif selection == 2:
            number = int(input("Get all prime numbers smaller than "))
            functions.prime_numbers_smaller_than(number)
        elif selection == 3:
            number = int(input("Fibonacci sequence with elements count = "))
            functions.fibonacci_sequence(number)
        elif selection == 4:
            print("my_map function")
            functions.exercise_4()
        elif selection == 5:
            print("my_filter function")
            functions.exercise_5()
        elif selection == 6:
            print("my_reduce function")
            functions.exercise_6()
        elif selection == 7:
            number = int(input("Special Sum of numbers smaller than "))
            print(functions.sum_of_special_numbers_smaller_than(number))
        elif selection == 8:
            print("sort [4, 2, 3, 1] {0}".format(functions.sort([4, 2, 3, 1])))
        elif selection == 9:
            print("Check if 1 in list [1, 4, 5] ")
            print(functions.element_in_list(1, [1, 4, 5]))
        elif selection == 10:
            print("call stateful function")
            print(functions.stateful_func())
            print(functions.stateful_func())
            print(functions.stateful_func())

            print("----- new state -----")

            new_state = functions.State()
            print(functions.stateful_func(new_state))
            print(functions.stateful_func(new_state))

            print("----- old state -----")
            print(functions.stateful_func())
        elif selection == 11:
            print("measure the duration of a function")
            print(functions.my_func())
        elif selection == 12:
            print("Exit")

launch_functions_menu()
