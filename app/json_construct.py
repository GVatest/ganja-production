import os
import json
import copy


def construct(dirpath):
    clear_flag = 0
    with open('app/' + dirpath.split('/')[1] + '/' + 'files.json') as f:
        data = json.load(f)
        current_data = copy.deepcopy(data)
        for currentdir, dirs, files in os.walk(dirpath):
            if currentdir == dirpath:
                for i in dirs:
                    if i not in data.keys():
                        data[i] = {}
                        current_data[i] = {}
                for i in data.keys():
                    if i not in dirs:
                        current_data.pop(i)
                        clear_flag = 1
            dir_keyf = currentdir.split('/')[-1]
            if dir_keyf in data.keys():
                for i in dirs:
                    if i not in data[dir_keyf].keys():
                        data[dir_keyf][i] = []
                        current_data[dir_keyf][i] = []
                if type(data[dir_keyf]) == dict:
                    for i in data[dir_keyf].keys():
                        if i not in dirs:
                            current_data[dir_keyf].pop(i)
                            clear_flag = 1

    with open('app/' + dirpath.split('/')[1] + '/' + 'files.json', 'w') as f:
        json.dump(current_data, f)

    from app.check_files import check_files
    check_files(dirpath, clear_flag)
