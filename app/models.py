from app import db, admin, login
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.admin import MyModelView, MyFileAdmin, path


class Mails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    surname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    message = db.Column(db.String, index=True)

    def __repr__(self):
        return '<Name: {}, message: {}>'.format(self.name, self.message)


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120))
    review = db.Column(db.String)
    photo = db.Column(db.String, index=True)
    flag_to_post = db.Column(db.String, index=True)

    def __repr__(self):
        return '<Name: {}, review: {}>'.format(self.name, self.review)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String, index=True)
    photo_path = db.Column(db.String)
    text = db.Column(db.String)

    def __repr__(self):
        return '<path to photo: {}, text: {}>'.format(self.photo_path, self.text)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Admin {}>'.format(self.username)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String, index=True)
    name = db.Column(db.String, index=True)

    def __repr__(self):
        return '<Photo {}, file_path={}'.format(self.name, self.file_path)


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    title = db.Column(db.String)
    subtitle = db.Column(db.String)
    description = db.Column(db.String)
    preview = db.Column(db.String)


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))


admin.add_view(MyFileAdmin(path, '/static/', name='Static Files'))
admin.add_view(MyModelView(Mails, db.session))
admin.add_view(MyModelView(Reviews, db.session))
admin.add_view(MyModelView(Posts, db.session))
admin.add_view(MyModelView(File, db.session))
admin.add_view(MyModelView(Album, db.session))


