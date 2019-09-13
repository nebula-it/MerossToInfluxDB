from meross_iot.manager import MerossManager
from meross_iot.meross_event import MerossEventType
from meross_iot.cloud.devices.light_bulbs import GenericBulb
from meross_iot.cloud.devices.power_plugs import GenericPlug
from meross_iot.cloud.devices.door_openers import GenericGarageDoorOpener
import time
import os
import requests

## Get Env variables from docker
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
Influxdb_Host = os.getenv('InfluxDB_Host')
Influxdb_Port = os.getenv('InfluxDB_Port')
Influxdb_DBName = os.getenv('DBName')

if __name__=='__main__':
    # Initiates the Meross Cloud Manager. This is in charge of handling the communication with the remote endpoint
    manager = MerossManager(meross_email=EMAIL, meross_password=PASSWORD)

    # Starts the manager
    manager.start()

    # You can retrieve the device you are looking for in various ways:
    # By kind
    plugs = manager.get_devices_by_kind(GenericPlug)
    # Can be retreived by name as well
    #plug = manager.get_device_by_name("SM847")

    # gather data from Meross cloud
    while True:
        for plug in plugs:
            if not plug.online:
                print("The plug %s seems to be offline. Cannot retreive stats for it." % plug.name)
                continue
            if plug.supports_electricity_reading():
                PowerData = (plug.get_electricity())
                p_name = (plug.name)
                p_current = (PowerData['current'])
                p_voltage = (PowerData['voltage'])
                p_power = (PowerData['power'])
                #Send data to Influxdb using HTTP
                url = "http://{0}:{1}/write?db={2}".format(Influxdb_Host,Influxdb_Port,Influxdb_DBName)
                data = "Current,plug={0} value={1}\nVoltage,plug={0} value={2}\nPower,plug={0} value={3}".format(p_name,p_current,p_voltage,p_power)
                response = requests.post(url=url, data=data)
                print(response)
        time.sleep(30)
