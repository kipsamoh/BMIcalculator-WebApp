from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from bmi_calculator import bmi_calculator_blueprint

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'kipsamoh8698'  # Replace with a secure key

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example SQLite URI, replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Register blueprint for BMI calculator routes
app.register_blueprint(bmi_calculator_blueprint, url_prefix='/bmi_calculator')

# Home page redirect
@app.route('/')
def home():
    return redirect(url_for('bmi_calculator.home'))

# Define your SQLAlchemy models
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Message('{self.name}', '{self.email}')"

# Ensure the database tables are created before the first request
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
