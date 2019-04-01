FROM python:3.7-alpine

COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD 'hug -f main.py'