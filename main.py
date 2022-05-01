#!/usr/bin/env python3
from ev3dev.ev3 import *
import math
from math import *
import time


motorL = LargeMotor('outB')
motorR = LargeMotor('outC')
gyro_port =

k1 = 0.487
k2 = 0.024
k3 = 0.153
k4 = 0

start_time = time.time()
motorL.position = motorR.position = t = 0

segway_angle = 0
segway_speed = 0
wheel_angle = 0
last_wheel_angle = 0
wheel_speed = 0
u = 0

SetSensorHTGyro(gyro_port)

while True:
    dt = time.time() - time_now
    time_now = time.time() - start_time
    segway_speed = (SensorHTGyro(gyro_port))
    segway_angle += segway_speed * dt

    last_wheel_angle = wheel_angle
    wheel_angle = (motorR.position + motorL.position) / 2
    wheel_speed = (wheel_angle - last_wheel_angle) / dt

    u = k1 * segway_angle + k2 * wheel_speed + k3 * segway_speed + k4 * wheel_angle

    if u > 100:
        u = 100
    elif u < -100:
        u = -100

    motorL.run_direct(duty_cycle_sp=u)
    motorR.run_direct(duty_cycle_sp=u)
