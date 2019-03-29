import time
import board
import digitalio
import busio
import adafruit_lis3dh
import xlwt
import datetime
import os

# Hardware I2C setup. Use the CircuitPlayground built-in accelerometer if available;
# otherwise check I2C pins.
i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D6)  # Set to correct pin for interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_16_G
t = (time.strftime('%m_%d_%I_%M_'))

file = open((t+"file.txt"), "w")

print("Gathering acceleration data...")
timeout = time.time()+10

# Loop until 10s has passed
while True:
    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y, z.
    x, y, z = [value for value in lis3dh.acceleration]
    file.write("%0.5f %0.5f %0.5f\n" % (x, y, z))
    time.sleep(0.0013)
    if time.time()>timeout:
        break
