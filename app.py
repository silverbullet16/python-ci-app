from flask import Flask, jsonify, abort, render_template
app = Flask(__name__)


def square_number(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n * n


@app.route('/')
def home():
    data = {
        "title": "Python CI/CD Web Flask Application",
        "message": "created with Github Actions CI/CD Deployment to EC2 Amazon Linux!",
    }
    return render_template('index.html', data=data)


@app.route('/health')
def health_check():
    return jsonify(status="healthy")


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
