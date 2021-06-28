# import gc
# from time import sleep
#
# import requests
# import threading
# from package1_copy.Testing import Variables
#
# class check_conn
# def check_Light_sensor_conections():
#       a=1
#       while a==1:
#             try:
#               rl = requests.get('http://192.168.0.110/')
#               print('status_code Light_sensor_connection: ' + str(rl.status_code))
#               if int(rl.status_code) == 200:
#                   x = 1
#                   # root.after(0, xxx)
#                   rl.close()
#                   lbl_Light_sensor['text'] = 'Light sensor status: Connected, Ok'
#               else:
#                   x = 2
#                   lbl_Light_sensor['text'] = 'Light sensor status: Disconnected, Error'
#                   rl.close()
#
#             except:
#                 print('except! Light sensor')
#                 lbl_Light_sensor['text'] = 'Light sensor status: Error!'
#                 pass
#
#             sleep(3)
#
# def xxx():
#     try:
#         xxx1 = Variables.parsing_ESP
#         lbl_gen_fr_1_value['text'] = xxx1
#         lbl_gen_fr_2_value['text'] = xxx1
#         del xxx1
#         print('xxx')
#         gc.collect()
#         root.after(3000, xxx)
#     except:
#         lbl_gen_fr_1_value['text'] = 'Fucking ERROR!!!'
#         pass
#         gc.collect()
#         # root.after(3000, xxx)
#     sleep(3.0)
#
# def parser_GPIO_sadok():
#     try:
#
#             xxx1 = Variables.Sadok_Light
#
#             if int(xxx1) == 0:
#                 lbl_gen_fr3_1_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_1_value['text'] = "OFF"
#             del xxx1
#             print('parser_GPIO_sadok')
#     except:
#         lbl_gen_fr3_1_value['text'] = 'No connect to ESP!'
#         pass
#     gc.collect()
#     sleep(3.0)
#
#
# def parser_GPIO_4relay():
#     try:
#             if int(Variables.parsing_GPIO_4relay_0) != 0:
#                 lbl_gen_fr3_3_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_3_value['text'] = "OFF"
#             if int(Variables.parsing_GPIO_4relay_1) != 0:
#                 lbl_gen_fr3_4_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_4_value['text'] = "OFF"
#             if int(Variables.parsing_GPIO_4relay_2) != 0:
#                 lbl_gen_fr3_5_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_5_value['text'] = "OFF"
#             if int(Variables.parsing_GPIO_4relay_3) != 0:
#                 lbl_gen_fr3_6_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_6_value['text'] = "OFF"
#             print('parser_GPIO_4relay')
#             gc.collect()
#     except:
#         lbl_gen_fr3_3_value['text'] = 'Fucking ERROR!!!'
#         lbl_gen_fr3_4_value['text'] = 'Fucking ERROR!!!'
#         lbl_gen_fr3_5_value['text'] = 'Fucking ERROR!!!'
#         lbl_gen_fr3_6_value['text'] = 'Fucking ERROR!!!'
#         pass
#     finally:
#         gc.collect()
#         sleep(3.0)
#
#
# def check_req():
#     try:
#         # r = requests.get('https://google.com/')  # резервный ('http://httpbin.org/get')
#         # print('check_reg ' + str(r.status_code))
#         xxx1=Variables.status_code_check_req
#         if Variables.status_code_check_req == 200:
#             lbl_Internet_sensor['text'] = 'Internet sensor status: Connected, Ok'
#             print('check_reg')
#         else:
#             lbl_Internet_sensor['text'] = 'Internet sensor status: Disconnected, Error!'
#             print('check_reg')
#         gc.collect()
#         # root.after(3000, check_req)
#     except:
#         print('except! Internet')
#         lbl_Internet_sensor['text'] = 'Internet sensor status: Error!'
#         pass
#     finally:
#         gc.collect()
#         sleep(3.0)
#
#
# def check_Server_sensor_conections():
#     try:
#         rg = requests.get("http://f0555107.xsph.ru/")  # резервный ('http://httpbin.org/get')
#         print('check server ' + str(rg.status_code))
#         if int(rg.status_code) == 200:
#             lbl_Server_sensor['text'] = 'Server sensor status: Connected, Ok'
#         else:
#             lbl_Server_sensor['text'] = 'Server sensor status: Disconnected, Error!'
#         rg.close()
#         del rg
#     except:
#         print('except! Server')
#         lbl_Server_sensor['text'] = 'Server sensor status: Error!'
#         pass
#     gc.collect()
#     sleep(3.0)
#
#
# def update_time():
#     # change text on Label
#     lbl_time['text'] = time.strftime('Current date: %Y-%m-%d Current time: %H:%M:%S')
#
#     run `update_time` again after 1000ms (1s)
#     sleep(1.0)  # function name without ()
#
#
# check_Light_sensor_conections()