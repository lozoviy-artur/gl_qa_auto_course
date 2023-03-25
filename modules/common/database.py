import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('/Users/arturlozovyi/Desktop/gl_qa_auto_course' + '/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "Select sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connection successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return  record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalcode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

