from flask import Flask, render_template, url_for, request, render_template
import math
from verify import verificationProcess
app = Flask(__name__)
from database_mock import Database


# Input for the main page which the user will see. 
@app.route("/")
def index():
    DropdownOptions = get_options()
    NumberOfItems = get_number_of_items()
    return render_template('index.html',options=DropdownOptions, options1 = NumberOfItems)

@app.route("/", methods=["POST"])
def input():
    Booking : dict = {}
    errors : list = []
    Booking["Email"] :str= request.form["email"]
    Booking["FirstName"] :str= request.form["first_name"]
    Booking["LastName"] :str= request.form["last_name"]
    Booking["PhoneNumber"] : str = request.form["phone_number"]
    Booking["SocialSecurityNumber"] :str= request.form["person_number"]
    
    if("-" in Booking["SocialSecurityNumber"]):
        Booking["SocialSecurityNumber"]= Booking["SocialSecurityNumber"].replace("-","",1)
    if(len(Booking["SocialSecurityNumber"]) == 12):
        Booking["SocialSecurityNumber"] = Booking["SocialSecurityNumber"][2:]
    
    verification(Booking,errors)
    if(errors == [None]):
        dropdown_options : list = get_options()
        print(Booking)
        return render_template("index.html", options=dropdown_options,options1 = get_number_of_items())
    else:
        # Something went wrong, ie. errors have something inside it. 
        # Content will be printed to the terminal and error page will show
        print(errors)
        return render_template('error.html', Foo = errors)

@app.route('/', methods=['GET'])
def dropdown():
    return render_template('index.html', options=dropdown_options)

@app.route('/error.html')
def error(errors : list):
    return render_template('error.html', Foo = errors)

# Admin page and various pages connected too it. 
# Admin lent out shows the borrowed equipment
# Admin Returned shows the available bookings and the options to return them early

# ADMIN MAIN PAGE
@app.route("/admin.html")
def go_admin():
    return render_template('admin.html')

# ADMIN CURRENTLY LENT OUT EQUIPMENT
@app.route("/admin_lent_out.html")
def go_admin_lent_out():
    return render_template('admin_lent_out.html', Foo = get_lent_out_dict())

# ADMIN AVAILABLE EQUIPMENT
@app.route("/admin_equip.html")
def go_admin_avail_equip():
    return render_template('admin_equip.html', Foo = get_equip_dict())

# ADMIN RETURNED
@app.route("/admin_returned.html")
def go_admin_returned():
    return render_template('admin_returned.html', equip_lent = clean_equip_dict(get_lent_out_dict()))

@app.route("/admin_returned.html", methods = ['POST'])
def go_admin_input():
    a = request.form["dropdown"]
    print(a)
    return render_template('admin_returned.html', equip_lent = clean_equip_dict(get_lent_out_dict()))

# HELP FUNCTIONS TO CREATE FAKE DATA
# !!! TEMPORARY !!!

# Retrive list of available things from SQL
def get_options() -> list:
    return ["VR headset", "Pybrick", "Phone", "hotchip"]

def verification(Booking_request : dict, errors : list = []) -> list:
    verifier = verificationProcess()
    verifier.verify_phone_number(Booking_request["PhoneNumber"], errors)
    verifier.verify_person_number(Booking_request["SocialSecurityNumber"], errors)
    verifier.verify_email(Booking_request["Email"], errors)
    return errors

def get_equip_dict():
    ass :dict = {"name":"Pybricks", "ID" : 1, "Short description":"Short desscription","Amount":3}
    ass1 :dict = {"name":"VR", "ID" : 2, "Short description":"Short desscription2","Amount":1}
    return [ass1,ass]

def get_number_of_items() ->list:
    return ["1", "2", "4", "5", "7"]

def get_lent_out_dict() -> list:
    return[{"ID":"12354","Name":"Pybrick","Kategori": 2, "Description":"Short description","BookedAmount": 6},{"ID":"12354","name":"Pybrick","Kategori": 2, "Description":"Short description","BookedAmount": 6},{"ID":"154","name":"Phone","Kategori": 12, "Description":"Short descriptio231n","BookedAmount": 5},{"ID":"12354","name":"Pybrick","Kategori": 2, "Description":"Short description","BookedAmount": 6}, {"ID":"12354","name":"Pybrick","Kategori": 2, "Description":"Short description","BookedAmount": 6},{"ID":"12354","name":"Pybrick","Kategori": 2, "Description":"Short description","BookedAmount": 6}]

def clean_equip_dict(equip : list)-> list:
    list_of_equip : list =[]
    for i in range(len(equip)):
        list_of_equip.append("")

        curr : dict = equip[i]
        for x in curr:
            list_of_equip[-1] = " " +  list_of_equip[-1] + x + " : " + str( equip[i][x]) + " "
    return list_of_equip

# MAIN
if __name__ == "__main__":
    app.run(debug=True)

