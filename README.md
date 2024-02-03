# Car collection manager - project.
### This is an application that manages a collection of Car objects.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)


## General information
The purpose of this project is to present several
different patterns of good programming practices and
implement them in a simple web service application.

## Technologies Used
- Python 3.12
- Flask
- pytest
- Docker
- pipenv

## Features
- Flask framework used for web
- Included Postman json file with routes to import
- Implementation of abstract factory design pattern
- Tests for every project layer
- Basic form of web security - public key

## Setup
### Virtual Environment

Firstly run the following pipenv commands for virtual environment:

> pipenv shell

> pipenv install

### Tests
After setting up virtual environment it is crucial to run tests.
In order to do it, while in your project directory enter
the following command:
> pipenv run pytest

Here is a link to pytest coverage results(97%):

https://drive.google.com/drive/folders/1IoI7pbxZyOjlGx_QxCzqNAtW0h0Kyzj1?usp=drive_link

This step has to be done before setting up Docker. At this point 
all the tests should pass with a correct result.

### Docker
Next, it is time run the Docker Desktop and in your project directory 
type the following commands, for creating and running docker container:

> docker-compose up -d --build

For the logs to appear in console, enter:

> docker-compose logs -f

If you want to stop running container, while in the directory
enter command:

> docker-compose stop

### Postman
(Optional) Postman installation for easily running routes.
For the Flask routes, it is recommended to use Postman as it is much
easier and more intuitive than running routes from the browser.
This app has the routes already provided. All you have to do is import
the Postman json collection and run them in the desired order.

### Notes regarding security
There is a scheduler configured for this projects web app.
In order to run the scheduler, which is configured to delete
old or invalid tokens, you should run it as a separate process.
In order to do it, simply open new terminal (because this script 
must be run as a separate process) and enter the following command:

> pipenv run python cars_manager_app/web/remove_expired_tokens.py


## Usage
This project is being made for usage only as a standalone application 
and has no other use cases other than managing a collection of
Car objects.


## Project Status
Project is: in progress.

