
import mysql.connector
from mysql.connector import errorcode
import config

config_dict = {
    'user':'root',
    'password':'1234',
    'host':'localhost',
    'database':'dv1663'}
def add_student(student_data,database):
    """ Expects a dictionary with details about the student, as well as a cursor object to execute sql-code.
        Adds a student to the database and closes the cursor object afterwards.
        
        Example format of dictionary: 
        student_data = {
        'social_security_number': '00-00-00-0000'
        'first_name':'John'
        'last_name':'Doe'
        'email':'somemail@gmail.com'
        'phone_number':'0700-00-00-00'
        }
    For more details about implementation: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
    """
    cursor=database.cursor()
    add_student = ("INSERT INTO students "
                   "(SocialSecurityNumber,FirstName,LastName,Email,PhoneNumber) "
                   "VALUES (%(social_security_number)s,%(first_name)s,%(last_name)s,%(email)s,%(phone_number)s)")
    try:
        cursor.execute(add_student,student_data)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    cursor.close()
    database.commit()
    return 1
    
def add_equipment(equipment_data,database):
    """ Expects a dictionary with details about an piece of equipment, as well as a cursor object to execute sql-code.
        Adds equipment to the database and closes the cursor object afterwards. Returns an error message if something goes wrong.
        
        Example format of dictionary: 
        equipment_data = {
        'name': 'Raspberry Pi',
        'type_id':1,
        'description': 'A One chip computer',
        'total_number_items': 15
        }
    For more details about implementation: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
    """
    cursor=database.cursor()
    add_equipment = ("INSERT INTO equipment "
                   "(Name,TypeId,Description,TotalNumberItems) "
                   "VALUES (%(name)s,%(type_id)s,%(description)s,%(total_number_items)s)")
    try:
        cursor.execute(add_equipment,equipment_data)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    
    cursor.close()
    database.commit()
    return 1
    
def add_request(request_data,database):
    cursor=database.cursor()
    add_request = ("INSERT INTO requests "
                   "(SocialSecurityNumber,EquipmentId,Quantity,StartDate,EndDate) "
                   "VALUES (%(social_security_number)s,%(equipment_id)s,%(quantity)s,%(start_date)s,%(end_date)s)")
    try:
        cursor.execute(add_request,request_data)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    cursor.close()
    database.commit
    return 0
    
def add_booking(booking_data,database):
    cursor= database.cursor()
    add_booking = ("INSERT INTO requests "
                   "(BookingId,SocialSecurityNumber,EquipmentId,NumberOfItems,StartDate,EndDate) "
                   "VALUES (%(social_security_number)s,%(equipment_id)s,%(number_of_items)s,%(start_date)s,%(end_date)s)")
    try:
        cursor.execute(add_booking,booking_data)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    cursor.close()
    database.commit()
    return 1
    
def remove_request(database,request_id):
    cursor=database.cursor()
    delete_query = "DELETE FROM requests WHERE RequestId= {request_id}".format(request_id=request_id)
    cursor = database.cursor()
    try:
        cursor.execute(delete_query)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    cursor.close()
    database.commit
    return 0
def remove_booking(database,booking_id):
    cursor=database.cursor()
    delete_query = "DELETE FROM bookings WHERE BookingId= {booking_id}".format(booking_id=booking_id)
    cursor = database.cursor()
    try:
        cursor.execute(delete_query)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    cursor.close()
    database.commit
    return 0
def update_return_date(database,booking_id,return_date):
    cursor = database.cursor()
    update_booking_return_date = ("UPDATE bookings SET ReturnDate ='{return_date}' WHERE BookingId ={booking_id}".format(return_date=return_date,booking_id=booking_id))
    try:
        cursor.execute(update_booking_return_date)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    cursor.close()
    database.commit()
    return 0
def get_requests(database):
    cursor=database.cursor()
    requests= []
    select_requests = ("SELECT RequestId,requests.SocialSecurityNumber,FirstName,LastName,Email,PhoneNumber,EquipmentId,Item,Quantity,StartDate,EndDate FROM ((requests INNER JOIN students USING(SocialSecurityNumber)) INNER JOIN equipment USING(EquipmentId))")
    try:
        cursor.execute(select_requests)
        for (request_id,social_security_number,first_name,last_name,email,phone_number,equipment_id,item,quantity,start_date,end_date) in cursor:
            # print("\tItem: "+item,"\tCategory: "+category,"\tDescription: "+description,"\tQuantity: "+str(available_quantity))
            current_item= {
            "RequestId":request_id,
            "SocialSecurityNumber":social_security_number,
            "FirstName":first_name,
            "LastName":last_name,
            "Email":email,
            "PhoneNumber":phone_number,
            "EquipmentId":equipment_id,
            "Item":item,
            "Quantity":quantity,
            "StartDate":start_date,
            "EndDate":end_date,
            }
            requests.append(current_item)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    
    cursor.close()
    return requests
