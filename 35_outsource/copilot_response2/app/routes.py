from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, StoryForm, ContributionForm
from app.models import User, Story, Contribution
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
@login_required
def home():
    user_stories = current_user.stories
    contributions = Contribution.query.filter_by(contributor=current_user).all()
    return render_template('home.html', stories=user_stories, contributions=contributions)

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
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
@login_required
def new_story():
    form = StoryForm()
    if form.validate_on_submit():
        story = Story(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(story)
        db.session.commit()
        flash('Your story has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_story.html', title='New Story', form=form)

@main.route("/story/<int:story_id>", methods=['GET', 'POST'])
@login_required
def add_to_story(story_id):
    story = Story.query.get_or_404(story_id)
    form = ContributionForm()
    if form.validate_on_submit():
        contribution = Contribution(content=form.content.data, contributor=current_user, story=story)
        db.session.add(contribution)
        db.session.commit()
        flash('Your contribution has been added!', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_to_story.html', title='Add to Story', form=form, story=story)