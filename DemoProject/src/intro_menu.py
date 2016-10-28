import intro


def launch_intro_menu():
    print("Intro Section - Enter the exercise number you want to run")
    selection = 0

    while selection != 4:
        print("exercise #1")
        print("exercise #2")
        print("exercise #3")
        print("exit #4")

        selection = int(input("Insert Selection = "))

        if selection == 1:
            intro.reverse_name()
        elif selection == 2:
            number = int(input("Insert Number to reverse = "))
            print("reversed number = {0}".format(intro.reverse_number(number)))
        elif selection == 3:
            number = int(input("Search palindromes lower than "))
            intro.palindromes_lower_than(number)
        elif selection == 4:
            print("exit")

launch_intro_menu()
