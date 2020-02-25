FROM python:3.7
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

# update apt-get
RUN apt-get update -y && apt-get upgrade -y

# Install Nodejs
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs

# install aws-cli
RUN pip install awscli

# install boto3
RUN pip install boto3

# install serverless framework
RUN npm install -g serverless

# set aws key 
RUN sls config credentials --provider aws --key $AWS_ACCESS_KEY_ID --secret $AWS_SECRET_ACCESS_KEY

# change work directory
RUN mkdir -p /app
WORKDIR /app/app