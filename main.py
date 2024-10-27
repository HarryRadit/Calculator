from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']


        if operation == 'add':
            result = int(num1) + int(num2)
        elif operation == 'subtract':
            result = int(num1) - int(num2)
        elif operation == 'multiply':
            result = int(num1) * int(num2)
        elif operation == 'divide':
            result = int(num1) / int(num2)

    return render_template('calculatory.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)

