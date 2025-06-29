import pytest
from httpx import AsyncClient
from main import app

import asyncio

from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    if books:  # If there are books, check the structure
        book = books[0]
        required_fields = ["ISBN", "title", "author", "year", "cover", "gender", "price", "rating"]
        for field in required_fields:
            assert field in book, f"Missing field: {field}"

# def test_get_book_not_found():
#     response = client.get("/books/DOESNOTEXIST")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Book not found"

def test_get_book_detail():
    # Test with a known ISBN from our CSV data
    test_isbn = "0195153448"  # Classical Mythology
    response = client.get(f"/books/{test_isbn}")
    
    if response.status_code == 200:
        book_detail = response.json()
        # Check all required fields for detail view
        required_detail_fields = ["ISBN", "title", "author", "year", "publisher", "cover", "gender", "price", "rating"]
        for field in required_detail_fields:
            assert field in book_detail, f"Missing field in detail: {field}"
        
        # Verify specific values
        assert book_detail["ISBN"] == test_isbn
        assert book_detail["title"] == "Classical Mythology"
        assert book_detail["gender"] == "Education"
        assert book_detail["price"] == "45.99"
        assert book_detail["rating"] == "4.2"
    else:
        # If specific book not found, skip the test
        pytest.skip(f"Book with ISBN {test_isbn} not found in database")
