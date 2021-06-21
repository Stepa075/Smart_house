import requests

from package1.parsing_server1 import parsing_GPIO_Sadok, parsing_GPIO_4relay, parsing_ESP

# param_4relay = parsing_GPIO_4relay()
params = {'params': str(parsing_ESP())}
r = requests.get('http://ochre-propulsion.000webhostapp.com/index.php', params=params)
r.encoding = "UTF8"
print(r.text)