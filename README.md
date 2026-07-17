# Inventory Management System - Flask REST API

## Overview
This project is a Flask-based REST API that simulates an inventory management system for a retail store. It allows users to perform CRUD (Create, Read, Update and Delete) operations on inventory items using a temporary Python list as storage.
The application also integrates with the OpenFoodFacts API to automatically retrieve product information using a barcode. A Command Line Interface (CLI) is included to interact with the API.

## Features

- View all inventory items
- View a single inventory item
- Add new inventory items
- Update item price and stock
- Delete inventory items
- Retrieve product information from OpenFoodFacts using a barcode
- CLI interface for interacting with the API
- Unit tests using pytest and unittest.mock

## Technologies Used

- Python 3
- Flask
- Requests
- Pipenv
- Pytest
- OpenFoodFacts API

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd flask-inventory-management-system
```

### Install dependencies using Pipenv
```bash
pipenv install
```
### Activate the virtual environment
```bash
pipenv shell
```

## Running the Application
Start the Flask server:
```bash
python app.py
```
Open another terminal, activate Pipenv again if necessary:
```bash
pipenv shell
```

Run the CLI application:
```bash
python cli.py
```

## Running the Tests
Run all tests using:
```bash
pytest
```
or
```bash
pipenv run pytest
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/inventory` | Retrieve all inventory items |
| GET | `/inventory/<item_id>` | Retrieve one inventory item |
| POST | `/inventory` | Add a new inventory item |
| PATCH | `/inventory/<item_id>` | Update an inventory item |
| DELETE | `/inventory/<item_id>` | Delete an inventory item |

## Example POST Request

```json
{
    "barcode": "737628064502",
    "price": 5.99,
    "stock": 15
}
```
If the barcode exists in OpenFoodFacts, the API automatically fills in the product name and brand.

## Project Structure
```
flask-inventory-management-system/
│
├── app.py
├── cli.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── LICENSE
└── tests/
    └── test_app.py
```