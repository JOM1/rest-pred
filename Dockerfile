FROM fedora:28

WORKDIR /RESTimage
#RUN 
RUN yum install git -y ; git clone https://github.com/JOM1/flask-pred.git /RESTimage
RUN pip3 install pipdeps/*
EXPOSE 5000
CMD ["python3", "imageCheck.py"] 
#, "$MODEL_NAME", "$BUCKET_NAME", "$MODEL_PATH"]