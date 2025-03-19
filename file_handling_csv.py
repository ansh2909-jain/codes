import csv
import pandas as pd

# Open the CSV file in read mode(Reading a CSV File)
with open('sam.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        print(row)  # Each row is a list

###############################################################################

# Open the CSV file in write mode (this will overwrite the file)(Writing to a CSV File)
with open('sam.csv', mode='w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Writing header row
    csv_writer.writerow(['Name', 'Age', 'Occupation'])

    # Writing data rows
    csv_writer.writerow(['Anmol', 23, 'Engineer'])
    csv_writer.writerow(['Anu', 25, 'Designer'])

###############################################################################

# Open the CSV file in append mode(Appending to a CSV File)
with open('sam.csv', mode='a', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Appending data rows
    csv_writer.writerow(['Samyak', 28, 'Doctor'])

###############################################################################

# Open the CSV file in read mode( Reading CSV with DictReader (Using Dictionaries))
with open('sam.csv', mode='r') as file:
    # Create a CSV DictReader object
    csv_reader = csv.DictReader(file)

    # Iterate through the rows and print each row as a dictionary
    for row in csv_reader:
        print(row)  # Each row is a dictionary

###############################################################################

# Data to be written as a dictionary(Writing CSV with DictWriter (Using Dictionaries))
data = [
    {'Name': 'Anmol', 'Age': 23, 'Occupation': 'Engineer'},
    {'Name': 'Anu', 'Age': 25, 'Occupation': 'Designer'},
]

# Open the CSV file in write mode
with open('sam.csv', mode='w', newline='') as file:
    # Define fieldnames (column headers)
    fieldnames = ['Name', 'Age', 'Occupation']

    # Create a CSV DictWriter object
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    csv_writer.writeheader()

    # Write the data rows
    csv_writer.writerows(data)

###############################################################################

# Open the CSV file(Reading/Handling Large CSV Files)
with open('large_file.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Process each row individually to save memory
    for row in csv_reader:
        # Process the row (for example, print it)
        print(row)

###############################################################################

# Reading a CSV file(CSV File Handling with pandas)
df = pd.read_csv('sam.csv')
print(df)

# Writing to a CSV file
df.to_csv('output.csv', index=False)

###############################################################################

