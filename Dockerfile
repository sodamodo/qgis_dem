# see https://docs.docker.com/docker-cloud/builds/advanced/
# using ARG in FROM requires min v17.05.0-ce
ARG QGIS_DOCKER_TAG=latest

FROM  qgis/qgis:${QGIS_DOCKER_TAG}
MAINTAINER Denis Rouzaud <denis@opengis.ch>

RUN curl https://bootstrap.pypa.io/get-pip.py | python3
RUN pip3 install sphinx

COPY NED_Reference/ /NED_Reference
COPY . /

RUN chmod 777 -R ./NED_Reference
RUN ls
RUN cd NED_Reference && ls

ENTRYPOINT ["python3", "dem.py"]
