
# Library Management System

A simple Library Management System built using Flask and SQLAlchemy. The system allows users (librarians) to manage books, members, and transactions like issuing and returning books. The project also supports adding multiple entries (books and members) at once, and calculates a fee for book returns based on the time the book was borrowed.

### API hosted at : https://santhosh6328.pythonanywhere.com

## Features

- **Books Management**: Add, update, delete, and search for books.
- **Members Management**: Add, update, delete, and search for library members.
- **Transactions**: Issue books to members and return books with automated fee calculation (based on the time the book is held).
- **Fee Calculation**: Charges 1 rupee per second for each book return, based on the time difference between the issue date and return date.
- **Bulk Entry**: Supports adding multiple books and members in a single request.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Flask-SQLAlchemy**: SQLAlchemy extension for Flask to handle database operations.
- **Flask-Migrate**: Extension for database migrations using Alembic.
- **SQLite**: Default database (can be switched to PostgreSQL or others).
- **RESTful API**: The system is exposed as a RESTful API.

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Step-by-Step Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/santhosh6328/library-app.git
    cd library-app
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv\Scripts\activate
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:

    If you are using **Flask-Migrate** for database migrations, initialize the database by running:

    ```bash
    flask db init       # Only run this if setting up migrations for the first time
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Run the application**:

    Start the Flask development server:

    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000/`.

### Project Structure

```bash
library-app/
│
├── app/
│   ├── __init__.py             # Application factory and initialization
│   ├── models/
│   │   ├── book_model.py       # Book model
│   │   ├── member_model.py     # Member model
│   │   ├── transaction_model.py # Transaction model
│   ├── routes/
│   │   ├── book_route.py       # Routes related to book management
│   │   ├── member_route.py     # Routes related to member management
│   │   ├── transaction_route.py # Routes related to transactions
│   └── ...
├── migrations/                 # Flask-Migrate migration files
├── requirements.txt            # Python dependencies
├── run.py                      # Main entry point for running the application
└── README.md                   # Project README file
```

## API Endpoints

#### Note: postman collection for all the apis are attached in /postman folder

### Books

- **GET /books** - Get all books.
- **POST /books** - Add multiple books. Expects a list of book objects.
- **DELETE /books** - delete books.
- **GET /books/search** - Search for books by title and author.

### Members

- **GET /members** - Get all members.
- **POST /members** - Add multiple members. Expects a list of member objects.
- **DELETE /members** - delete members.


### Transactions

- **POST /issue_book** - Issue a book to a member.
- **POST /return_book** - Return a book.
- **POST /all_transactions** - Return all transactions.

## Example Requests

### Adding Multiple Books

**POST /books/add**

```json
[
    {
        "title": "The Great Gatsby",
        "authors": "F. Scott Fitzgerald",
        "isbn": "9780743273565",
        "stock": 25
    },
    {
        "title": "1984",
        "authors": "George Orwell",
        "isbn": "9780451524935",
        "stock": 15
    }
]
```

### Adding Multiple Members

**POST /members/add**

```json
[
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890"
    },
    {
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "phone": "0987654321"
    }
]
```

### Returning a Book

**POST /books/return**

```json
{
    "transaction_id": 1
}
```

Response:

```json
{
    "message": "Book returned successfully",
    "fee_charged": 120,   # Fee charged based on time difference in seconds
    "return_time_epoch": 1697818800
}
```
