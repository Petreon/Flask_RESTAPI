# Flask_RESTAPI
Creating a Flaks REST API to learn new concepts about it
This is a simple API that you can do a full CRUD of name,views and likes for video

## Routes for the API
- GET method, /videos/int:videoid , get the data of video if exists

- PUT method, /videos/int:videoid , with the json of your video {"name":"example","views":integer,"likes":integer}

- PATCH method, /videos/int:videoid , with the json of your video {"name":"example","views":integer,"likes":integer}
    in this method you dont need to pass all parameters it will only changes what you put

- DELETE method, /videos/int:videoid , delete the video if exists

you can see methods examples in the tests.py file

## How to install
1. First create an venv for the application
- $ python3 -m venv venv

2. Clone the application
- $ git clone https://github.com/Petreon/Flask_RESTAPI.git

3. Install the dependencies
- $ pip3 install -r requirements.txt

4. Start the enviroment
- $ source venv/bin/activate

5. Start the server
- $ python3 main.py <br>
    attention: if you want to deploy it, turn off the debug mode