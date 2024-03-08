from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
        except:
            result = "You should enter a real number"
            return render_template('index.html', result=result)

        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Cannot divide by zero'

    
    return render_template('index.html', result=result)


    


if __name__ == "__main__":
    app.run(debug = True)