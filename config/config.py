import logging
import time
import mysql.connector
from mysql.connector import errorcode

# Dictionary of all specified tables
TABLES = {}
ALTER_DICT= {}
config_dict = {
    'user':'root',
    'password':'1234',
    'host':'localhost',
    'database':'dv1663'}

TABLES['students']= ("CREATE TABLE IF NOT EXISTS students("
"SocialSecurityNumber varchar(13) NOT NULL,"
"FirstName varchar(50) NOT NULL,"
"LastName varchar(50) NOT NULL,"
"Email varchar(100) NOT NULL,"
"PhoneNumber varchar(50) NOT NULL,"
"PRIMARY KEY (SocialSecurityNumber)"
")")

TABLES['types']= ("CREATE TABLE IF NOT EXISTS types("
"TypeId int NOT NULL AUTO_INCREMENT,"
"Name varchar(50) NOT NULL,"
"Description varchar(255) NOT NULL,"
"PRIMARY KEY (TypeId)"
")")

TABLES['equipment']= ("CREATE TABLE IF NOT EXISTS equipment("
"EquipmentId int AUTO_INCREMENT NOT NULL ,"
"Name varchar(50) NOT NULL,"
"TypeId int NOT NULL,"
"Description varchar(250) NOT NULL,"
"TotalNumberItems int NOT NULL,"
"PRIMARY KEY (EquipmentId)"
")")

TABLES['requests']= ("CREATE TABLE IF NOT EXISTS requests("
"RequestId int NOT NULL AUTO_INCREMENT,"
"SocialSecurityNumber varchar(13) NOT NULL,"
"EquipmentId int NOT NULL,"
"NumberOfItems int NOT NULL,"
"StartDate varchar(10) NOT NULL,"
"EndDate varchar(10) NOT NULL,"
"PRIMARY KEY (RequestId),"
"FOREIGN KEY (SocialSecurityNumber) REFERENCES students(SocialSecurityNumber),"
"FOREIGN KEY (EquipmentId) REFERENCES equipment(EquipmentId)"
")")

TABLES['bookings']= ("CREATE TABLE IF NOT EXISTS bookings("
"BookingId int NOT NULL AUTO_INCREMENT,"
"SocialSecurityNumber varchar(13) NOT NULL,"
"EquipmentId int NOT NULL,"
"NumberOfItems int NOT NULL,"
"StartDate varchar(10) NOT NULL,"
"EndDate varchar(10) NOT NULL,"
"PRIMARY KEY (BookingId),"
"FOREIGN KEY (SocialSecurityNumber) REFERENCES students(SocialSecurityNumber),"
"FOREIGN KEY (EquipmentId) REFERENCES equipment(EquipmentId)"
")")
ALTER_DICT['types']=(
    "ALTER TABLE types RENAME COLUMN Name to Category")
ALTER_DICT['equipment']=(
    "ALTER TABLE equipment RENAME COLUMN Name to Item,RENAME COLUMN TotalNumberItems to TotalQuantity"
    )
ALTER_DICT['bookings']= (
    "ALTER TABLE bookings ADD ReturnDate varchar(10),RENAME COLUMN NumberOfItems to Quantity"
    )
def set_up_log():
    """Returns a logger which logs messages in the terminal and in a file. Logger is used in the connect() method to log all connection attempts.
    See link for more details: https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html"""
    # Set up logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Log to console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log to a file
    file_handler = logging.FileHandler("log/cpy-errors.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler) 
    return logger
def connect(config,attempts=10,delay=2):
    """Connects to the database specified in the config dictionary, provided that the database is available, returns the connection object.
       Expects a config dictionary with credentials to connect to the database, a integer that specifies how many attempts should be done if a connection is unsuccessful, and a integer specifying the delay between attempts in seconds.
       See link for more details: https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    """
    logger= set_up_log() 
    attempt = 1
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            print("Connection Successful")
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError) as err:
            if (attempts is attempt):
                # Attempts to reconnect failed; returning None
                logger.info("Failed to connect, exiting without a connection: %s", err)
                return None
            logger.info(
                "Connection failed: %s. Retrying (%d/%d)...",
                err,
                attempt,
                attempts-1,
            )
            time.sleep(delay ** attempt)   # progressive reconnect delay
            attempt += 1


    return None


def create_tables(cursor):
    """Creates all tables, provided that it recieves a correct cursor-object for executing sql-code 
    """
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
                print(err.msg)
        else:
            print("OK")
def alter_tables(cursor):
    for table_name in ALTER_DICT:
        table_change = ALTER_DICT[table_name]
        try:
            print("Altering column {}:".format(table_name),end='')
            cursor.execute(table_change)
        except mysql.connector.Error as err:
                print(err.msg)
        else:
            print("Ok")
    
if __name__ == "__main__": 
    database=connect(config_dict,10,1)
    if (database !=0):
        cursor = database.cursor()
    create_tables(cursor)
    alter_tables(cursor)
    cursor.close()
    database.close()