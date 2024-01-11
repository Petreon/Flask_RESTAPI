from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

#importing flask_sqlalchemy to persist data
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self,name=name,views=views,likes=likes) -> str:
        return f"video (name = {name}, views = {views}, likes = {likes})"


## if the database isnt create the db.create_all() will create on for us, but if its create it wont do nothing
with app.app_context():
    db.create_all()

## this is used to validate if all inputs in the put are what we are expecting
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str,help="Name of the video not send", required=True) ## help i what return if dont send the video name
video_put_args.add_argument("likes", type=int,help="Likes of the video not send", required=True)
video_put_args.add_argument("views", type=int,help="Views of the video not send", required=True) 

#have better ways to do this, but i will stay with that
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str,help="Name of the video not send", )
video_update_args.add_argument("likes", type=int,help="Likes of the video not send", )
video_update_args.add_argument("views", type=int,help="Views of the video not send", )


resource_fields = {
    #serializing the data getting from de database to give a correctly response
    'id':fields.Integer,
    'name':fields.String,
    'views':fields.Integer,
    'likes':fields.Integer
}

class Video(Resource):
    #a way to serialize the data do return the response
    @marshal_with(resource_fields) # serialize the result with resource_fields
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()

        if not result:
            abort(404,message=f"Video with id = {video_id} not found")
        # we need to serialize the result that is an instance of VideoModel

        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        # but we can do this using the reparser from the flask_restapi
        args = video_put_args.parse_args()
        #print(args)
        result = VideoModel.query.filter_by(id=video_id).first()

        if result:
            ## aborting if already have an result in the database
            abort(409, message=f"video with id = {video_id} already exists")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video,201 ## 201 response to created, 200 is to okay
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,f"Video with id = {video_id} not found")
        
        #have better ways to do this to
        if args["name"] is not None:
            result.name = args["name"]
        if args["views"] is not None:
            result.views = args["views"]
        if args["likes"] is not None:
            result.likes = args["likes"]
        
        db.session.add(result) # this not need but i will stay
        db.session.commit()

    
        return result

    
    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()

        if not result:
            abort(404,f"Video with id = {video_id} not found")

        db.session.delete(result)
        db.session.commit()

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
