from flask import Flask, jsonify, request, abort
app = Flask(__name__)

# Utility function to check if a number is prime
def square_number(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n * n

@app.route('/')
def home():
    return jsonify(message="Welcome to the Python CI/CD Demo App!")

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