from flask import Flask, render_template, request, redirect, url_for, session, flash
from bmi_calculator import bmi_calculator_blueprint
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key

# Registering the blueprint for BMI calculator routes
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
        
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
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
        
        if username in users:
            flash('Username already exists. Please choose a different one.', 'error')
        else:
            hashed_password = generate_password_hash(password, method='sha256')
            users[username] = {'email': email, 'password': hashed_password}
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

# Dashboard (protected route)
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    return render_template('dashboard.html', username=username)

# Profile page (protected route)
@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    user_data = users.get(username)
    return render_template('profile.html', user=user_data)

# Settings page (protected route)
@app.route('/settings')
def settings():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('settings.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
