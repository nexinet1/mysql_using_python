import mysql.connector

# establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

# create a cursor object to execute SQL queries
cursor = db.cursor()

# define the data to be inserted into the database
data = [
    ("John", "Doe", "john.doe@email.com"),
    ("Jane", "Doe", "jane.doe@email.com"),
    ("Bob", "Smith", "bob.smith@email.com")
]

# define the SQL query to insert the data into the database
query = "INSERT INTO customers (first_name, last_name, email) VALUES (%s, %s, %s)"

# use a pipeline to insert the data into the database
for row in data:
    cursor.execute(query, row)
    db.commit()

# print a confirmation message
print(cursor.rowcount, "rows inserted successfully into the customers table")

# close the cursor and database connection
cursor.close()
db.close()
