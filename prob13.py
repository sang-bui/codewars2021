from math import sqrt

name = input()
lOfRamp = int(input())
acc = float(input())
wOfRiver = float(input())

time = sqrt(2*lOfRamp/acc)
speed = time * acc
distance = speed**2/9.805

if distance < wOfRiver-5:
    print("{} will reach a speed of {} m/s on a {} meter ramp, crossing {} of {} meters, SPLASH!".format(name, round(speed,2), lOfRamp, round(distance,2), wOfRiver))
elif distance >= wOfRiver-5 and distance <= wOfRiver:
    print("{} will reach a speed of {} m/s on a {} meter ramp, crossing {} of {} meters, BARELY MADE IT!".format(name, round(speed,2), lOfRamp, round(distance,2), wOfRiver))
elif distance > wOfRiver:
     print("{} will reach a speed of {} m/s on a {} meter ramp, crossing {} of {} meters, LIKE A BOSS!".format(name, round(speed,2), lOfRamp, round(distance,2), wOfRiver))
