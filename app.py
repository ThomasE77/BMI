from flask import Flask, render_template, request
from bmi import calculate_bmi, determine_bmi_category

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        height_feet = int(request.form['height_feet'])
        height_inches = int(request.form['height_inches'])
        weight_pounds = float(request.form['weight_pounds'])

        bmi = calculate_bmi(height_feet, height_inches, weight_pounds)
        bmi_category = determine_bmi_category(bmi)

        return render_template('result.html', bmi=bmi, category=bmi_category)

if __name__ == '__main__':
    import pytest
    pytest.main(['-v', 'bmi.py'])

    app.run(debug=True)