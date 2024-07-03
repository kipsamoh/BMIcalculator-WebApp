from flask import Flask, redirect, url_for
from bmi_calculator import bmi_calculator_blueprint

app = Flask(__name__)
app.secret_key = 'kipsamoh8698'  # Replace with a secure key

# Registering the blueprint for BMI calculator routes
app.register_blueprint(bmi_calculator_blueprint, url_prefix='/bmi_calculator')

# Home page
@app.route('/')
def home():
    return redirect(url_for('bmi_calculator.home'))

if __name__ == '__main__':
    app.run(debug=True)
