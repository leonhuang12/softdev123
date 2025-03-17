from flask import render_template, url_for, flash, redirect, request, Blueprint, g
from app import bcrypt, login_manager
from app.forms import RegistrationForm, LoginForm, StoryForm, ContributionForm
from app.models import query_db, user_loader, User
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return user_loader(user_id)

@main.teardown_app_request
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@main.route("/")
@main.route("/home")
# @login_required
def home():
    user_stories = query_db('SELECT * FROM story WHERE author_id = ?', [current_user.get_id()])
    contributions = query_db('SELECT * FROM contribution WHERE user_id = ?', [current_user.get_id()])
    return render_template('home.html', stories=user_stories, contributions=contributions)

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        query_db('INSERT INTO user (username, email, password) VALUES (?, ?, ?)', 
                [form.username.data, form.email.data, hashed_password])
        get_db().commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = query_db('SELECT * FROM user WHERE email = ?', [form.email.data], one=True)
        if user and bcrypt.check_password_hash(user[3], form.password.data):
            user_obj = User(id=user[0], username=user[1], email=user[2], password=user[3])
            login_user(user_obj, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/story/new", methods=['GET', 'POST'])
# @login_required
def new_story():
    form = StoryForm()
    if form.validate_on_submit():
        query_db('INSERT INTO story (title, content, author_id) VALUES (?, ?, ?)', 
                [form.title.data, form.content.data, current_user.id])
        get_db().commit()
        flash('Your story has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_story.html', title='New Story', form=form)

@main.route("/story/<int:story_id>", methods=['GET', 'POST'])
@login_required
def add_to_story(story_id):
    story = query_db('SELECT * FROM story WHERE id = ?', [story_id], one=True)
    form = ContributionForm()
    if form.validate_on_submit():
        query_db('INSERT INTO contribution (content, user_id, story_id) VALUES (?, ?, ?)', 
                [form.content.data, current_user.id, story_id])
        get_db().commit()
        flash('Your contribution has been added!', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_to_story.html', title='Add to Story', form=form, story=story)