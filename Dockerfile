FROM fedora:28

WORKDIR /RESTimage
COPY . /RESTimage
RUN pip3 install pipdeps/*
RUN yum install libstdc++.x86_64 -y
EXPOSE 5000
CMD ["python3", "imageCheck.py"] 
#, "$MODEL_NAME", "$BUCKET_NAME", "$MODEL_PATH"]