import os
import datetime
import pymysql

# Get username Github workspace
username = os.getenv('https://github.com/kris965')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE Name in ({});".format(format_strings),
            list_of_names)

        connection.commit()

finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
