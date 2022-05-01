FROM python:3.10.3
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/ 
EXPOSE 8000
CMD gunicorn src.CourseStore.wsgi --log-file -