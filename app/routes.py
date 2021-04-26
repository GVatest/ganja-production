from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import FeedbackForm, ReviewForm, LoginForm, UploadForm
from app.models import Reviews, Mails, Posts, Admin, File, Album
from flask_login import current_user, login_user, logout_user
from app.message import send_msg, send_review
from threading import Thread
import os


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', photos=File.query.filter(File.name.like('%home-page%')).all(), videos=File.query.filter(File.file_path.like('%static\content\previews_videos%')).all())


@app.route('/about')
def about():

    prep_rew = []
    for rew in Reviews.query.filter_by(flag_to_post=1):
        prep_rew.append(rew)

    reviews = {
        'reviews': prep_rew
    }

    return render_template('about.html', reviews=reviews)


@app.route('/albums')
def albums():
    albums = Album.query.all()
    for album in albums:
        album.preview = '/'.join(album.preview.split('\\'))
    return render_template('albums.html', albums=albums)


@app.route('/<album_name>/view')
def album_viewer(album_name):
    photos = File.query.filter(File.name.like(f'%{album_name}%')).all()
    return render_template('view.html', photos=photos)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    feedback_form = FeedbackForm()
    review_form = ReviewForm()

    if feedback_form.send.data and feedback_form.validate():
        mail = Mails()
        mail.name = feedback_form.name.data
        mail.surname = feedback_form.surname.data
        mail.email = feedback_form.email.data
        mail.message = feedback_form.message.data
        db.session.add(mail)
        send_msg(feedback_form.name.data, feedback_form.surname.data, feedback_form.email.data, feedback_form.message.data)
        db.session.commit()
        return redirect('/contacts')

    if review_form.leave.data and review_form.validate():
        review = Reviews()
        review.name = review_form.rname.data
        review.email = review_form.remail.data
        review.review = review_form.review.data
        review.photo = 'static\images\logo.jpg'
        review.flag_to_post = 0
        db.session.add(review)
        send_review(review_form.rname.data, review_form.remail.data, review_form.review.data)
        db.session.commit()
        return redirect('/contacts')
    return render_template('contacts.html', fb=feedback_form, rv=review_form)


@app.route('/posts')
def blog():

    posts = {
        'posts': Posts.query.all()
    }

    return render_template('posts.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/admin')
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(admin, remember=True)
        return redirect('/admin')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
