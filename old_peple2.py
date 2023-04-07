import pandas as panda_obj
import sqlite3


def fetchdata():
    # connecting with DB
    conn_obj = sqlite3.connect('social_network.db')

    # cursor object
    cursor_obj = conn_obj.cursor()

    # query to fetch data
    query = 'SELECT name,age FROM people where age >= 50 LIMIT 200'

    # fetching data
    cursor_obj.execute(query)

    # fetchall method to get all the rows
    data_set = cursor_obj.fetchall()

    # using for loop
    for element in data_set:
        name, age = element
        print(f" {name} is {age} years old. ")

    # changes committed
    conn_obj.commit()
    conn_obj.close()
    return data_set


def create_csv(data_set_temp):
    # dataframe obj and use of Pandas
    people_data_frame = panda_obj.DataFrame(data_set_temp, columns=['Name', 'Age'])
    people_data_frame.to_csv('lab_7.csv', index=False)


# Fetching the data
data_set = fetchdata()

# Method to create CSV file
create_csv(data_set)
