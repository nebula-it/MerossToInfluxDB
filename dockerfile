FROM python:3-alpine

WORKDIR /usr/src/app/meross

RUN apk add git &&\
    apk add curl &&\
    apk add nano &&\
    git clone https://github.com/albertogeniola/MerossIot.git &&\
    cd ./MerossIot &&\
    python ./setup.py install
ENV EMAIL=**None** \
    PASSWORD=**None** \
    InfluxDB_Host=localhost \
    InfluxDB_Port=8086 \
    DBName=**None**

COPY ./getMerossStats.py /usr/src/app/meross
## - u used for unbuffered output, so python output is written to Docker log, see: https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker
ENTRYPOINT [ "python","-u", "./getMerossStats.py" ]
