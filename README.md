# DSC478FinalProject

Final Project for DePaul University DSC478: Machine Learning. 

Movie recommender system using the movielens.com dataset

Main.py is the main script

We run this from Docker with

docker build -t movierecommender

docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw movierecommender
