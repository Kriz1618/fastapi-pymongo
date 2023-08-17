# MongoDB FastAPI Exmaple
Basic API using FastAPI and MongoDB **[based on](https://morioh.com/p/fd31220b32ec?f=5c21fb01c16e2556b555ab32)**

## Install
```
	python -m pip install -r requirements.txt
```

## Steps
* Create virtual environment
	```
	pyenv virtualenv 3.10.10 env
	```
* Activate the environment
	```
	pyenv activate env
	```
* Install modules
	```
	pip install pymongo fastapi uvicorn python-dotenv pipreqs
	```
* Freeze modules in the requirements.txt
	```
	pipreqs --force
	```
* Start server
	```
	uvicorn main:app --reload
	```
* Visualize docs by open the [url](http://127.0.0.1:8000/docs)


## Dockerize the app
* Create the DockerFile with all the configurations
* Create the docker-compose.yml file with the container configuration
* Start the container
	```
	docker-compose -up -d
	```
* Stop the container
	run the command `docker-compose stop` or `docker stop {container_name}`
* Rebuild image an container
	```
	docker-compose up --build
	```
