import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)
PinEntrada=8
PinSalida=29
GPIO.setup(PinEntrada,GPIO.IN)
GPIO.setup(PinSalida, GPIO.OUT,initial=0)
try:
          while(True):
                if GPIO.input(PinEntrada):
                        GPIO.output(PinSalida,1)
                        time.sleep(1)
                        print("Pin en Alto")
                else:
                        GPIO.output(PinSalida,0)
                        time.sleep(1)
                        print("Pin en Bajo")
except KeyboardInterrupt:
         GPIO.cleanup()
print("Exiting...")


