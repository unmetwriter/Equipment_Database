from flask import Flask, render_template, url_for, request, render_template
import math
from verify import verificationProcess
app = Flask(__name__)


@app.route("/")
def index():
    dropdown_options = get_options()
    number_of_items = get_number_of_items()
    return render_template('index.html',options=dropdown_options, options1 = number_of_items)

@app.route("/", methods=["POST"])
def input():
    booking : dict = {}
    errors : list = []
    booking["email"] :str= request.form["email"]
    booking["name"] :str= request.form["first_name"]
    booking["name"] :str= booking["name"] + " " + request.form["last_name"]
    booking["personNumber"] :str= request.form["person_number"]
    booking["phoneNumber"] : str = request.form["phone_number"]
    verification(booking,errors)
    print(errors)
    if(errors == [None]):
        dropdown_options = get_options()
        print(booking)
        return render_template("index.html", options=dropdown_options,options1 = get_number_of_items())
    else:
        return "Shits fucked"

@app.route('/', methods=['GET'])
def dropdown():
    return render_template('index.html', options=dropdown_options)

@app.route("/admin.html")
def go_admin():
    return render_template('admin.html')

@app.route("/admin_borrowed.html")
def go_admin_borrowed():
    return render_template('admin_borrowed.html')

@app.route("/admin_equip.html")
def go_admin_equip():
    return render_template('admin_equip.html', Foo = get_equip_dict())

@app.route("/admin_lent_out.html")
def go_admin_requests():
    return render_template('admin_lent_out.html', Foo = get_equip_dict())

# Retrive list of available things from SQL
def get_options():
    return ["VR headset", "Pybrick", "Phone", "hotchip"]

def verification(booking_request : dict, errors : list) -> list:
    verifier = verificationProcess()
    verifier.verify_phone_number(booking_request["phoneNumber"], errors)
    verifier.verify_person_number(booking_request["personNumber"], errors)
    return errors

def get_equip_dict():
    ass :dict = {"name":"Pybricks", "ID" : 1, "Short description":"Short desscription","Amount":3}
    ass1 :dict = {"name":"VR", "ID" : 2, "Short description":"Short desscription2","Amount":1}
    return [ass1,ass]

def get_number_of_items():
    return ["1", "2", "4", "5", "7"]

if __name__ == "__main__":
    app.run(debug=True)
