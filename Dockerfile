FROM python:latest

WORKDIR /app/
copy . /app/

#RUN python3 -m pip install -r requirements.txt
RUN pip install uvicorn
RUN pip install fastapi
CMD uvicorn --host=0.0.0.0 --port 8080 main:app
