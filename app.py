from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy users for login (replace with actual authentication logic)
users = {
    'user1': {'username': 'user1', 'password': 'password1'},
    'user2': {'username': 'user2', 'password': 'password2'}
}

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for BMI calculation
@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi = weight / (height ** 2)
    return render_template('index.html', bmi_result=bmi)

# Route for blog page
@app.route('/Health & Fitness Blogs')
def /HealthFitnessBlogs():
    # Dummy blog posts (replace with actual data retrieval logic)
    blog_posts = [
        {'title': 'First Post', 'content': 'Content of first post'},
        {'title': 'Second Post', 'content': 'Content of second post'}
    ]
    return render_template('blog.html', posts=blog_posts)

# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            # Dummy login success handling (replace with actual session management)
            return redirect(url_for('home'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
