import requests
import parsing_server1



def logicks_Sadok_Light():
       try:
           if int(parsing_server1.parsing_ESP()) <=100:
              url='http://192.168.0.100/gpio?st=0&pin=0'
              requests.get(url)
              print('Night')
           else:
               url = 'http://192.168.0.100/gpio?st=1&pin=0'
               requests.get(url)
               print('Day!')

       except:
           pass


def logicks_4relay_Light():
    try:
        if int(parsing_server1.parsing_ESP()) <= 100:
            url = 'http://192.168.0.120/gpio?st=1&pin=0'
            requests.get(url)
            url = 'http://192.168.0.120/gpio?st=1&pin=2'
            requests.get(url)
            url = 'http://192.168.0.120/gpio?st=1&pin=14'
            requests.get(url)
            url = 'http://192.168.0.120/gpio?st=1&pin=5'
            requests.get(url)

            print('4Relay Night')
        else:
            url = 'http://192.168.0.120/gpio?st=0&pin=0'
            requests.get(url)
            url = 'http://192.168.0.120/gpio?st=0&pin=2'
            requests.get(url)
            url = 'http://192.168.0.120/gpio?st=0&pin=14'
            requests.get(url)
            url = 'http://192.168.0.120/gpio?st=0&pin=5'
            requests.get(url)

            print('4 Relay Day!')

    except:
        pass


def get_URL(URL):
    try:
        url = URL
        r = requests.get(url)
        r.encoding = "UTF8"
        with open('response.txt', 'w') as output_file:
          output_file.write(r.text)

        f = open('response.txt')
        response=f.read()
        f.close()
        return response
    except:
        return None
        pass
