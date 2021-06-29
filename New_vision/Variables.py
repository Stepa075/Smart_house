from datetime import datetime

send_to_server = ''
receive_from_server = []
receive_from_server1 = 0
receive_from_server2 = 0
receive_from_server3 = 0
receive_from_server4 = 0
receive_from_server5 = 0
receive_from_server6 = 0
receive_from_server7 = 'home'
Sadok_Light = 1
parsing_ESP = 110
r1 = '0'
r2 = '0'
r3 = '0'
r4 = '0'
parsing_GPIO_4relay = [r1, r2, r3, r4]
parsing_GPIO_4relay_0 = parsing_GPIO_4relay[0]
parsing_GPIO_4relay_1 = parsing_GPIO_4relay[1]
parsing_GPIO_4relay_2 = parsing_GPIO_4relay[2]
parsing_GPIO_4relay_3 = parsing_GPIO_4relay[3]
GPIO_sad_on = 'http://192.168.0.100/gpio?st=0&pin=0'
GPIO_sad_off = 'http://192.168.0.100/gpio?st=1&pin=0'

GPIO_4relay1_on = 'http://192.168.0.120/gpio?st=1&pin=0'
GPIO_4relay1_off = 'http://192.168.0.120/gpio?st=0&pin=0'
GPIO_4relay2_on = 'http://192.168.0.120/gpio?st=1&pin=2'
GPIO_4relay2_off = 'http://192.168.0.120/gpio?st=0&pin=2'
GPIO_4relay3_on = 'http://192.168.0.120/gpio?st=1&pin=5'
GPIO_4relay3_off = 'http://192.168.0.120/gpio?st=0&pin=5'
GPIO_4relay4_on = 'http://192.168.0.120/gpio?st=1&pin=14'
GPIO_4relay4_off = 'http://192.168.0.120/gpio?st=0&pin=14'

response_flag = ['0', '0', '0', '0', '0', '0', 'sleep']
response_flag_1 = ''
response_flag_2 = ''
response_flag_3 = ''
response_flag_4 = ''
response_flag_5 = ''
response_flag_6 = ''
response_flag_7 = ''

parsing_ESP1 = 110
parsing_GPIO_4relay1 = [r1, r2, r3, r4]
Sadok_Light1 = 1

status_code_light_sensor = 0
status_code_sadok = 0
status_code_4relay = 0
status_code_check_req = 0
status_code_server_connections = 0
time_now = datetime.now().strftime("%H:%M:%S")
URL = ''
Response_URl = ''
