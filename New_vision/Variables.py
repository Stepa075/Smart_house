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
parsing_GPIO_4relay_0 = r1
parsing_GPIO_4relay_1 = r2
parsing_GPIO_4relay_2 = r3
parsing_GPIO_4relay_3 = r4
GPIO_sad_on = 'http://192.168.0.100/gpio?st=0&pin=0'
GPIO_sad_off = 'http://192.168.0.100/gpio?st=1&pin=0'
GPIO_sad_flag = 2
GPIO_4relay1_on = 'http://192.168.0.120/gpio?st=1&pin=0'
GPIO_4relay1_off = 'http://192.168.0.120/gpio?st=0&pin=0'
GPIO_4relay2_on = 'http://192.168.0.120/gpio?st=1&pin=2'
GPIO_4relay2_off = 'http://192.168.0.120/gpio?st=0&pin=2'
GPIO_4relay3_on = 'http://192.168.0.120/gpio?st=1&pin=5'
GPIO_4relay3_off = 'http://192.168.0.120/gpio?st=0&pin=5'
GPIO_4relay4_on = 'http://192.168.0.120/gpio?st=1&pin=14'
GPIO_4relay4_off = 'http://192.168.0.120/gpio?st=0&pin=14'
GPIO_4Relay1_flag = 2
GPIO_4Relay2_flag = 2
GPIO_4Relay3_flag = 2
GPIO_4Relay4_flag = 2

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
time_start = 0
time_now = datetime.now().strftime("%H:%M:%S")
time_for_program_start = ''
current_time = 0
URL = ''
Response_URl = ''

# pump variables:
gerkon_down = '0'
gerkon_up = '0'
gerkon_alarm = '0'
status = 'Updating...'
Position_relay1_on_off = '0'
Position_relay2 = '0'
Position_relay3_alarm = '0'

counting_requaest = 0
counting_requaest_stand_by = 0
time_request_per_hour = 0
time_request_per_hour_stand_by = 0