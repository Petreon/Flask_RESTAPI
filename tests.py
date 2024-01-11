## testing the main.py with request module

import requests

BASEurl = "http://127.0.0.1:5000/" ## location of the API

Video_response = requests.put(BASEurl + "video/1", {"likes":10})


















#Dont use this anymore --------------------------------------------

#response = requests.get(BASEurl + "helloworld/bill")
#response1 = requests.post(BASEurl + "helloworld/aslas/1")
#responsepaulo = requests.get(BASEurl + "testing")
#responsepaulo1 = requests.post(BASEurl + "testing")

#print(response.json())
#print(response1.json())
#print(responsepaulo.json())
#print(responsepaulo1.json())

