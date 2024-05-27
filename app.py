from flask import Flask, render_template, url_for, request, render_template
import math
import config.config
import config.sql
import mysql.connector
from datetime import datetime
import json 
from verify import verificationProcess
app = Flask(__name__)
def get_database():
    db =config.config.connect(config.config.config_dict)
    return db

database = get_database()

@app.route("/")
def index():
    dropdown_options = get_options()
    return render_template('index.html',options=dropdown_options)

@app.route("/", methods=["POST"])
def input():
    booking : dict = {}
    errors : list = []
    booking["Email"] :str= request.form["email"]
    booking["FirstName"] :str= request.form["first_name"]
    booking["LastName"] :str= request.form["last_name"]
    booking["SocialSecurityNumber"] :str= request.form["person_number"]
    booking["PhoneNumber"] : str = request.form["phone_number"]
    booking["StartDate"] = datetime.today().strftime('%Y-%m-%d')
    temp = datetime.today().strftime('%Y-%m-%d')
    temp = temp.replace("24","25",1)
    booking["EndDate"] = temp
    print(request.form["dropdown"])
    booking["EquipmentId"] = int(request.form["dropdown"][1]) 
    booking["Quantity"] = request.form["quantity"]

    verification(booking,errors)
    print(errors)
    if(errors == [None]):
        dropdown_options = get_options()
        print(booking)
        keys_to_include = {'SocialSecurityNumber', 'EquipmentId','Quantity','StartDate', 'EndDate'}
        keys_to_include_student = {'Email','FirstName','LastName','SocialSecurityNumber','PhoneNumber'}
        subset_dict = {k: booking[k] for k in keys_to_include}
        subset_student_dict= {k:booking[k] for k in keys_to_include_student}
        print(config.sql.add_student(subset_student_dict,database))
        print(config.sql.add_booking(subset_dict,database))
        return render_template("index.html", options=dropdown_options)
    else:
        return "Shits fucked"

@app.route('/', methods=['GET'])
def dropdown():
    return render_template('index.html', options=get_options())

@app.route("/admin.html")
def go_admin():
    return render_template('admin.html')

@app.route("/admin_borrowed.html")
def go_admin_borrowed():    
    return render_template('admin_borrowed.html', Foo = config.sql.get_booked_items(database))

@app.route("/admin_equip.html")
def go_admin_equip():
    return render_template('admin_equip.html', Foo = config.sql.get_available_items(database))

@app.route("/admin_lent_out.html")
def go_admin_requests():
    return render_template('admin_lent_out.html', Foo = config.sql.get_active_bookings(database))

@app.route('/admin_returned.html')
def go_admin_returned():
    return render_template('admin_returned.html', options = config.sql.get_active_bookings(database))

@app.route('/admin_returned.html', methods = ['POST'])
def get_return_data():
    print(type(request.form["dropdown"]))
    booking_dict = request.form["dropdown"]
    booking_id = booking_dict[14]
    if (booking_dict[15] != ','):
        booking_id = booking_id + booking_dict[15]
    booking_id = int(booking_id)

    #booking_dict=json.loads(booking_string)
    return_date = request.form["curr_date"]
    config.sql.update_return_date(database,booking_id,return_date)
    return render_template('admin_returned.html', options = config.sql.get_active_bookings(database))

@app.route('/admin_categories.html')
def go_admin_cats():
    db = get_database()
    categories_list = config.sql.get_categories(db)
    return(render_template('admin_categories.html', options = categories_list, foo = get_options()))

@app.route('/admin_categories.html', methods = ['POST'])
def select_cats():
    db = get_database()
    categories_list = config.sql.get_categories(database)
  
    a = request.form["dropdown"]
    print(a)
    return(render_template('admin_categories.html',options =categories_list ,foo=config.sql.get_items_by_category(int(a[1]),db)))
    # if a == "Saft":
    #     return(render_template('admin_categories.html', options = ["Saft", "kakor", "Hattar"], foo =["Yoo", "jordgub", "hallon"]))
    # if a == "kakor":
    #     return(render_template('admin_categories.html', options = ["Saft", "kakor", "Hattar"],foo =["biskvi", "tårta", "muffin"]))
    
    # if a == "Hattar":
    #     return(render_template('admin_categories.html', options = ["Saft", "kakor", "Hattar"], foo = ["Trilby", "fedora", "tophat"]))
# Retrive list of available things from SQL
def get_options():
    items = config.sql.get_available_items(database)
    if items == mysql.connector.Error:
        return 404
    item_names = []
    
    for item in items:
        item_names.append((item["ItemId"],item["Item"],item["AvailableQuantity"]))

    return item_names


def verification(booking_request : dict, errors : list) -> list:
    verifier = verificationProcess()
    verifier.verify_phone_number(booking_request["PhoneNumber"], errors)
    verifier.verify_person_number(booking_request["SocialSecurityNumber"], errors)
    return errors

def get_equip_dict():
    ass :dict = {"name":"Pybricks", "ID" : 1, "Short description":"Short desscription","Amount":3}
    ass1 :dict = {"name":"VR", "ID" : 2, "Short description":"Short desscription2","Amount":1}

    return [ass1,ass]

def get_number_of_items():
    return ["1", "2", "4", "5", "7"]

if __name__ == "__main__":
    app.run(debug=True)

