import sqlite3

class Crud:

    def __init__(self):
        self.connection = sqlite3.connect('tickets.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (ID INTEGER PRIMARY KEY, Prefix TEXT, Year INT, Ticket_ID INT)''')


    def read_all(self):
        self.cursor.execute('''SELECT * FROM tickets''')
        output = self.cursor.fetchall()
        return output


    def read_most_recent(self):
        self.cursor.execute('''SELECT * FROM tickets ORDER BY ID DESC LIMIT 1''')
        output = self.cursor.fetchone()
        return output


    def write(self, prefix, year, ticket_id):
        self.cursor.execute('''INSERT INTO tickets (Prefix, Year, Ticket_ID) VALUES (?,?,?)''', (prefix, year, ticket_id))
        self.connection.commit()
    

    def search(self, prefix, year, ticket_id):
        self.cursor.execute('''SELECT * FROM tickets WHERE Prefix = (?) and Year = (?) and Ticket_ID = (?)''', (prefix, year, ticket_id))
        output = self.cursor.fetchall()
        return output


    def close(self):
        self.connection.close()


def main():
    mydb = Crud()
    #mydb.write("aaa", 2024, 1114)
    #mydb.read_most_recent()
    print(mydb.read_all())
    print(mydb.search("aaa", 2024, 1114))
    mydb.close()


if __name__ == "__main__":
    main()
