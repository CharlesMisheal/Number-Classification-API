# Number Classification API

This is a simple Flask-based API that returns interesting mathematical properties and a fun fact about a given number.

## Features

- *Is prime*: Check if the number is prime.
- *Is perfect*: Check if the number is a perfect number.
- *Properties*: Get a list of properties (e.g., even/odd, Armstrong, perfect square).
- *Digit sum*: Calculate the sum of the digits of the number.
- *Fun fact*: Fetch a fun fact about the number from the Numbers API (math type).
- *CORS Support*: Allows cross-origin requests.
- *Error Handling*: Returns a 400 Bad Request for invalid inputs.

## API Endpoint
GET <your-url>/api/classify-number?number=371
I will be using the number 371

Example Response (200 OK)
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

## Error Response (400 Bad Request)
{
    "number": "alphabet",
    "error": true
}
**Note:** Only valid integers are accepted

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Number-Classification-API.git
   cd Number-Classification-API

2. Install dependencies:
    pip install -r requirements

3. Run the Flask app
    python app.py

4. Access the API at:
    http://127.0.0.1:5000/

## Deployment
Deploy the API (Optional)

To make your API publicly accessible, you can deploy it using a platform like *Heroku, **Vercel, or **Render. 

Here’s how to deploy on **Heroku*:

1. Create a Procfile in your project folder:
   ```plaintext
   web: python app.py 

## Tech Stack
Python(Flask)
External API:NumbersAPI