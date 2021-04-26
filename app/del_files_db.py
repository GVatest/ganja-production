from app.models import File
from app import db


def del_files(current_files):
    db_files = File.query.all()
    for i in db_files:
        if [i.name[i.name.find('_') + 1:], i.file_path] not in current_files and 'static/content/previews_videos' not in i.file_path:
            db.session.delete(i)
    db.session.commit()

