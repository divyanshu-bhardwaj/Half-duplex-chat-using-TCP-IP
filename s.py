import socket
server_port = 5000
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
connection_socket, address = server_socket.accept()
print ("Connection Established : ", address)
while True:
  sentence = connection_socket.recv(2048).decode()
  print('Client: ',sentence)
  message = input(">> ")
  connection_socket.send(message.encode())
  if(message == 'q'):
    connection_socket.close()