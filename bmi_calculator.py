from flask import Blueprint, render_template, request

# Blueprint definition
bmi_calculator_blueprint = Blueprint('bmi_calculator', __name__)

# Route for the Home page with BMI calculation
@bmi_calculator_blueprint.route('/')
def home():
    return render_template('index.html')

# Route for BMI calculation
@bmi_calculator_blueprint.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    # Extracting height and weight from the form
    height = float(request.form['height'])
    weight = float(request.form['weight'])

    # Calculating BMI
    bmi = weight / ((height / 100) ** 2)

    # Rendering the home template with BMI value
    return render_template('index.html', bmi=bmi)

# Route for the About page
@bmi_calculator_blueprint.route('/about')
def about():
    return render_template('about.html')

# Route for the Blog page
@bmi_calculator_blueprint.route('/blog')
def blog():
    # blog posts
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
        # Implement your login logic here
        username = request.form['username']
        password = request.form['password']
        # Check username and password validity
        if username == 'admin' and password == 'password':
            # Redirect to a protected page or dashboard
            return render_template('dashboard.html', username=username)
        else:
            # Display login failed message or redirect to login page with error
            return render_template('login.html', error="Invalid credentials. Please try again.")
    # If GET method, display the login form
    return render_template('login.html')

# Route for the Dashboard (protected page)
@bmi_calculator_blueprint.route('/dashboard')
def dashboard():
    #Check if user is authenticated (session-based or token-based)
    # uthenticated
    username = 'admin'  # Replace with actual authentication logic
    return render_template('dashboard.html', username=username)

 #routes for additional pages as needed
@bmi_calculator_blueprint.route('/settings')
def settings():
    return render_template('settings.html')

@bmi_calculator_blueprint.route('/profile')
def profile():
    # Fetch user profile data 
    user_data = {'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30}
    return render_template('profile.html', user=user_data)

@bmi_calculator_blueprint.route('/logout')
def logout():
    # Implement logout logic (clear session, redirect to login page)
    return render_template('login.html', message="You have been logged out.")
