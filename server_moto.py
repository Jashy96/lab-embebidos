import socket

TCP_IP = '172.32.150.98'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
        col = " "
        data = conn.recv(BUFFER_SIZE)
        m = str(data)
        col = m[2:len(m)-1]
        col = col.lower()
        if not data: break
        if col == "verde":
                print ("received data:", m)               
        else:
                print("NO VERDE",data)

        print(col)
        conn.send(data)  # echo
conn.close()
