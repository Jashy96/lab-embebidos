import socket
import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)
PinEntrada=16
PinSalida=29
GPIO.setup(PinEntrada,GPIO.IN)
GPIO.setup(PinSalida,GPIO.OUT,initial=0)

TCP_IP = '172.32.149.207'
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
                GPIO.output(PinSalida,1)
                time.sleep(1)
                print("Pin en Alto")
                print ("received data:", m)               
        else:
                print("NO VERDE",data)
                GPIO.output(PinSalida,0)
                time.sleep(1)
                print("Pin en Bajo")
        print(col)
        conn.send(data)  # echo
GPIO.cleanup()
conn.close()
