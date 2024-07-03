from flask import Blueprint, render_template, request

# Blueprint definition
bmi_calculator_blueprint = Blueprint('bmi_calculator', __name__)

# Route for the Home page
@bmi_calculator_blueprint.route('/')
def home():
    return render_template('index.html')

# Route for the About page
@bmi_calculator_blueprint.route('/about')
def about():
    return render_template('about.html')

# Route for the Blog page
@bmi_calculator_blueprint.route('/blog')
def blog():
    # Sample data for blog posts (replace with actual data retrieval logic)
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
        # Example: Check username and password validity
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
    # Example: Check if user is authenticated (session-based or token-based)
    # For demonstration, assume authenticated
    username = 'admin'  # Replace with actual authentication logic
    return render_template('dashboard.html', username=username)

# Route for BMI calculation
@bmi_calculator_blueprint.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    # Extracting height and weight from the form
    height = float(request.form['height'])
    weight = float(request.form['weight'])

    # Calculating BMI
    bmi = weight / ((height / 100) ** 2)

    # Determining recommendation based on BMI
    if bmi < 18.5:
        recommendation = "You are underweight. You should consider gaining some weight."
    elif bmi >= 18.5 and bmi < 24.9:
        recommendation = "Your weight is normal. Keep up the good work!"
    elif bmi >= 25 and bmi < 29.9:
        recommendation = "You are overweight. You should consider losing some weight."
    else:
        recommendation = "You are obese. It's important to prioritize weight loss for your health."

    # Rendering the result template with BMI value and recommendation
    return render_template('result.html', bmi=bmi, recommendation=recommendation)

# Optional: Add more routes for additional pages as needed
@bmi_calculator_blueprint.route('/settings')
def settings():
    return render_template('settings.html')

@bmi_calculator_blueprint.route('/profile')
def profile():
    # Fetch user profile data (replace with actual logic)
    user_data = {'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30}
    return render_template('profile.html', user=user_data)

@bmi_calculator_blueprint.route('/logout')
def logout():
    # Implement logout logic (clear session, redirect to login page)
    return render_template('login.html', message="You have been logged out.")
