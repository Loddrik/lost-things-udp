FROM python:3.6-stretch
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD [ "bash","runallservices.sh" ]