import os
# import json

# 1


def extract_users_from_file(file_name):
    fn = os.path.join(os.path.dirname(__file__), file_name)
    users = {}
    with open(fn) as f:
        for line in f:
            row_elements = line.split(":")
            if len(row_elements) > 0 and "#" not in row_elements[0]:
                users[row_elements[0]] = row_elements[2]

    return users


extracted_users = extract_users_from_file("passwd")

# for key, value in sorted(extracted_users.items()):
#     print('{0}  {1}'.format(key, value))

# 2


def wc(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    chars_count = 0
    lines_count = 0
    words_count = 0
    unique_words = []
    with open(file_path) as file:
        for line in file:
            chars_count += len(line)
            lines_count += 1
            row_elements = line.split(" ")
            words_count += len(row_elements)
            for item in row_elements:
                if item not in unique_words:
                    unique_words.append(item)

    return chars_count, words_count, lines_count, len(unique_words)

# file_info = wc('passwd')
# print("{0} characters {1} words {2} lines and {3} unique words in file"
# .format(file_info[0], file_info[1], file_info[2], file_info[3]))

# 3


def extract_users(file_name):
    fn = os.path.join(os.path.dirname(__file__), file_name)
    users = {}
    with open(fn) as file:
        for line in file:
            row_elements = line.split(":")
            if len(row_elements) > 0 and '#' not in row_elements[0]:
                users[row_elements[0]] = row_elements[2]
    return users

file_users = extract_users('passwd')


def output_users_to_file(users, file_name):
    with open(file_name, "a+") as f:
        for key, value in users.items():
            f.write('{0}    {1} \n'.format(key, value))


output_users_to_file(file_users, 'output.csv')

# 4


# def class_scores_file_paths(score_folder='scores'):
#     dir_path = os.path.join(os.path.dirname(__file__), score_folder)
#     classes = []
#     for filename in os.listdir(dir_path):
#         classes.append(dir_path + "/" + filename)
#
#     return classes
#
#
# def process_file(path):
#     # print(path)
#     with open(path, "r") as f:
#         # print(f)
#         # data = json.load(f)
#         # data = json.loads(f.read())
#         # print(type(data))
#         # js = f.read()
#         # print(js)
#
#         # json_string = '{"uuid":"5730e8666ffa02.34177329","error":""}'
#
#         json_data = json.load(f)
#         print(json_data)
#
#
# def score_statistics(score_folder='scores'):
#     for path in class_scores_file_paths():
#         process_file(path)
#
#
# score_statistics('scores')


# 5


def read_text(file_name):
    fn = os.path.join(os.path.dirname(__file__), file_name)
    words = []
    with open(fn) as f:
        for line in f:
            print(line)
            words_on_line = [s.lower() for s in line.split()]
            table = str.maketrans("", "", "!?;.,1234567890'")
            words_on_line = [s.translate(table) for s in words_on_line]
            words += words_on_line

    return words


# print(read_text("text.txt"))


# 5.1


def word_count(words):
    statistics = {}
    for item in words:
        statistics[item] = words.count(item)
    return statistics

some_words = read_text("text.txt")
words_statistics = word_count(some_words)
print(words_statistics)


# 5.2


def word_with_max_occurence(info_dict):
    max_occurence = -1
    popular_word = ""
    for key, value in info_dict.items():
        print("{0} = {1}".format(key, value))
        if max_occurence < value:
            max_occurence = value
            popular_word = key
    return popular_word

word = word_with_max_occurence(words_statistics)
print("Word with most occurences = " + word)
