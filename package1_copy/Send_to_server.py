import requests

from package1.parsing_server1 import parsing_GPIO_Sadok, parsing_GPIO_4relay, parsing_ESP
def send_to_server():
 try:
  r4_0 = parsing_GPIO_4relay()
  r4_1 = str(r4_0[0])
  r4_2 = str(r4_0[1])
  r4_3 = str(r4_0[2])
  r4_4 = str(r4_0[3])
  print('r4_2= ' + r4_2)
  # param_4relay = parsing_GPIO_4relay()
  params = {'params': str(parsing_ESP()), 'params1': str(parsing_GPIO_Sadok()), 'params2_1': str(r4_2), 'params2_2': str(r4_2), 'params2_3': str(r4_3), 'params2_4': str(r4_4), 'control': 'home'}

  r = requests.get('http://f0555107.xsph.ru/index.php', params=params)
  r.encoding = "UTF8"
  print(r.text)
 except:
  params = {'params': '0', 'params1': '0', 'params2_1': '0',
            'params2_2': '0', 'params2_3': '0', 'params2_4': '0', 'control': 'home'}
  r = requests.get('http://f0555107.xsph.ru/index.php', params=params)
  r.encoding = "UTF8"
  print(r.text)
  pass
