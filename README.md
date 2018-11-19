FIND - A - FILM

David Beck
Rob Weddell

Final Project for DePaul University DSC478: Machine Learning


Movie recommender system using the movielens.com dataset

Main.py is the main script and runs the text interface

Engine.py is responsible for calculating similarities

MovieData.py handles the data


Build time was approx. 90 seconds (though we saw as high as 4 minutes)
Create a docker container using this command:


    docker build -t findafilm


Startup time was approx 20 seconds
Run the application with:


    docker run -ti findafilm
