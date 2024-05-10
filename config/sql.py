
import mysql.connector
from mysql.connector import errorcode
import config

config_dict = {
    'user':'root',
    'password':'1234',
    'host':'localhost',
    'database':'dv1663'}
def add_student(student_data,cursor):
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
    add_student = ("INSERT INTO students "
                   "(SocialSecurityNumber,FirstName,LastName,Email,PhoneNumber) "
                   "VALUES (%(social_security_number)s,%(first_name)s,%(last_name)s,%(email)s,%(phone_number)s)")
    try:
        cursor.execute(add_student,student_data)
    except mysql.connector.Error as err:
        return err
    
    cursor.close()
    return 1
    
def add_equipment(equipment_data):
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
    add_equipment = ("INSERT INTO equipment "
                   "(Name,TypeId,Description,TotalNumberItems) "
                   "VALUES (%(name)s,%(type_id)s,%(description)s,%(total_number_items)s)")
    try:
        cursor.execute(add_equipment,equipment_data)
    except mysql.connector.Error as err:
        return err
    
    cursor.close()
    return 1
    
def add_request(request_data):
    add_request = ("INSERT INTO requests "
                   "(RequestId,SocialSecurityNumber,EquipmentId,NumberOfItems,StartDate,EndDate) "
                   "VALUES (%(social_security_number)s,%(equipment_id)s,%(number_of_items)s,%(start_date)s,%(end_date)s)")
    try:
        cursor.execute(add_request,request_data)
    except mysql.connector.Error as err:
        return err
    cursor.close()
    return 1
    
def add_booking(booking_data):
    add_booking = ("INSERT INTO requests "
                   "(BookingId,SocialSecurityNumber,EquipmentId,NumberOfItems,StartDate,EndDate) "
                   "VALUES (%(social_security_number)s,%(equipment_id)s,%(number_of_items)s,%(start_date)s,%(end_date)s)")
    try:
        cursor.execute(add_booking,booking_data)
    except mysql.connector.Error as err:
        return err
    cursor.close()
    return 1
    
def remove_request(request_id):
    pass
def remove_booking(booking_id):
    pass
def update_return_date(booking_id,return_date):
    pass
def get_available_items(cursor):
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
def get_items_by_category(type_id,cursor):
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
def get_bookings():
    pass
def get_inactive_bookings():
    pass
def get_active_bookings():
    pass
def get_overdue_bookings():
    pass
database=config.connect(config_dict,10,1)
if (database !=0):
    cursor = database.cursor()
    # print(get_available_items(cursor))
    print(get_items_by_category(2,cursor))

