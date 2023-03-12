# base image used to build the image
FROM python:3.7-alpine

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .
COPY app.py ./src/
COPY templates/index.html ./src/templates/

# update pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# command to run on container start
CMD ["python3", "src/app.py"]