# create a database for stock data
import mysql.connector

class StockDB:
    def __init__(self, db_name):
        self.db_name = db_name

    def sql_init(self, host="localhost", user="aaron", password="aaron12457AARON"):
        # create a connection
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        # create a cursor
        self.mycursor = self.mydb.cursor()
        # create a database
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS " + self.db_name)
        # select database
        self.mycursor.execute("USE " + self.db_name)

    def import_csv(self, csv_file):
        # check if
        pass


# if main,test mysql connection
if __name__ == '__main__':
    mydb = mysql.connector.connect(
    host="localhost",
    user="aaron",
    password="aaron12457AARON"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

    # select database mydatabase
    mycursor.execute("USE mydatabase")

    # create a test table
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

    # insert three records
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [ ('Peter', 'Lowstreet 4'),
            ('Amy', 'Apple st 652'),
            ('Michael', 'Valley 345')
            ]
    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")

    # select all records
    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

