# 📚 E-Book Manager

A sleek, minimalist web application for managing and viewing an e-book collection with PostgreSQL backend and modern frontend.

## 🚀 Features

- **📖 E-Book Overview**: Grid/list view of all e-books with cover images, titles, authors, publication years, genres, prices, and ratings
- **🔍 Detailed View**: Comprehensive book information including publisher and ISBN
- **🖨️ Print-Friendly**: Optimized print layout for catalog creation
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **⚡ Fast API**: RESTful backend with PostgreSQL database
- **🧪 Tested**: Both frontend and backend test suites included

## 📊 Book Information Displayed

Each e-book shows:
- 📸 **Cover Image** (Image-URL-M)
- 📚 **Title**
- ✍️ **Author**
- 📅 **Year of Publication**
- 🏷️ **Genre** (Fiction, History, Science, etc.)
- 💰 **Price** (USD)
- ⭐ **Rating** (1-5 stars)
- 🏢 **Publisher** (detailed view)
- 🔢 **ISBN** (detailed view)

## 🛠️ Technologies Used

### Frontend
- **HTML5** - Modern semantic markup
- **CSS3** - Responsive design with Flexbox/Grid  
- **JavaScript (ES6+)** - Vanilla JS for optimal performance

### Backend
- **FastAPI** - High-performance Python web framework
- **PostgreSQL** - Robust relational database
- **SQLAlchemy** - ORM for database operations
- **Uvicorn** - ASGI server

## ✨ New Features Added

- **🏷️ Genre Classification**: Books categorized by genre (Fiction, History, Science, etc.)
- **💰 Pricing Information**: Display book prices in USD
- **⭐ Rating System**: Star ratings from 1-5 for each book
- **🧪 Enhanced Testing**: Comprehensive test coverage for new fields
- **🎨 Improved UI**: Color-coded genre, price, and rating display
- **📱 Updated Responsive Design**: Better mobile experience with new fields

## 🔧 Updated API Endpoints

### GET /books
Returns array of books with **all new fields**:
- ISBN, title, author, year, cover
- **NEW**: gender, price, rating

### GET /books/{isbn}  
Returns detailed book information including publisher and **all new fields**.

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
- Backend tests: Run `pytest test_main.py` in the `backend/` directory
- Frontend tests: Open `frontend/test/index.html` in your browser to run Mocha tests

## Project Structure
- `backend/`: FastAPI backend
  - `main.py`: FastAPI application
  - `test_main.py`: Backend tests
- `frontend/`: HTML/CSS/JS frontend
- `frontend/test/`: Mocha tests
  - `app.test.js`: Frontend JavaScript tests

Used adjusted data set:
J. Schler, M. Koppel, S. Argamon and J. Pennebaker (2006). Effects of Age and Gender on Blogging in Proceedings of 2006 AAAI Spring Symposium on Computational Approaches for Analyzing Weblogs. URL: http://www.cs.biu.ac.il/~schlerj/schler_springsymp06.pdf


---

**Happy Reading!** 📚✨


