import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))



# GET http://www.dr-chuck.com/page1.htm HTTP/1.0
