# A Django application to test the CI/CD pipeline
This repository contains the source code for the Django application that is designed to work in conjunction with [the AWS CDK Django infrastructure project](https://github.com/ndhoanit1112/django-cicd-aws-cdk).

This application is basically an application that calculates Fibonacci numbers using a background task setup with Celery.

## Prerequisites
Before getting started with this project, ensure that you have the following prerequisites:
* Docker (https://docs.docker.com/get-docker/)
* Docker Compose (https://docs.docker.com/compose/install/)

## Some Main Files:
* `buildspec_{env}.yml`: The build specification file for AWS CodeBuild. It defines the build steps and environment for building the Django application.
* `Dockerfile`: The Dockerfile for creating the Docker image of the Django application and Celery service.
* `nginx/Dockerfile`: The Dockerfile for creating the Docker image of the nginx server.
* `docker-compose.yml`: The Docker Compose file for running the Django application locally along with its dependencies (e.g., database).
* `.env`: The environment file containing environment variables for the Django application, incase you want to run the application locally. (Have a look at the `.env.example.` file for a referrence and create an `.env` file yourself).

## Integration with AWS CDK Django Project
Before using this repository, make sure you have already built and deployed the infrastructure using [the AWS CDK Django project](https://github.com/ndhoanit1112/django-cicd-aws-cdk). The AWS CDK project provisions the necessary AWS resources to deploy this Django application.
Once the infrastructure is ready, try making changes in the `develop` and `master` of this project to test the pipeline and the deployment.

This Django application is basically an application for calculating Fibonacci numbers, it includes a background task setup with Celery to perform the Fibonacci calculation.

## Running the Application Locally:
To run the Django application locally using Docker and Docker Compose:
1. Modify the .env file to configure the environment variables for the Django application. Update the variables with your own values.
2. Run the following command to start the application:
```bash
docker-compose up -d
```
This command will start the Django application and its dependencies (e.g., database and Celery worker) defined in the docker-compose.yml file.
3. Access the application in your web browser at http://localhost:8000/fibs/.
