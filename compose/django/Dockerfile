FROM python:3.6

RUN mkdir /src
RUN mkdir /static

WORKDIR /src

RUN apt-get update && apt-get install -y gettext libgettextpo-dev zlib1g libjpeg-dev

RUN pip install --upgrade pip

COPY ./src/requirements.txt /scripts/
RUN pip install --no-cache-dir -r /scripts/requirements.txt

CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py migrate; python manage.py runserver 0.0.0.0:8000"]