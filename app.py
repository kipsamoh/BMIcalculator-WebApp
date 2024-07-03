from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from bmi_calculator import bmi_calculator_blueprint
from models import db, User

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

# Login manager setup
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprint for BMI calculator routes
app.register_blueprint(bmi_calculator_blueprint)

# In-memory user store (replace with your actual user management)
users = {
    'john': {'password': generate_password_hash('password123')},
    'jane': {'password': generate_password_hash('password456')}
}

# Home page
@app.route('/')
def home():
    return redirect(url_for('bmi_calculator.home'))

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Blog page
@app.route('/blog')
def blog():
    # data for blog posts (replace with actual data retrieval logic)
    blog_posts = [
        {'title': 'First Blog Post', 'content': 'Lorem ipsum dolor sit amet...'},
        {'title': 'Second Blog Post', 'content': 'Consectetur adipiscing elit...'},
        {'title': 'Third Blog Post', 'content': 'Sed do eiusmod tempor incididunt...'}
    ]
    return render_template('blog.html', blog_posts=blog_posts)

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('bmi_calculator.dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

# Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

# Dashboard (protected route)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Profile page (protected route)
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

# Settings page (protected route)
@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
