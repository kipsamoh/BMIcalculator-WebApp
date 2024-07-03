from flask import Flask, render_template, request, redirect, url_for
from bmi_calculator import bmi_calculator_blueprint

app = Flask(__name__)

# Registering the blueprint for BMI calculator routes
app.register_blueprint(bmi_calculator_blueprint)

# Example user database (replace with your actual user management)
users = {
    'john': {'password': 'password123'},
    'jane': {'password': 'password456'}
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
    # Sample data for blog posts (replace with actual data retrieval logic)
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
        
        if username in users and users[username]['password'] == password:
            # Example: set session variable for logged in user
            return redirect(url_for('bmi_calculator.home'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
