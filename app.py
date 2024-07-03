from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from bmi_calculator import bmi_calculator_blueprint  # Import blueprint after initializing Flask app

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
login_manager.login_view = 'bmi_calculator.login'  # Specify the login view for Flask-Login

# Register blueprint for BMI calculator routes
app.register_blueprint(bmi_calculator_blueprint, url_prefix='/bmi_calculator')

# Home page redirect
@app.route('/')
def home():
    return redirect(url_for('bmi_calculator.home'))

# Ensure the database tables are created before the first request
# Note: Using 'with app.app_context()' to handle database initialization
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
