from flask import Flask
from flask_restful import Api, Resource
import hello2

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource): ##putting Resource in the class we can use mtehod to handle requests in the class
    def get(self,name): ##we can access name from the <string:name> passed in the url
        #defining the get request of what would it return
        return {"data":"Hello World"}
    
    def post(self):
        #defining result of post method
        return {"data":"Posted"}
    
## adding the class Helloworld with all methods with the route /helloworld
api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(hello2.TestingHello, "/testing")

## in this way we dont use the flask itself to initialize the server, it is inicialize when we call the main function
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
