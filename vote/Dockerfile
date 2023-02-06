# Using official python runtime base image
FROM python:3-slim

# Set the application directory
WORKDIR /src

RUN ls -lah /usr/local/lib/python3.11/site-packages
RUN pip install --upgrade pip || ls -lah /usr/local/lib/python3.11/site-packages 

# Install our requirements.txt
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /src

# Make port 8080 available for links and/or publish
EXPOSE 8080

# Define our command to be run when launching the container
CMD ["python", "app.py"]
