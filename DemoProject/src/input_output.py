import os
import json
from pprint import pprint

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
            for word in row_elements:
                if word not in unique_words:
                    unique_words.append(word)

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


def class_scores_file_paths(score_folder='scores'):
    dir_path = os.path.join(os.path.dirname(__file__), score_folder)
    classes = []
    for filename in os.listdir(dir_path):
        classes.append(dir_path + "/" + filename)

    return classes


# def process_file(path):
#     print(path)
#     with open(path) as json_data:
        # print(json_data)
        # data = json.load(json_data)
        # print(data)
        # js = json_data.read()
        # print(json.loads('{0}'.format(js)))
        # print(type(json.loads('{0}'.format(js))))


# def score_statistics(score_folder='scores'):
#     for path in class_scores_file_paths():
#         process_file(path)


# score_statistics('scores')
