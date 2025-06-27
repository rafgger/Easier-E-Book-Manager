# E-Book Manager

A minimalist web application to manage and view your e-book collection.

## Features
- Overview page: Grid/list of e-books with cover, title, author, year (from PostgreSQL)
- Detail page: Click a book to see all details (plus publisher, ISBN)
- Print-friendly overview (dedicated CSS)
- Responsive, clean UI
- Frontend tests with Mocha

## Technologies
- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI (Python)
- Database: PostgreSQL

## Setup Instructions

### Backend
1. Install Python 3.8+ and PostgreSQL.
2. Create the `Books` database and `books` table as described in the instructions.
3. In `backend/`, install dependencies:
   ```
pip install -r requirements.txt
   ```
4. Set your PostgreSQL connection string in the `DATABASE_URL` environment variable if needed.
5. Start the API:
   ```
uvicorn main:app --reload
   ```

See on:

```
http://localhost:8000/docs 
```

### Frontend
1. Open `frontend/index.html` in your browser.
2. The app fetches data from `http://localhost:8000/books`.

### Testing
- Open `frontend/test/index.html` in your browser to run Mocha tests.

## Project Structure
- `backend/`: FastAPI backend
- `frontend/`: HTML/CSS/JS frontend
- `frontend/test/`: Mocha tests

## Author
- [Your Name]
