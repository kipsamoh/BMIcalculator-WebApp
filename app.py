from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'kipsamoh8698'  # Replace with a secure key

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example SQLite URI, replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Home page redirect
@app.route('/')
def home():
    from bmi_calculator import bmi_calculator_blueprint  # Import inside function to avoid circular import
    return redirect(url_for('bmi_calculator.home'))

# Ensure the database tables are created before the first request
@app.before_startup
def create_tables():
    from bmi_calculator import bmi_calculator_blueprint  # Import inside function to avoid circular import
    db.create_all()

# Register blueprint for BMI calculator routes
from bmi_calculator import bmi_calculator_blueprint
app.register_blueprint(bmi_calculator_blueprint, url_prefix='/bmi_calculator')

if __name__ == '__main__':
    app.run(debug=True)
