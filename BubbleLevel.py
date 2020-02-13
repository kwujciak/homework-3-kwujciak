# I worked with Sami Rothstein on the beginning (everything until def point_direction) during lab time.
# Kate Wujciak
import microbit
import random
import time
import math

print(microbit.accelerometer.get_x())

print(microbit.accelerometer.get_y())

print(microbit.accelerometer.get_z())

print(microbit.accelerometer.get_values())

x = microbit.accelerometer.get_x()
y = microbit.accelerometer.get_y()
z = microbit.accelerometer.get_z()

Ax = ((math.atan2(x,(math.sqrt((y**2)+(z**2)))))*180)/(math.pi)
Ay = ((math.atan2(y,(math.sqrt((x**2)+(z**2)))))*180)/(math.pi)
Az = ((math.atan2(z,(math.sqrt((x**2)+(y**2)))))*180)/(math.pi)

# while True:
#     time.sleep(1)
#     print((microbit.accelerometer.get_x(), microbit.accelerometer.get_y(), microbit.accelerometer.get_z(),))

def find_tilt_x(acc_x, acc_y, acc_z):
# This function defines the angle at which the microbit is tilted in the x direction in radians.
# It takes three parameters, acc_x, acc_y, acc_z, which are the values on each axis
# which microbit gives us from the reading on its accelerometer.
# It returns the angle at which the microbit is tilted in the x direction.
    tiltX=((math.atan2(acc_x,(math.sqrt((y**2)+(z**2)))))*180)/(math.pi)
    return tiltX

def find_tilt_y(acc_x, acc_y, acc_z):
# This function defines the angle at which the microbit is tilted in the u direction in radians.
# It takes three parameters, acc_x, acc_y, acc_z, which are the values on each axis of
# which microbit gives us from the reading on its accelerometer.
# It returns the angle at which the microbit is tilted in the y direction.
    tiltY=((math.atan2(acc_y,(math.sqrt((x**2)+(z**2)))))*180)/(math.pi)
    return tiltY

def point_direction(tiltX, tiltY):
# This function has a particular "bubble" turn on when it is tilted in that direction.
# Using if statements, depending on the angle at which the microbit is tilted, it will
# instruct the microbit to turn on a certain pixel. If it is tilted even further in the
# four main directions, it will turn on a further light to signify magnitude.
# It takes two parameters, tiltX and tiltY, which are the angles in the x and y directions
# that the microbit is being tilted. It has no return value.
    microbit.display.clear()
    print(tiltX, tiltY)
    if (-5 < tiltX < 5) and (-5 < tiltY < 5): #center
        microbit.display.set_pixel(2, 2, 9)
    elif (-5 < tiltX < 5) and (-15 < tiltY < -5): #North
        microbit.display.set_pixel(2, 1, 9)
        if (-5 < tiltX < 5) and (-40 < tiltY < -15): #North2
            microbit.display.set_pixel(2, 0, 9)
    elif (5 < tiltX < 15) and (-15 < tiltY < -5): #NE
        microbit.display.set_pixel(3, 1, 9)
    elif (5 < tiltX < 15) and (-5 < tiltY < 5): #E
        microbit.display.set_pixel(3, 2, 9)
        if (15 < tiltX < 40) and (-5 < tiltY < 5): #E2
            microbit.display.set_pixel(4, 2, 9)
    elif (5 < tiltX < 15) and (5 < tiltY < 15): #SE
        microbit.display.set_pixel(3, 3, 9)
    elif (-5 < tiltX < 5) and (5 < tiltY < 15): #South
        microbit.display.set_pixel(2, 3, 9)
        if (-5 < tiltX < 5) and (15 < tiltY < 40): #S2
            microbit.display.set_pixel(2, 4, 9)
    elif (-15 < tiltX < -5) and (5 < tiltY < 15): #SW
        microbit.display.set_pixel(1, 3, 9)
#         if (-40 < tiltX < -15) and (15 < tiltY < 40):
#             microbit.display.set_pixel(0, 4, 9)
    elif (-40 < tiltX < -15) and (-5 < tiltY < 5): #W
        microbit.display.set_pixel(1, 2, 9)
        if (-15 < tiltX < -5) and (-5 < tiltY < 5): #W2
            microbit.display.set_pixel(0, 2, 9)
    elif (-15 < tiltX < -5) and (-15 < tiltY < -5): #NW
        microbit.display.set_pixel(1, 1, 9)
    microbit.sleep(50)

while True:
    acc_x = microbit.accelerometer.get_x()
    acc_y = microbit.accelerometer.get_y()
    acc_z = microbit.accelerometer.get_z()

    point_direction(find_tilt_x(acc_x, acc_y, acc_z), find_tilt_y(acc_x, acc_y, acc_z))