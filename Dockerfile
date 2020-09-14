FROM jupyter/datascience-notebook

USER root
RUN mkdir /src
RUN mkdir /task-for-hiring-data

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD python lib/run.py