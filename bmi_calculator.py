from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

bmi_calculator_blueprint = Blueprint('bmi_calculator', __name__)

# Routes within the BMI Calculator blueprint
@bmi_calculator_blueprint.route('/')
def home():
    return render_template('index.html')

@bmi_calculator_blueprint.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    # Handle BMI calculation logic here
    return render_template('index.html', bmi=bmi)

@bmi_calculator_blueprint.route('/about')
def about():
    return render_template('about.html')

@bmi_calculator_blueprint.route('/blog')
def blog():
    # Dummy data for demonstration
    blog_posts = [
        {'title': 'First Blog Post', 'content': 'Lorem ipsum dolor sit amet...'},
        {'title': 'Second Blog Post', 'content': 'Consectetur adipiscing elit...'},
        {'title': 'Third Blog Post', 'content': 'Sed do eiusmod tempor incididunt...'}
    ]
    return render_template('blog.html', blog_posts=blog_posts)

@bmi_calculator_blueprint.route('/contact')
def contact():
    return render_template('contact.html')

@bmi_calculator_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        return redirect(url_for('bmi_calculator.dashboard'))  # Redirect to dashboard on successful login
    
    return render_template('login.html')

@bmi_calculator_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic
        return redirect(url_for('bmi_calculator.login'))  # Redirect to login page after successful registration
    
    return render_template('register.html')

# Additional routes for dashboard, profile, settings, and logout within the blueprint should be defined here

