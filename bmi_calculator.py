from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

# Blueprint definition
bmi_calculator_blueprint = Blueprint('bmi_calculator', __name__)

# In-memory user store (use a database in production)
users = {}

# Route for the Home page
@bmi_calculator_blueprint.route('/')
def home():
    return render_template('index.html')

# Route for BMI calculation
@bmi_calculator_blueprint.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi = weight / ((height / 100) ** 2)
    return render_template('index.html', bmi=bmi)

# Route for the About page
@bmi_calculator_blueprint.route('/about')
def about():
    return render_template('about.html')

# Route for the Blog page
@bmi_calculator_blueprint.route('/blog')
def blog():
    blog_posts = [
        {'title': 'First Blog Post', 'content': 'Lorem ipsum dolor sit amet...'},
        {'title': 'Second Blog Post', 'content': 'Consectetur adipiscing elit...'},
        {'title': 'Third Blog Post', 'content': 'Sed do eiusmod tempor incididunt...'}
    ]
    return render_template('blog.html', blog_posts=blog_posts)

# Route for the Contact page
@bmi_calculator_blueprint.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the Login page
@bmi_calculator_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('bmi_calculator.dashboard'))
        else:
            flash("Invalid credentials. Please try again.")
    return render_template('login.html')

# Route for the Registration page
@bmi_calculator_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username in users:
            flash("Username already exists. Please choose a different one.")
        else:
            hashed_password = generate_password_hash(password, method='sha256')
            users[username] = {'email': email, 'password': hashed_password}
            flash("Registration successful! Please log in.")
            return redirect(url_for('bmi_calculator.login'))
    return render_template('register.html')

# Route for the Dashboard (protected page)
@bmi_calculator_blueprint.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('bmi_calculator.login'))
    username = session['username']
    return render_template('dashboard.html', username=username)

# Route for the Profile page
@bmi_calculator_blueprint.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('bmi_calculator.login'))
    username = session['username']
    user_data = users.get(username)
    return render_template('profile.html', user=user_data)

# Route for the Settings page
@bmi_calculator_blueprint.route('/settings')
def settings():
    if 'username' not in session:
        return redirect(url_for('bmi_calculator.login'))
    return render_template('settings.html')

# Route for the Logout
@bmi_calculator_blueprint.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.")
    return redirect(url_for('bmi_calculator.login'))
