FROM jupyter/tensorflow-notebook:hub-1.4.0
COPY ./requirements.txt  /home/jovyan/


RUN pip install -r /home/jovyan/requirements.txt