## testing the main.py with request module

import requests, json

BASEurl = "http://127.0.0.1:5000/" ## location of the API

data = [{"name":"first_video","likes":10,"views":1000},
        {"name":"second_video","likes":10324,"views":100430},
        {"name":"third_video","likes":1023,"views":100210}]


for i in range(0,3):
    Video_response = requests.put(BASEurl + f"videos/{i+1}", json=data[i])
    ## putting the json attribute we set the header for application/json
    print(Video_response.json())
    print(Video_response.status_code)


for i in range(0,4):
    Video_response = requests.get(BASEurl + f"videos/{i+1}")
    print(Video_response.json())
    print(Video_response.status_code)

#for i in range(0,3):
#    Video_response = requests.delete(BASEurl + f"videos/{i+1}")
#    print(Video_response)
    #in delete methods we dont response any json data only the status code
    #print(Video_response.status_code)

Video_response = requests.patch(BASEurl + "videos/1", json={"likes":999, "name":"new_video1"})
print(Video_response.status_code)
data = Video_response.text
data_json = json.loads(data)
print(data_json)


# testing delete
Video_response = requests.delete(BASEurl + "videos/2")
print(Video_response.text)
print(Video_response.status_code)














#Dont use this anymore --------------------------------------------

#response = requests.get(BASEurl + "helloworld/bill")
#response1 = requests.post(BASEurl + "helloworld/aslas/1")
#responsepaulo = requests.get(BASEurl + "testing")
#responsepaulo1 = requests.post(BASEurl + "testing")

#print(response.json())
#print(response1.json())
#print(responsepaulo.json())
#print(responsepaulo1.json())

