from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

## this is used to validate if all inputs in the put are what we are expecting
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str,help="Name of the video not send", required=True) ## help i what return if dont send the video name
video_put_args.add_argument("likes", type=int,help="Likes of the video not send", required=True)
video_put_args.add_argument("views", type=int,help="Views of the video not send", required=True) 


videos = {}


def handle_video_get_exists(video_id):
    if video_id not in videos:
        ## this is the correct way to handle
        abort(404, message=f"video {video_id} does not exists")

def handle_video_put_exists(video_id):
    if video_id in videos:
        abort(409, message=f"video {video_id} already exists")
        ## 409 is for an content is already created


class Video(Resource):
    def get(self, video_id):
        handle_video_get_exists(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        # adding videos in the dictionary, taking the body with request
        #print(request.form)
        # but we can do this using the reparser from the flask_restapi
        handle_video_put_exists(video_id)
        args = video_put_args.parse_args()
        #print(args)
        videos[video_id] = args
        return videos[video_id],201 ## 201 response to created, 200 is to okay
    
    def delete(self, video_id):
        handle_video_get_exists(video_id)
        #print(videos)
        del videos[video_id]
        #print(videos)
        return {"data":f"video {video_id} removed"}, 204
    
api.add_resource(Video,"/videos/<int:video_id>")






















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
