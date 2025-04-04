from flask import Flask, render_template, request

app = Flask(__name__) # Create a Flask application

def convert(decimal_num): # Convert decimal number to roman numeral
    roman = {
        1000:'M', 
        900:'CM', 
        500:'D', 
        400:'CD', 
        100:'C', 
        90:'XC', 
        50:'L', 
        40:'XL', 
        10:'X', 
        9:'IX', 
        5:'V', 
        4:'IV', 
        1:'I'
        }
    num_to_roman = '' # Initialize empty string to store roman numeral

    for i in roman.keys(): # Iterate through the roman dictionary
        num_to_roman += roman[i]*(decimal_num//i) #
        decimal_num %= i
    return num_to_roman # Convert decimal number to roman numeral


@app.route('/', methods=['POST', 'GET']) # Main route
def main_post(): 
    if request.method == 'POST':
        alpha = request.form['number'] # Get the number from the form
        if not alpha.isdecimal(): #
            return render_template('index.html', developer_name='Mesud', not_valid=True) 
        number = int(alpha)
        if not 0 < number < 4000:
            return render_template('index.html', developer_name='Mesud', not_valid=True)
        return render_template('index.html', valid=True, number_decimal = number , number_roman= convert(number), developer_name='Mesud')
    else:
        return render_template('index.html', developer_name='Mesud', not_valid=False)

if __name__ == '__main__':
    # app.run(debug=True) # Uncomment this line to run the app in debug mode
    app.run(host='0.0.0.0', port=80) # run the app on port 80

