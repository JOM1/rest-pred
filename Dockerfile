FROM registry.access.redhat.com/rhscl/python-36-rhel7

WORKDIR /RESTimage
COPY . /RESTimage
RUN pip3 install pipdeps/*
EXPOSE 5000
CMD ["python3", "imageCheck.py"] 
#, "$MODEL_NAME", "$BUCKET_NAME", "$MODEL_PATH"]