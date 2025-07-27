# Server

This is a server for serving my notes online.
Note, the server spins up docker containers for each user, so we don't wanna run it in docker container (we don't wanna spin a docker container from another docker container, it is possible to do so but not recommended). Instead we will create a python virtual environment, install all the requirements, then run the server.

To run first create your python venv on your server instance:

```
python3 -m venv venv
source venv/bin/activate
```

Then install all the requirements:
```
pip3 install -r requirements.txt
```
Then run the server in production.

```
gunicorn -w 4 -b 0.0.0.0:80 manage_containers_service:app
```

