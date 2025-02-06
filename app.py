from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to check if a number is a prime number
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is a perfect number
def is_perfect(n):
    """Check if a number is perfect."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n
# Function to check if a number is an Armstrong number
def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

# Function to calculate the sum of digits
def digit_sum(n):
    """Calculate the sum of digits."""
    return sum(int(d) for d in str(n))

# Function to get a fun fact about a number
def get_fun_fact(n):
    """Get a fun fact about a number."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available.")
        return "No fun fact available."
    except Exception:
        return "Error fetching fun fact."

@app.route("/")
def home():
    """Return a welcome message."""
    return "Hello, your Flask API is running on Heroku!"
# API endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """Classify a number based on its properties."""
    number = request.args.get('number')
    if not number:
        return jsonify({"error": "Invalid input. Please provide a valid number."}), 400
    try:
        number = float(number)
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide a valid number."}), 400
    
    # Determine properties
    properties = []
    if is_armstrong(int(number)):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
         # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime(int(number)),
        "is_perfect": is_perfect(int(number)),
        "properties": properties,
        "digit_sum": digit_sum(int(number)),
        "fun_fact": get_fun_fact(int(number))
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

