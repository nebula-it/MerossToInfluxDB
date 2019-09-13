# To build the container
1. Clone the repository, 
```
git clone https://github.com/nebula-it/MerossToInfluxDB.git
```
2. Change directory to "MerossToInfluxDB/"
```
cd MerossToInfluxDB/
```
3. Build using docker
```
docker build -t merossinflux:1.0 .
```
4. You image is ready now with tag "meross:1.0"
5. Start a container using this image, use the following docker run command:
```
docker run -d -e EMAIL=yourMerossAccountEmail \
-e PASSWORD=yourMerossAccountPassword \
-e InfluxDB_Host=10.10.10.5 \
-e DBName=Meross \ 
-e InfluxDB_Port=8086 \
--restart on-failure \
meross:1.0
```

### NOTE

InfluxDB_Host defaults to 'localhost' if not provided in docker run command. InfluxDB_Port defaults to 8086.
