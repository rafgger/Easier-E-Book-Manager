# 📚 Loading Books.csv into PostgreSQL with pgAdmin

This guide explains how to load entries of `Books.csv` into a PostgreSQL table using `pgAdmin`.
---

## 🏗️ Step 1: Create database (Books) and Table (books) in pgAdmin.
---

## 📝 Step 2: Prepare the CSV File

Make sure your CSV has a header row. Add the following as the first line if it's missing:

```
csv:
isbn,title,author,year,publisher,img_m,genre,price,rating
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
    img_m TEXT,
    genre VARCHAR(50),
    price DECIMAL(10,2),
    rating DECIMAL(3,1)
);

-- If the table already exists, add the new columns with:
ALTER TABLE public.books ADD COLUMN IF NOT EXISTS genre VARCHAR(50);
ALTER TABLE public.books ADD COLUMN IF NOT EXISTS price DECIMAL(10,2);
ALTER TABLE public.books ADD COLUMN IF NOT EXISTS rating DECIMAL(3,1);

-- If you had the old 'gender' column, rename it:
ALTER TABLE public.books RENAME COLUMN gender TO genre;
```

We should see the imported entries.

