FROM qgis/qgis:latest
ENV CACHEBUSTER=123

MAINTAINER Denis Rouzaud <denis@opengis.ch>

RUN curl https://bootstrap.pypa.io/get-pip.py | python3
RUN pip3 install sphinx requests 

COPY NED_Reference/ /NED_Reference
COPY data/ /data
COPY . /

RUN chmod 777 -R ./NED_Reference
RUN chmod 777 -R ./data


ENTRYPOINT ["python3", "dem.py"]
