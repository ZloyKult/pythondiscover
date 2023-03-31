from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)

api = Api()

courses = {"Name": "New line", "Number": 113, "Id": 942}

class Main(Resource):
    def get(self):
        return courses

api.add_resource(Main, "/api/courses")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="192.168.32.114")


