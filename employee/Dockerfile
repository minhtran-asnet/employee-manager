FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

ADD ./requirements /code/requirements
RUN pip install -r /code/requirements/test.txt
RUN groupadd -r django \
    && useradd -r -g django django

ADD . /code
COPY ./runserver.sh /runserver.sh

RUN chown -R django /code
RUN chmod +x /runserver.sh

WORKDIR /code

EXPOSE 8000
