from faker import Faker
import sqlite3
from datetime import datetime


# Method to create table
def create_table():
    # Creating DB connection
    conn_obj = sqlite3.connect('social_network.db')

    # cursor object
    cursor_obj = conn_obj.cursor()

    # creating table to store the data
    create_table_query = """ CREATE TABLE IF NOT EXISTS people ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL, address TEXT NOT NULL, city TEXT NOT NULL, province TEXT NOT NULL, bio TEXT, age INTEGER, created_at DATETIME NOT NULL, updated_at DATETIME NOT NULL ); """

    # Query execution
    cursor_obj.execute(create_table_query)

    # returning connection object
    return conn_obj


# Method to insert data
def insert_data(conn1):
    # cursor object
    crsr = conn1.cursor()

    # Faker Object created
    obj_faker = Faker("en_CA")

    # Loop to handle insertions
    for int1 in range(200):
        person_id = int1 + 1
        person_name = obj_faker.first_name()
        person_email = obj_faker.ascii_email()
        person_address = obj_faker.address()
        person_city = obj_faker.city()
        person_province = obj_faker.administrative_unit()
        person_bio = obj_faker.sentence(nb_words=10)
        person_age = obj_faker.random_int(min=1, max=100)

        # Current system date and time
        person_created_at = datetime.now()

        # Current system date and time
        person_updated_at = datetime.now()

        # Insert Query
        insert_query = """ INSERT INTO people ( id, name, email, address, city, province, bio, age, created_at, updated_at ) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?); """

        # Setting the values in Query
        profile_obj = (person_id,
                       person_name,
                       person_email,
                       person_address,
                       person_city,
                       person_province,
                       person_bio,
                       person_age,
                       person_created_at,
                       person_updated_at)

        # Executing query to add new people data to table
        crsr.execute(insert_query, profile_obj)

        # Committing the changes
        conn1.commit()


# Create table method call
conn1 = create_table()

# Insert data method call
insert_data(conn1)

# closing the connection
conn1.close()
