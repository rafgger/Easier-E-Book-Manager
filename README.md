# 📚 E-Book Manager

A sleek, minimalist web application for managing and viewing an e-book collection with PostgreSQL backend and modern frontend. This is a easier version of [Harder-E-Book-Manager](https://github.com/rafgger/Harder-E-Book-Manager).


<a href="https://youtu.be/QnpynhklHaQ" target="_blank">
  <img src="https://github.com/user-attachments/assets/2f7ad878-8c01-4cd3-ba44-7b854df35d3e" alt="Easier E-Book Manager" width="500"/>
</a>


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
- 🏷️ **Genre** (Fiction, History, Science, etc.) - String field
- 💰 **Price** (USD) - Numeric field (DECIMAL 10,2) with currency formatting
- ⭐ **Rating** (1-5 stars) - Numeric field (DECIMAL 3,1) with star display
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
- **NEW**: genre, price, rating

### GET /books/{isbn}  
Returns detailed book information including publisher and **all new fields**.

## Technologies
- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI (Python)
- Database: PostgreSQL

## 🔧 Setup Instructions

### Prerequisites
- **Python 3.8+** installed
- **PostgreSQL** database server running
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Database Setup
1. Create PostgreSQL database named `Books`
2. Follow instructions in `CREATE_DB.md` to set up the schema
3. Import sample data from `Books.csv`

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables (optional):
   ```bash
   set DATABASE_URL=postgresql://username:password@localhost/Books
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
5. Verify API is running at `http://localhost:8000/docs`

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Open `index.html` in your browser
3. The app will automatically connect to the backend at `http://localhost:8000`

**Note:** No additional frontend setup required - uses vanilla JavaScript!

### 🧪 Testing

#### Backend Tests
```bash
cd backend
python -m pytest test_main.py -v
```
- **Model Structure Test**: Verifies Book model has correct fields with proper data types
- **API Endpoint Test**: Validates `/books` returns all required fields including numeric price/rating

#### Frontend Tests
Open `frontend/test/standalone.html` in your browser for self-contained tests.
- **6 comprehensive tests** covering all functionality
- **No external dependencies** (works offline)
- Tests book rendering, detail view, and navigation
- Validates proper handling of numeric price and rating values
- Self-contained test framework (no CDN dependencies)

**Alternative test files available:**
- `frontend/test/standalone.html` - **RECOMMENDED** (self-contained, always works)
- `frontend/test/index.html` - Original Mocha/Chai tests (requires CDN access)
- `frontend/test/debug.html` - Debug version (legacy)

#### Test Results Expected:
- ✅ **Backend**: 2/2 tests passing (model structure + API endpoints)
- ✅ **Frontend**: 6/6 tests passing (rendering, navigation, data handling)

## 🔧 API Endpoints

### GET /books
Returns array of books with all fields including numeric price and rating:
```json
{
  "ISBN": "string",
  "title": "string", 
  "author": "string",
  "year": number,
  "cover": "string",
  "genre": "string",
  "price": number,    // DECIMAL(10,2)
  "rating": number    // DECIMAL(3,1)
}
```

### GET /books/{isbn}
Returns detailed book information including publisher, with same numeric data types.

## 🖨️ Print Feature

The application includes a print-optimized layout accessible via browser's print function (Ctrl+P).

## ✨ Key Features Implemented

- **🏷️ Genre Classification**: Books categorized by genre (Fiction, History, Science, etc.)
- **💰 Numeric Pricing**: Database-enforced DECIMAL(10,2) with currency formatting ($45.99)
- **⭐ Numeric Ratings**: Database-enforced DECIMAL(3,1) with star display (★4.2)
- **🧪 Comprehensive Testing**: Backend and frontend test suites with 100% pass rate
- **🎨 Enhanced UI**: Color-coded display with proper numeric formatting
- **📱 Responsive Design**: Works seamlessly across devices
- **🔄 Self-Contained Tests**: Frontend tests work without external CDN dependencies
- **📖 Print Optimization**: Clean print layout for catalog creation
- **⚡ Fast Performance**: Vanilla JavaScript for optimal speed
- **🔒 Data Integrity**: Proper data types and validation at all layers

## 🎯 Project Status

✅ **COMPLETED** - All features implemented and tested  
✅ **Backend** - FastAPI with PostgreSQL integration  
✅ **Frontend** - Responsive UI with modern design  
✅ **Database** - Proper schema with numeric data types  
✅ **Testing** - Comprehensive test suites (backend + frontend)  
✅ **Documentation** - Complete setup and usage instructions  
✅ **Demo Ready** - Full demo transcript and testing guide  

---

**Happy Reading!** 📚✨


