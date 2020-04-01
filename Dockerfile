FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
RUN apk add --update --no-cache py3-numpy
ENV PYTHONPATH=/usr/lib/python3.7/site-packages
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt