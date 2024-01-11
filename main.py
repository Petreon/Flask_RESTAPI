from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        # adding videos in the dictionary, taking the body with request
        print(request.form)
        # but we can do this using the reparser from the flask_restapi
    
api.add_resource(Video,"/video/<int:video_id>")






















# i wont use this animore, but i will leave them ----------
names = {"tim":{"age":19,"gender":"male"},
         "bill":{"age":21,"gender":"male"}}

class HelloWorld(Resource): ##putting Resource in the class we can use mtehod to handle requests in the class
    def get(self,name): ##we can access name from the <string:name> passed in the url
        #defining the get request of what would it return
        return {"name":name,
            "data":names[name],}
    
    def post(self,name,test):
        #defining result of post method
        return {"data":"Posted"}
    
## adding the class Helloworld with all methods with the route /helloworld
api.add_resource(HelloWorld, "/helloworld/<string:name>")

import hello2
api.add_resource(hello2.TestingHello, "/testing")

##### FINSHING TESTSSSSSSSSSSSSSSSSSSSSS ---------------------


## in this way we dont use the flask itself to initialize the server, it is inicialize when we call the main function
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
