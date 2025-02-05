# Number Properties API

## Overview
This is my first API task experience with HNG internship. It is a Flask-based API that provides detailed mathematical properties and fun-facts for a given number. The number 371 was used as an example as required in this task, but you can use any number of your choice.

## Features
- Classify number properties
- Identify prime, perfect, and Armstrong numbers
- Generate fun mathematical facts
- Robust error handling

## Endpoints

### 1. URL Parameter Endpoint
**Path:** `/number/<number>`
**Method:** GET
**Example:** `http://your-domain/number/371`

### 2. Query Parameter Endpoint
**Path:** `/api/classify-number`
**Method:** GET
**Query Parameter:** `number`
**Example:** `http://your-domain/api/classify-number?number=371`

## Response Structure

### Success Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["odd", "armstrong"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```

### Error Response
```json
{
    "number": "alphabet",
    "error": true,
    "message": "Please provide a valid number"
}
```

## Supported Number Properties
- Even/Odd
- Prime
- Perfect
- Armstrong

## Installation

### Prerequisites
- Python 
- Flask
- Requests library

### Steps
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run application

## Deployment
- You can deploy this api to any platform but i used heroku
- Runs on port 5000

## Error Handling
- Handles non-numeric inputs
- Validates positive numbers
- Provides descriptive error messages


