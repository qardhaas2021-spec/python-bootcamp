-- Practice books database (like beginner SQL courses)

DROP TABLE IF EXISTS books;

CREATE TABLE books (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  genre TEXT,
  year INTEGER,
  price REAL
);

INSERT INTO books (title, author, genre, year, price) VALUES
('Python Basics', 'Ahmed Ali', 'Programming', 2024, 19.99),
('SQL for Beginners', 'Sara Khan', 'Database', 2023, 24.50),
('Data Science Intro', 'John Smith', 'Data', 2025, 29.99),
('Clean Code', 'Robert Martin', 'Programming', 2008, 34.00),
('Harry Potter', 'J.K. Rowling', 'Fantasy', 1997, 12.99),
('The Alchemist', 'Paulo Coelho', 'Fiction', 1988, 10.50),
('Pandas Handbook', 'Wes McKinney', 'Data', 2022, 39.99),
('Atomic Habits', 'James Clear', 'Self-help', 2018, 16.00);
