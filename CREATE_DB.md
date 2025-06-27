# 📚 Loading Books.csv into PostgreSQL with pgAdmin

This guide explains how to load entries of `Books.csv` into a PostgreSQL table using `pgAdmin`.
---

## 🏗️ Step 1: Create database (Books) and Table (books) in pgAdmin.
---

## 📝 Step 2: Prepare the CSV File

Make sure your CSV has a header row. Add the following as the first line if it's missing:

```
csv:
isbn,title,author,year,publisher,img_m
```
Then save a new CSV file with only the first 20 entries (plus header). Call it Books_sample.csv.

## 🎨 Step 3: Create the Table in pgAdmin
Open pgAdmin and connect to your server.

Open the Query Tool and run this SQL to create the books table:

sql
```
CREATE TABLE public.books (
    isbn VARCHAR(20) PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INT,
    publisher TEXT,
    img_m TEXT
);
```

We should see the imported entries.

