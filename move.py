import sys,tty,termios,time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DRIVE_1 = 23
#REV
DRIVE_2 = 22
DRIVE_3 = 17
DRIVE_4 = 18

GPIO.setup(DRIVE_1, GPIO.OUT)
GPIO.setup(DRIVE_2, GPIO.OUT)
GPIO.setup(DRIVE_3, GPIO.OUT)
GPIO.setup(DRIVE_4, GPIO.OUT)

fwleft = GPIO.PWM(DRIVE_1,50)
rvleft = GPIO.PWM(DRIVE_2,50)
fwright = GPIO.PWM(DRIVE_3,50)
rvright = GPIO.PWM(DRIVE_4,50)


fwleft.start(0)
rvleft.start(0)
fwright.start(0)
rvright.start(0)


class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


#w= 119
#s= 115
#a = 97
#d = 100

#i=105
#k=107
#j=106
#l=108

def drive(power):
    inkey = _Getch()
    k=inkey()
    print power
#FORWARD - W KEY
    if ord(k) == 119:
        if power > 95:
            print "Full Speed"
            pass
        if power < 0:
            print "Accelerating"
            power = power + 1
            rvleft.start(power)
            rvright.start(power)
            fwleft.start(0)
            fwright.start(0)
        if power > -1:
            power = power + 1
            fwleft.start(power)
            fwright.start(power)
            rvleft.start(0)
            rvright.start(0)
#REVERSE - S KEY
    if ord(k) == 115:
        if power < -95:
            pass
            print "Full Reverse"
        if power < -1:
            rvleft.start(power)
            rvright.start(power)
            power = power - 1
        if power > 0:
            power = power - 1
            fwleft.start(-power)
            fwright.start(-power)
#SPIN LEFT - A KEY
    if ord(k) == 97:
        if power > 20:
            fwright.start(power-20)
            rvright.start(0)
        if power < 0:
            fwright.start(0)
            rvright.start(power-20)
#SPIN LEFT - E KEY
#    if ord(k) == 101:
#                GPIO.output(DRIVE_1, GPIO.HIGH)
#                GPIO.output(DRIVE_2, GPIO.LOW)
#                GPIO.output(DRIVE_3, GPIO.LOW)
#                GPIO.output(DRIVE_4, GPIO.HIGH)
#SPIN LEFT - Q KEY
#    if ord(k) == 113:
#                GPIO.output(DRIVE_1, GPIO.LOW)
#                GPIO.output(DRIVE_2, GPIO.HIGH)
#                GPIO.output(DRIVE_3, GPIO.HIGH)
#                GPIO.output(DRIVE_4, GPIO.LOW)
#TURN RIGHT - D KEY
    if ord(k) == 100:
        if power > 20:
            fwleft.start(power-20)
            rvleft.start(0)
        if power < 0:
            fwleft.start(0)
            rvleft.start(power-20)
#ESC Key
    if ord(k) == 27:
                GPIO.cleanup()
                exit()
    else:
        if power > -1:
            rvleft.start(power)
            rvright.start(power)
            fwleft.start(0)
            fwright.start(0)
        if power < 0:
            fwleft.start(-power)
            fwright.start(-power)
            rvleft.start(0)
            rvright.start(0)
    return power

power = 0
while True:
    power = drive(power)


