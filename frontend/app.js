const API_URL = "http://localhost:8000/books";

const bookList = document.getElementById("book-list");
const bookDetail = document.getElementById("book-detail");
const backBtn = document.getElementById("back-btn");

function showOverview() {
    bookList.classList.remove("hidden");
    bookDetail.classList.add("hidden");
    backBtn.classList.add("hidden");
}

function showDetail() {
    bookList.classList.add("hidden");
    bookDetail.classList.remove("hidden");
    backBtn.classList.remove("hidden");
}

function renderBooks(books) {
    bookList.innerHTML = books.map(book => `
        <div class="book-card" data-isbn="${book.ISBN}">
            <img class="book-cover" src="${book.cover}" alt="${book.title}">
            <div class="book-title">${book.title}</div>
            <div class="book-author">${book.author}</div>
            <div class="book-year">${book.year}</div>
        </div>
    `).join("");
}

function renderBookDetail(book) {
    bookDetail.innerHTML = `
        <img src="${book.cover}" alt="${book.title}">
        <h2>${book.title}</h2>
        <div class="meta"><strong>Author:</strong> ${book.author}</div>
        <div class="meta"><strong>Year:</strong> ${book.year}</div>
        <div class="meta"><strong>Publisher:</strong> ${book.publisher}</div>
        <div class="meta"><strong>ISBN:</strong> ${book.ISBN}</div>
    `;
}

async function fetchBooks() {
    const res = await fetch(API_URL);
    const books = await res.json();
    renderBooks(books);
}

async function fetchBookDetail(isbn) {
    const res = await fetch(`${API_URL}/${isbn}`);
    const book = await res.json();
    renderBookDetail(book);
    showDetail();
}

bookList.addEventListener("click", e => {
    const card = e.target.closest(".book-card");
    if (card) {
        fetchBookDetail(card.dataset.isbn);
    }
});

backBtn.addEventListener("click", () => {
    showOverview();
});

// Initial load
fetchBooks();
showOverview();
