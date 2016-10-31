import input_output


def launch_input_output_menu():
    print("I/O Section - Enter the exercise number you want to run")
    selection = 0

    while selection != 7:
        print("exercise #1")
        print("exercise #2")
        print("exercise #3")
        print("exercise #4")
        print("exercise #5")
        print("exercise #6")
        print("exit #7")

        selection = int(input("Insert Selection = "))

        if selection == 1:
            print("Extract users form a file")
            for key, value in sorted(input_output.extracted_users.items()):
                print('{0}  {1}'.format(key, value))
        elif selection == 2:
            print("Apply word count on a file")
            file_info = input_output.wc('passwd')
            print("{0} characters {1} words {2} lines and {3} "
                  "unique words in file".format(file_info[0], file_info[1],
                                                file_info[2], file_info[3]))
        elif selection == 3:
            print("Output users to a file")
            file_users = input_output.extract_users('passwd')
            input_output.output_users_to_file(file_users, 'output.csv')
        elif selection == 4:
            print("Read text file")
            print(input_output.read_text("text.txt"))
        elif selection == 5:
            some_words = input_output.read_text("text.txt")
            words_statistics = input_output.word_count(some_words)
            print(words_statistics)
        elif selection == 6:
            some_words = input_output.read_text("text.txt")
            words_statistics = input_output.word_count(some_words)
            word = input_output.word_with_max_occurence(words_statistics)
            print("Word with most occurences = " + word)
        elif selection == 7:
            print("exit")

launch_input_output_menu()
