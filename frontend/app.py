import flask_bcrypt as bcrypt
from  flask  import Flask
from flask import render_template
from flask import  flash, redirect, url_for
from .forms import LoginForm, SearchForm
from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from .models import db


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b84ec431597ecc1b44d18c7a5c2edc3d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://syncthia:mylovelypc@localhost/scrolls'

db.init_app(app)


bcrypt = bcrypt.Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/genres')
def genres():
    return render_template('genres.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('You have been logged in!', 'success')
            return redirect(url_for('base'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

from flask import render_template
from .forms import RegisterForm

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = models.User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/search')
def search():
    return render_template('search.html')

#base  can only be accessed by logged in users
@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