def get_available_items(database):
    cursor=database.cursor()
    select_active_bookings= ("SELECT Item,Category,Description,AvailableQuantity FROM available_items")
    active_items=[]
    try:
        cursor.execute(select_active_bookings)
        for (item,category,description,available_quantity) in cursor:
            # print("\tItem: "+item,"\tCategory: "+category,"\tDescription: "+description,"\tQuantity: "+str(available_quantity))
            current_item= {
                "Item":item,
                "Category":category,
                "Description":description,
                "Available Quantity":available_quantity
            }
            active_items.append(current_item)
        return active_items
    except mysql.connector.Error as err:
        cursor.close()
        return err
def get_booked_items(database):
    """Returns a list of dictionaries containing items which are currently booked. 
        If the query cannot be executed, an error is returned instead"""
    cursor=database.cursor()
    booked_items_query = "SELECT * FROM booked_items"
    try:
        cursor.execute(booked_items_query)
        booked_items=[]
        for(equipment_id,item,category,description,booked_quantity) in cursor:
            current_item = {
                "ItemId":equipment_id,
                "Item":item,
                "Category":category,
                "Description":description,
                "BookedQuantity":booked_quantity
            }
            booked_items.append(current_item)
    except mysql.connector.Error as err:
        cursor.close()
        return err
    cursor.close()
    return booked_items
def get_items_by_category(type_id,database):
    cursor=database.cursor()
    category_query= "call items_in_category({id})".format(id=type_id)
    category_items=[]
    try:
        cursor.execute(category_query)
        for (item,category,description,available_quantity) in cursor:
            # print("\tItem: "+item,"\tCategory: "+category,"\tDescription: "+description,"\tQuantity: "+str(available_quantity))
            current_item= {
                "Item":item,
                "Category":category,
                "Description":description,
                "Available Quantity":available_quantity
            }
            category_items.append(current_item)
        cursor.close()
        return category_items
    except mysql.connector.Error as err:
        cursor.close()
        return err
def get_inactive_bookings(database):
    cursor=database.cursor()
    inactive_bookings_query = "SELECT * FROM bookings_view WHERE EndDate <CURRENT_DATE()"
    try:
        cursor.execute(inactive_bookings_query)
        inactive_bookings = append_booking_query_data(cursor)
        return inactive_bookings    
    except mysql.connector.Error as err:
        cursor.close()
        return err
def get_active_bookings(database):
    cursor=database.cursor()
    overdue_bookings_query = "SELECT * FROM active_bookings"
    overdue_bookings = []
    try:
        cursor.execute(overdue_bookings_query)
        overdue_bookings =append_booking_query_data(cursor)
        return overdue_bookings
    except mysql.connector.Error as err:
        cursor.close()
        return err
    
def get_overdue_bookings(database):
    cursor=database.cursor()
    overdue_bookings_query = "SELECT * FROM bookings_view WHERE ReturnDate IS NULL AND EndDate <CURRENT_DATE()"
    try:
        cursor.execute(overdue_bookings_query)
        overdue_bookings =append_booking_query_data(cursor)
        return overdue_bookings
    except mysql.connector.Error as err:
        cursor.close()
        return err
def append_booking_query_data(cursor):
    bookings_data = []
    for (booking_id,social_security_number,first_name,last_name,email,phone_number,equipment_id,item,quantity,start_date,end_date,return_date) in cursor:
            # print("\tItem: "+item,"\tCategory: "+category,"\tDescription: "+description,"\tQuantity: "+str(available_quantity))
        current_item= {
            "BookingId":booking_id,
            "SocialSecurityNumber":social_security_number,
            "FirstName":first_name,
            "LastName":last_name,
            "Email":email,
            "PhoneNumber":phone_number,
            "EquipmentId":equipment_id,
            "Item":item,
            "Quantity":quantity,
            "StartDate":start_date,
            "EndDate":end_date,
            "ReturnDate":return_date,
        }
        bookings_data.append(current_item)
    cursor.close()
    return bookings_data

database=config.connect(config_dict,10,1)
if (database !=0):
    cursor = database.cursor()
    #print(update_return_date(database,booking_id=5,return_date="2024-05-10"))
    
    # print(get_overdue_bookings(cursor))
    # cursor = database.cursor()
    # print(get_active_bookings(cursor))
    # cursor = database.cursor()
    # print(get_inactive_bookings(cursor))
    request_data = {
        "social_security_number":"06-01-02-0000",
        "equipment_id":5,
        "quantity":3,
        "start_date":"2024-05-15",
        "end_date":"2025-01-01"
    }
    print(add_request(request_data,database))
    print(get_requests(database))
