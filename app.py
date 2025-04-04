from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def game():
    secret = random.randint(1, 100)
    return render_template('index.html', secret_number=secret)

@app.route('/guess')
def check_guess():
    guess = int(request.args.get('guess'))
    secret = int(request.args.get('secret'))
    return f"Your guess {guess} is {'correct!' if guess == secret else 'wrong!'}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
