#!/bin/bash
sudo docker kill restpred
sudo docker rm restpred
sudo docker image rm restpred_img
sudo docker build -t restpred_img .
sudo docker run -d -p 5000:5000 --name restpred restpred_img
