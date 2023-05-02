# FastAPI Solution
This is a solution built with FastAPI for processing orders and filtering them based on a given criterion.

## Installation
Clone the repository:
```bash
git clone https://github.com/<username>/<repository>.git
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Usage
Start the FastAPI server:
```css
python app/main.py
```
Make a POST request to the /solution endpoint with the following JSON payload:
```json
{
  "orders": [
    {
      "id": 1,
      "item": "Laptop",
      "quantity": 1,
      "price": 999.99,
      "status": "completed"
    },
    {
      "id": 2,
      "item": "Smartphone",
      "quantity": 2,
      "price": 499.95,
      "status": "pending"
    },
    {
      "id": 3,
      "item": "Headphones",
      "quantity": 3,
      "price": 99.90,
      "status": "completed"
    },
    {
      "id": 4,
      "item": "Mouse",
      "quantity": 4,
      "price": 24.99,
      "status": "canceled"
    }
  ],
  "criterion": "completed"
}
```
The response will be the total price of the filtered orders.
## API Documentation
The API documentation can be found by accessing the /docs endpoint when the server is running. This provides an interactive documentation UI that can be used to test the API endpoints.

## API Live Server
There is an actual live server running with the implementation of this "solution" endpoint at https://fast-api-solution.onrender.com

For testing this implementation you can execute the following ´bash´ request:
```bash
curl -X POST "https://fast-api-solution.onrender.com/solution" -H "Content-Type: application/json" -d '{
  "orders": [
    {
      "id": 1,
      "item": "Laptop",
      "quantity": 1,
      "price": 999.99,
      "status": "completed"
    },
    {
      "id": 2,
      "item": "Smartphone",
      "quantity": 2,
      "price": 499.95,
      "status": "pending"
    },
    {
      "id": 3,
      "item": "Headphones",
      "quantity": 3,
      "price": 99.90,
      "status": "completed"
    },
    {
      "id": 4,
      "item": "Mouse",
      "quantity": 4,
      "price": 24.99,
      "status": "canceled"
    }
  ],
  "criterion": "completed"
}'
```