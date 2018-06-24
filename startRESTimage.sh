#!/bin/bash
sudo docker kill restpred
sudo docker rm restpred
sudo docker image rm restpred_img
sudo docker build -t restpred_img .
#sudo docker run -d -e "MODEL_NAME=$1","BUCKET_NAME=$2","MODEL_PATH=$3" -p 5000:5000 --name restpred restpred_img
sudo docker run -d -p 5000:5000 -e MINIO_IP=172.17.0.2 --name restpred restpred_img
#sudo docker run -it restpred_img bash
