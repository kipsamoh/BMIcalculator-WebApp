from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Message  # Import db and models from the package
from flask_login import login_user, logout_user, current_user, login_required

# Blueprint definition
bmi_calculator_blueprint = Blueprint('bmi_calculator', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
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
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please choose a different one.")
        else:
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.")
            return redirect(url_for('bmi_calculator.login'))
    return render_template('register.html')

# Route for the Dashboard (protected page)
@bmi_calculator_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

# Route for the Profile page
@bmi_calculator_blueprint.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

# Route for the Settings page
@bmi_calculator_blueprint.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

# Route for the Logout
@bmi_calculator_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('bmi_calculator.login'))

# Route for sending a message
@bmi_calculator_blueprint.route('/send_message', methods=['POST'])
@login_required
def send_message():
    name = request.form['name']
    email = request.form['email']
    message_content = request.form['message']
    
    # Create a new message object
    new_message = Message(name=name, email=email, message=message_content)
    
    # Add the message to the database session
    db.session.add(new_message)
    db.session.commit()
    
    flash("Message sent successfully!")

    return redirect(url_for('bmi_calculator.contact'))
