## testing the main.py with request module

import requests

BASEurl = "http://127.0.0.1:5000/" ## location of the API

Video_response = requests.put(BASEurl + "video/1", json={"name":"first_video","likes":10,"views":1000})
## putting the json attribute we set the header for application/json
print(Video_response.json())
print(Video_response.status_code)

input()

Video_response = requests.get(BASEurl + "video/2")
print(Video_response.json())

















#Dont use this anymore --------------------------------------------

#response = requests.get(BASEurl + "helloworld/bill")
#response1 = requests.post(BASEurl + "helloworld/aslas/1")
#responsepaulo = requests.get(BASEurl + "testing")
#responsepaulo1 = requests.post(BASEurl + "testing")

#print(response.json())
#print(response1.json())
#print(responsepaulo.json())
#print(responsepaulo1.json())

