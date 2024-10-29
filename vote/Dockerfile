# Using official python runtime base image
FROM python:3-slim AS base

ARG TEST_ENV_VAR
# ENV TEST_ENV_VAR=$TEST_ENV_VAR
# Set the application directory
WORKDIR /src

RUN touch newfile.txt
RUN echo $TEST_ENV_VAR
# RUN echo "Testing env variable: $TEST_ENV_VAR" > newfile.txt
RUN pip install --upgrade pip

# Install our requirements.txt
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /src

FROM base AS buld
ARG TEST_ENV_VAR
ENV APP_NAME="myapp/${TEST_ENV_VAR}"

WORKDIR /src
RUN echo ${APP_NAME}
RUN echo "Testing env variable: ${APP_NAME}" > newfile.txt
# Make port 8080 available for links and/or publish
EXPOSE 8080
RUN echo "Test logging 1"
RUN echo "Test logging 2"
RUN echo "Test logging 3"
RUN echo "Test logging 4"
RUN echo "Test logging 5"
RUN echo "Test logging 6"
RUN echo "Test logging 7"
RUN echo "Test logging 8"
RUN echo "Test logging 9"
RUN echo "Test logging 10"
RUN echo "Test logging 11"
# Define our command to be run when launching the container
CMD ["python", "app.py"]
