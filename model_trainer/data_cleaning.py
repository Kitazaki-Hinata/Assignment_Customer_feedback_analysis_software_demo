'''data cleaning class'''

import os

def change_one_to_two(folder_path):
    '''change label 1 to 2, as sample only has two sentiment'''
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            with open(file_path, 'w', encoding='utf-8') as file:
                for line in lines:
                    line = line.rstrip()
                    if line.endswith('1'):
                        file.write(line[:-1] + '2\n')
                    elif line.endswith('0'):
                        file.write(line + '\n')
                    else:
                        file.write(line + '\n')


if __name__ == '__main__':
    # change folder Sentiment Labelled Sentences Data Set
    current_file_path = os.path.abspath(os.path.dirname(__file__))
    dataset_path = os.path.join(current_file_path, "..", 'dataset', "Sentiment Labelled Sentences Data Set")
    change_one_to_two(dataset_path)