DSC478FinalProject

David Beck
Rob Weddell

Final Project for DePaul University DSC478: Machine Learning


Movie recommender system using the movielens.com dataset

Main.py is the main script and runs the text interface

Engine.py is responsible for calculating similarities

MovieData.py handles the data


Create a docker container using this command:

    docker build -t movierecommender


Run the application with:

    docker run -ti movierecommender