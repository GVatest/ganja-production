from app import app, db
from flask_admin.contrib.sqla import ModelView
from app import admin, login
from flask import redirect, url_for, request
from flask_login import current_user
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin


path = op.join(op.dirname(__file__), 'static')


class MyFileAdmin(FileAdmin):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login')


class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login')

