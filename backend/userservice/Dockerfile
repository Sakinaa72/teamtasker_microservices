FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8002
CMD ["python","manage.py","runserver","0.0.0.0:8002"]