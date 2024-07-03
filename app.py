from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Ensure the database tables are created before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Home page redirect
@app.route('/')
def home():
    from bmi_calculator import bmi_calculator_blueprint  # Import within the function to avoid circular import
    return redirect(url_for('bmi_calculator.home'))

if __name__ == '__main__':
    app.run(debug=True)
