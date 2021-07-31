from datetime import datetime
from time import sleep

seichas = datetime.now()
while True:
    delta = datetime.now() - seichas
    print(delta)
    # print(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
    sleep(1.0)
