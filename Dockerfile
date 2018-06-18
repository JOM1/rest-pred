FROM fedora:28

RUN pip3 install pillow keras flask boto3 numpy tensorflow flask_restful
COPY . /RESTimage
WORKDIR /RESTimage
CMD ["python3", "imageCheck.py"]
EXPOSE 5000
