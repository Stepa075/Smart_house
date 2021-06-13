import parsing_server1
from parsing_server1 import ESP_Light_Sensor

def logicks_Sadok_Light():
       if ESP_Light_Sensor <=100:
           print('Night')
       else:
           print('Day!')
