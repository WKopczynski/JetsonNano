################ Based on UARTDemo by JetsonHacksNano

import time
import serial

# Inicjalizacja portu
SerialPort = serial.Serial(
    port = "/dev/ttyTHS1",
    baudrate = 115200,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    )
# 1 sekunda na zaladowanie
time.sleep(1)

# Echo
try:
    SerialPort.write("Sup.".encode())
    while True:
        #if SerialPort.inWaiting() > 0:
            SendData = 'q'
            SerialPort.write(SendData.encode())
            ReceivedData = SerialPort.read()
            print(ReceivedData)
            if ReceivedData == "\r".encode():
                SerialPort.write("\n".encode())
            #time.sleep(1)
    

except KeyboardInterrupt:
    print("Bye.")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    SerialPort.close()
    pass
