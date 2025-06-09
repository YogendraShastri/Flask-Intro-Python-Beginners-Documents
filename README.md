# Flask CRUD API with SQLAlchemy

This is a simple RESTful API built using **Flask** and **SQLAlchemy**, demonstrating basic **CRUD (Create, Read, Update, Delete)** operations on a "Book" model.

## What is Flask?

[Flask](https://flask.palletsprojects.com/) is a lightweight and beginner-friendly web framework for Python that helps you build web applications and APIs quickly with minimal code. It's flexible and extensible, making it perfect for small to medium-sized projects.


## 📁 Project Structure

```
flask_crud_api/
├── app.py              # Main Flask application with all routes
├── models.py           # SQLAlchemy Book model
├── db.sqlite3          # SQLite database file (auto-created)
├── requirements.txt    # Python dependencies
├── Dockerfile          # For containerizing the app (optional)
└── README.md           # You're reading this!
```

## Technologies Used

- Python 3.10
- Flask
- SQLAlchemy (ORM for database)
- SQLite (for simplicity)
- Docker (optional, for containerized deployment)

## 🔧 Setup Instructions
___________________________
### 1. Clone the project

```bash
git clone <your-repo-url>
cd flask_crud_api
```

### 2. Set up virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

The app will be running at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## API Testing with Postman

### Create a Book

- **Method:** `POST`
- **URL:** `http://localhost:5000/book`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "published_year": 2018
}
```

### Get All Books

- **Method:** `GET`
- **URL:** `http://localhost:5000/book`


### Get a Book by ID

- **Method:** `GET`
- **URL:** `http://localhost:5000/book/1`

---

### Update a Book

- **Method:** `PUT`
- **URL:** `http://localhost:5000/book/1`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
  "title": "Atomic Habits (Updated)",
  "author": "James Clear",
  "published_year": 2019
}
```

###  Delete a Book

- **Method:** `DELETE`
- **URL:** `http://localhost:5000/book/1`


## Docker Setup (Optional)

### 1. Build the Docker image

```bash
docker build -t flask-crud-api .
```

### 2. Run the container

```bash
docker run -p 5000:5000 flask-crud-api
```

Now your app will be available at: [http://localhost:5000](http://localhost:5000)

---

## Requirements File

To generate or update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## Future Enhancements (Ideas)

- Input validation using `marshmallow` or `pydantic`
- Add pagination and sorting
- JWT authentication
- Connect to PostgreSQL or MySQL instead of SQLite
- Unit tests using `pytest` or `unittest`

---

## Acknowledgements

- Flask documentation: https://flask.palletsprojects.com/
- SQLAlchemy ORM: https://www.sqlalchemy.org/

---

## Author

Made by Yogendra Shastri — feel free to reach out! Thanks....
