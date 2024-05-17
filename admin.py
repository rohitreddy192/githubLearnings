import sqlite3
from werkzeug.security import generate_password_hash

# Connect to the SQLite database
conn = sqlite3.connect("instance/users.db")
cur = conn.cursor()

# Sample data with passwords
data = [
    ('vinayrohitreddypadala12@gmail.com', 'password'),
    ('vishal@dzynkraft.ai', 'password')
]

# Insert data into the table with hashed passwords
for email, password in data:
    hashed_password = generate_password_hash(password)
    cur.execute('''INSERT INTO User (email, password) VALUES (?, ?)''', (email, hashed_password))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
