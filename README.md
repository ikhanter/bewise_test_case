### BEWISE.IO TEST CASE


#### TASK

1. Using Docker (preferably docker-compose), deploy an image from any open source DBMS (preferably PostgreSQL). Provide all the necessary scripts and configuration (docker/compose) files for deploying the DBMS, as well as instructions for connecting to it. It is necessary to ensure the safety of data when restarting the container (that is, use volumes to store DBMS files on the host machine.

2. Implement a simple web service in Python3 (using FastAPI or Flask, for example) that performs the following functions:
The service must implement a REST API that accepts POST requests with content like {"questions_num": integer}.
After receiving the request, the service, in turn, requests from the public API (English questions for quizzes) https://jservice.io/api/random?count=1 the number of questions specified in the received request. Next, the received answers must be saved in the database from step 1. At least the following information must be saved (you can choose the names of the columns and data types yourself, you can also add your own columns): 1. Question ID, 2. Question text, 3. Answer text, 4. Date the question was created. If there is the same question in the database, additional requests must be made to the public quiz API until a unique question for the quiz is received.
The answer to the request from step 2.a must be the previous saved question for the quiz. If it is absent, it is an empty object.

3. The repository with the task must contain instructions for assembling a docker image with the service from step 2., configuring it and launching it. And also an example of a request to the POST API of the service.

4. It is advisable if, when performing the task, you use docker-compose, SqlAalchemy, and use type annotations.


#### REQUIREMENTS

- OS Linux;
- Docker;
- Docker Compose.


#### INSTALLATION

1. Use command
    ```git clone git@github.com:ikhanter/bewise_test_case.git```
    for cloning the repo to your locak machine.
2. Use command
    ```docker-compose build```
    for building image of the project.
3. Use command
    ```docker-compose up```
    for creating and launching the container of the image and
    ```docker-compose down```
    for stopping of the container.


#### USAGE

- Send POST-request to ```localhost:5000``` with ```Content-Type: application/json``` and request body ```{"questions_num": <number>}```, where ```<number>``` is ```integer```-type value. For example: ```curl -X POST -H "Content-Type: application/json" -d '{"questions_num": <number>}' http://localhost:5000```
- ```<number>``` means how much questions will be added to the DB. Despite of limiting of amount of questions for one request as 100 by ```jservice.io```'s API, the possibility to add more questions for one request is realized.
- DB save its own data on the host machine and keeps it between container running.