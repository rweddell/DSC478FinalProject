FIND - A - FILM

David Beck
Rob Weddell

Final Project for DePaul University DSC478: Programming Machine Learning Applications


Movie recommender system using the movielens.com dataset

    F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context.
    ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1â€“19:19.
    https://doi.org/10.1145/2827872

    https://www.kaggle.com/rounakbanik/the-movies-dataset/home

Main.py is the main script and runs the text interface

Engine.py is responsible for calculating recommendations

MovieData.py handles the data


Build time was approx. 90 seconds (though we saw as high as 4 minutes)
Create a docker container using this command:


    docker build -t findafilm .


Startup time was approx 20 seconds
Run the application with:


    docker run -ti findafilm


Download the docker image from:

    https://hub.docker.com/r/rweddell/findafilm/

Command:

    docker pull rweddell/findafilm
