import serial

PORT = '/dev/tty.usbserial-A1014R97'
SPEED = 9600

def send_int(val):
  connection = serial.Serial(PORT, SPEED, timeout=0, stopbits=serial.STOPBITS_TWO)
  connection.write(val)
  connection.close()

print "Stopped."
send_int("90")
