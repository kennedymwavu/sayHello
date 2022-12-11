from flask import Flask, render_template, request, flash

# to initialize our application:
app = Flask(__name__)
# that creates a class for our app

app.secret_key = 'manbearpig_MUDMAN888'

@app.route('/hello')
def index():
    flash("What's your name?")
    return render_template('index.html')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash('Hi ' + str(request.form['name_input']) + ', greetings!')
    return render_template('index.html')
