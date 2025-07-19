from flask import Flask, jsonify, render_template, request, abort
import random
app = Flask(__name__)


def square_number(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n * n


@app.route('/')
def home():
    data = {
        "title": "Python CI/CD Web Flask Application",
        "message": "Built and deployed through GitHub Actions CI/CD to EC2 Amazon Linux!",
    }
    return render_template('index.html', data=data)


@app.route('/health')
def health_check():
    return jsonify(status="healthy")


@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice')
    options = ['rock', 'paper', 'scissors']

    if user_choice not in options:
        return jsonify(error="Invalid choice"), 400

    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify(
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result
    )


@app.route('/square/<int:number>', methods=['GET'])
def square(number):
    try:
        result = square_number(number)
        return jsonify(number=number, square=result)
    except ValueError as e:
        abort(400, description=str(e))


@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
    app.run(debug=True)
