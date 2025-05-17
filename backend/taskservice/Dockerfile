FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8003
CMD ["python","manage.py","runserver","0.0.0.0:8003"]