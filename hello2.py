from flask_restful import Resource

class TestingHello(Resource):
    def get(self):
        return {"data":"retornado Paulo"}
    def post(self):
        return {"data":"Post Paulo"}