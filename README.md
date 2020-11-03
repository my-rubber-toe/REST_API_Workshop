# REST_API_Workshop

## Pre-requisites
1. Install `python3.8+`
2. Install git
3. Install docker

## Navigating the Workshop

This repository is divided into multiple branches. Each branch represents a step on the workshop. Branches are set as `lesson-#` where # is the number of the lesson.

## Setting Repository

1. Clone the respository using `git clone`. 
2. Change your directory to the downloaded repository.
3. (Optional) Create a python virtual environment using `python -m venv venv`.
    - Access your virtual environment by running:
        - Linux: `source ./venv/bin/activate`
        - Windows: `.\venv\Scripts\Activate`
5. Install all the required packages by running `pip install -r requirements.txt`.

## Running Database and Database UI

For this workshop we will be using containers to create a database and a database user interface.

Make sure that you have docker installed in your operating system. For details on how to install Docker follow this link [here](https://docs.docker.com/desktop/).

NOTE: Make sure that you have **Windows10 version 1903** or higher to use Docker on Windows.
NOTE: For Ubuntu OS use the following link: [Docker Install on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Once you have docker installed on your machine, run `docker-compose up -d`. This will create two containers in the background, one for our database and one for our database user interface.
