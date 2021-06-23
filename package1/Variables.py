from package1.Recive_on_server import parsing_server_response
from package1.Send_to_server import send_to_server


# def get_variables():
#     global send_to_server_res
#     global response_to_server_res
#     global str1
#     send_to_server_res = send_to_server()
#     response_to_server_res = parsing_server_response()
str1=10
def seter():
    global str1
    str1 = str1*2*15
    # global str1
# send_to_server_res = "_"
# response_to_server_res="_"
seter()
print(str(str1))







if __name__ == "__main__":
    # get_variables()
    seter()
