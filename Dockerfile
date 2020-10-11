FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
RUN python manage.py migrate --noinput
RUN python manage.py loaddata members.json courses.json

# admin:password
RUN python manage.py create_admin

#CMD python manage.py runserver 0.0.0.0:8000
