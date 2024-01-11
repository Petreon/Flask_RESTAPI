from flask_restful import Resource

#only testing if i can create resources outside the main

class TestingHello(Resource):
    def get(self):
        return {"data":"retornado Paulo"}
    def post(self):
        return {"data":"Post Paulo"}