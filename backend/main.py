# FastAPI backend for E-Book Manager
# Requirements: fastapi, uvicorn, asyncpg, sqlalchemy

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.future import select
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:123456@localhost:5432/Books"
)

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    ISBN = Column("isbn",String, primary_key=True, index=True)
    Book_Title = Column("title", String)
    Book_Author = Column("author", String)
    Year_Of_Publication = Column("year", Integer)
    Publisher = Column("publisher",String)
    Image_URL_M = Column("img_m", String)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/books")
async def get_books():
    async with SessionLocal() as session:
        result = await session.execute(select(Book))
        books = result.scalars().all()
        return [
            {
                "ISBN": b.ISBN,
                "title": b.Book_Title,
                "author": b.Book_Author,
                "year": b.Year_Of_Publication,
                "cover": b.Image_URL_M
            }
            for b in books
        ]

@app.get("/books/{isbn}")
async def get_book(isbn: str):
    async with SessionLocal() as session:
        result = await session.execute(select(Book).where(Book.ISBN == isbn))
        book = result.scalar_one_or_none()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return {
            "ISBN": book.ISBN,
            "title": book.Book_Title,
            "author": book.Book_Author,
            "year": book.Year_Of_Publication,
            "publisher": book.Publisher,
            "cover": book.Image_URL_M
        }
