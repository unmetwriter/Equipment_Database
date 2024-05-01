from flask import Flask, render_template, url_for
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')

class Equipment(Resource):
    
    def get(self,number):
        return {number:"Hello world"}
class Booking_Request(Resource):
    def get(self,social_security_number):
        return 200
api.add_resource(Equipment,"/Equipment/<int:number>") 
if __name__ =="__main__":
    app.run(debug=True)

