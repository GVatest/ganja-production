import os
import json
import zipfile


class FileNotFoundError(Exception):
    pass


def check_files(dirpath, flag=0):
    try:
        if flag == 1:
            raise FileNotFoundError
    except FileNotFoundError:
        from app.files_to_json_db import save_squeeze_files
        save_squeeze_files(dirpath)
    current_data = {}
    with open('app/' + dirpath.split('/')[1] + '/' + 'files.json') as f:
        data = json.load(f)
        try:
            for currentdir, dirs, files in os.walk(dirpath):
                if currentdir == dirpath:
                    for i in dirs:
                        if i in data.keys():
                            current_data[i] = {}
                        else:
                            raise FileNotFoundError
                dir_keyd = currentdir.split('/')[-2]
                dir_keyf = currentdir.split('/')[-1]
                if dir_keyf in current_data.keys():
                    for i in dirs:
                        if i in data[dir_keyf].keys():
                            current_data[dir_keyf][i] = []
                        else:
                            raise FileNotFoundError
                if files and dir_keyd in current_data.keys():
                    if dir_keyf in current_data[dir_keyd].keys():
                        for i in files:
                            if i[-3:] == 'zip':
                                with zipfile.ZipFile(currentdir + '/' + i, 'r') as z:
                                    z.extractall(currentdir)
                                    continue
                            if i in data[dir_keyd][dir_keyf]:
                                current_data[dir_keyd][dir_keyf].append(i)
                            else:
                                raise FileNotFoundError
                        for i in data[dir_keyd][dir_keyf]:
                            if i not in files:
                                raise FileNotFoundError
                if files and dir_keyd == currentdir.split('/')[2] and dir_keyf != 'previews_videos':
                    current_data[dir_keyf] = []
                    for i in files:
                        if i[-3:] == 'zip':
                            with zipfile.ZipFile(currentdir + '/' + i, 'r') as z:
                                z.extractall(currentdir)
                                continue
                        if i in data[dir_keyf]:
                            current_data[dir_keyf].append(i)
                        else:
                            raise FileNotFoundError
                    for i in data[dir_keyf]:
                        if i not in files:
                            raise FileNotFoundError
        except FileNotFoundError:
            from app.files_to_json_db import save_squeeze_files
            save_squeeze_files(dirpath)
