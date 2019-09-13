# MerossToInfluxDB
Docker Container to gather stats from Meross cloud and send it to influxdb instance.

This is based on the work done by https://github.com/albertogeniola

I needed something simple to poll Meross devices and get the stats in InfluxDB. This is my very first attempt at dockerizing something so any feedback is welcome.

# Start Container
Use the command below to start the container or use attached docker-compose file
```
docker run -d -e EMAIL=yourMerossAccountEmail \
-e PASSWORD=yourMerossAccountPassword \
-e InfluxDB_Host=10.10.10.5 \
-e DBName=Meross \ 
-e InfluxDB_Port=8086 \
--restart on-failure \
nebulait/merossinflux
```
