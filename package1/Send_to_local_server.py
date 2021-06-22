import requests

from package1 import parsing_server1
from package1.parsing_server1 import parsing_GPIO_Sadok, parsing_GPIO_4relay, parsing_ESP
r4_0 = parsing_server1.parsing_GPIO_4relay()
r4_1 = str(r4_0[0])
r4_2 = str(r4_0[1])
r4_3 = str(r4_0[2])
r4_4 = str(r4_0[3])
print('r4_2= ' + r4_2)
# param_4relay = parsing_GPIO_4relay()
params = {'params': str(parsing_ESP()), 'params1': str(parsing_GPIO_Sadok()), 'params2_1': str(r4_2), 'params2_2': str(r4_2), 'params2_3': str(r4_3), 'params2_4': str(r4_4), 'control': 'home'}

r = requests.get('http://localhost/test/index.php', params=params)
r.encoding = "UTF8"
print(r.text)