import os
import json
from app import db
from app.models import File
from PIL import Image
import PIL


def save_squeeze_files(dirpath):
    current_data = {}
    current_files = []
    with open('app/' + dirpath.split('/')[1] + '/' + 'files.json') as f:
        data = json.load(f)
        try:
            for currentdir, dirs, files in os.walk(dirpath):
                if currentdir == dirpath:
                    for i in dirs:
                        if i in data.keys():
                            current_data[i] = {}
                dir_keyd = currentdir.split('/')[-2]
                dir_keyf = currentdir.split('/')[-1]
                if dir_keyf in current_data.keys():
                    for i in dirs:
                        current_data[dir_keyf][i] = []
                if files and dir_keyd in current_data.keys():
                    if dir_keyf in current_data[dir_keyd].keys():
                        for i in files:
                            if i[-3:] == 'zip':
                                pass
                            else:
                                current_files.append([i, '/'.join(currentdir.split('/')[1:]) + '/' + i])
                                if i in data[dir_keyd][dir_keyf]:
                                    current_data[dir_keyd][dir_keyf].append(i)
                                elif dir_keyf != 'previews_videos':
                                    current_data[dir_keyd][dir_keyf].append(i)
                                    im = Image.open(currentdir + '/' + f"{i}")
                                    im.save(currentdir + '/' + i, quality=70)
                                    file = File()
                                    file.name = dir_keyf + '_' + i
                                    file.file_path = '/'.join(currentdir.split('/')[1:]) + '/' + i
                                    db.session.add(file)
                if files and dir_keyd == currentdir.split('/')[2]:
                    current_data[dir_keyf] = []
                    for i in files:
                        if i[-3:] == 'zip':
                            pass
                        else:
                            current_files.append([i, '/'.join(currentdir.split('/')[1:]) + '/' + i])
                            if i in data[dir_keyf]:
                                current_data[dir_keyf].append(i)
                            elif dir_keyf != 'previews_videos':
                                current_data[dir_keyf].append(i)
                                im = Image.open(currentdir + '/' + f"{i}")
                                im.save(currentdir + '/' + i, quality=70)
                                file = File()
                                file.name = dir_keyf + '_' + i
                                file.file_path = '/'.join(currentdir.split('/')[1:]) + '/' + i
                                db.session.add(file)
            db.session.commit()
        except PIL.UnidentifiedImageError:
            db.session.rollback()
            save_squeeze_files(dirpath)
        except RecursionError:
            pass  # log

    with open('app/' + dirpath.split('/')[1] + '/' + 'files.json', 'w') as f:
        json.dump(current_data, f)

    from app.del_files_db import del_files
    del_files(current_files)
