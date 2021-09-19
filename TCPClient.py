import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET uses IPv4 adress and SOCK_STREAM is for tcp connection

client.connect(('10.0.2.15',9998)) #The target host and IP we want to connect to

client.send(b'\nHello server') #Message send to the server

response = client.recv(2300) #To receive some data back from the client

print(response.decode())
client.close()
