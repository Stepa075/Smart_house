import requests


def parsing_server_response():

  global lines
  try:
    url = "http://f0555107.xsph.ru/hello.html"
    r = requests.get(url)
    r.encoding = "UTF8"
    print('r.text = ' + r.text)
    with open('response_server.html', 'w') as output_file:
      output_file.write(r.text)
    with open('response_server.txt', 'w') as output_file:
      output_file.write(r.text)

    text_file = open("response_server.html", "r")
    lines = text_file.read().split(',')
    print(lines)
    print(lines[0])
    print(len(lines))
    text_file.close()


  except:
    lines.append('0')

    pass

  return lines

def change_side():
  if parsing_server_response()[6] =='home':
    print('No changes')
  else:
    print('outside')





# if __name__ == "__main__":
#   parsing_server_response()
#   change_side()