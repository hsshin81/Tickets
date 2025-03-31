import mysql.connector
import datetime

def gen_tickets(count, ticket_type):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="tickets"
    )
    mycursor = db.cursor()


    for i in range(count):
        
        mycursor.execute("SELECT number FROM records WHERE id=(SELECT MAX(id) FROM records);")
        prevticket = mycursor.fetchall()[0][0]
        newticket = str(int(prevticket)+1).zfill(8)
        
        sql = "INSERT INTO records (prefix, number, date) VALUES (%s, %s, %s)"
        x = datetime.datetime.now()
        mydate = x.strftime("%x %X")

        match ticket_type:
            case 1:
                myprefix="AAA"
            case 2:
                myprefix="BBB"
            case 3:
                myprefix="CCC"

        val = (myprefix, newticket, mydate)
        mycursor.execute(sql, val)
        db.commit()
        # return myprefix, newticket


    db.close()



def main():
    ticket_type = input("What kind of ticket? 1-AAA, 2-BBB, 3-CCC ")
    count = input("How many tickets: ")
    gen_tickets(int(count), int(ticket_type))


if __name__ == "__main__":
    main()