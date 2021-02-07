import socket
server_name = 'localhost'
server_port = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_name,server_port))

while True:
  sentence = input(">> ")
  client_socket.send(sentence.encode())
  message = client_socket.recv(2048)
  print ("Server: ", message.decode())
  if(sentence == 'q'):
    client_socket.close()