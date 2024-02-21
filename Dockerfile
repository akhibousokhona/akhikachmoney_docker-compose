FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

RUN mkdir /connexion
WORKDIR /connexion
COPY ./connexion /connexion

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

USER user
EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "connexion.wsgi"]
