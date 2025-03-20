import pymysql

# Open database connection 
connection = pymysql.connect(
    host='localhost',
    user='root',  # Change to your actual MySQL username
    password='AnshJain29@',  # Change to your actual password
    db='mysql'  # Change to your actual database name
)

# Create a cursor object 
cursor = connection.cursor()

# Execute SQL query to fetch all customers
cursor.execute("SELECT * FROM customers;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Insert multiple rows
sql_query = "INSERT INTO customers (`Id`, `Name`) VALUES (%s, %s)"
data = [(7, "Ankish"), (8, "Ansh")]

# Execute the insertion query
cursor.executemany(sql_query, data)
connection.commit()
print("Data inserted successfully!")

# Update: Set new Name for customer with ID = 9
sql_update_query = """
UPDATE customers
SET Name = %s 
WHERE Id = %s
"""

# Correct updated_data as a tuple of (Name, Id)
updated_data = ("ABCD", 9)  # Updating Name to 'ABCD' for customer with ID 9

# Execute the update query
cursor.execute(sql_update_query, updated_data)
connection.commit()
print("Updated successfully!")

# Delete: Delete customer with ID = 8
sql_delete_query = "DELETE FROM customers WHERE Id = %s"
Id_to_delete = (7,)

cursor.execute(sql_delete_query, Id_to_delete)
connection.commit()
print("Deleted successfully!")

# Close the cursor and the connection
cursor.close()
connection.close()