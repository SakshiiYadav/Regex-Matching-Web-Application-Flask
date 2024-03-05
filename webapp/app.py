from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    
    matches = re.findall(regex_pattern, test_string)
    
    if matches:
        return render_template('index.html', regex_matches=matches, test_string=test_string, regex_pattern=regex_pattern)
    else:
        return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, no_matches=True)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    
    # Regular expression pattern for validating email addresses
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(email_pattern, email):
        email_result = f'{email} is a valid email address'
    else:
        email_result = f'{email} is not a valid email address'
    
    return render_template('index.html', email_result=email_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
