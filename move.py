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

def get():
    inkey = _Getch()
    k=inkey()
#FORWARD - W KEY
    if ord(k) == 119:
                GPIO.output(DRIVE_1, GPIO.HIGH)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.HIGH)
                GPIO.output(DRIVE_4, GPIO.LOW)
#REVERSE - S KEY
    if ord(k) == 115:
                GPIO.output(DRIVE_1, GPIO.LOW)
                GPIO.output(DRIVE_2, GPIO.HIGH)
                GPIO.output(DRIVE_3, GPIO.LOW)
                GPIO.output(DRIVE_4, GPIO.HIGH)
#SPIN LEFT - A KEY
    if ord(k) == 97:
                GPIO.output(DRIVE_1, GPIO.LOW)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.HIGH)
                GPIO.output(DRIVE_4, GPIO.LOW)
#SPIN LEFT - E KEY
    if ord(k) == 101:
                GPIO.output(DRIVE_1, GPIO.HIGH)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.LOW)
                GPIO.output(DRIVE_4, GPIO.HIGH)
#SPIN LEFT - Q KEY
    if ord(k) == 113:
                GPIO.output(DRIVE_1, GPIO.LOW)
                GPIO.output(DRIVE_2, GPIO.HIGH)
                GPIO.output(DRIVE_3, GPIO.HIGH)
                GPIO.output(DRIVE_4, GPIO.LOW)
#TURN RIGHT - D KEY
    if ord(k) == 100:
                GPIO.output(DRIVE_1, GPIO.HIGH)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.LOW)
                GPIO.output(DRIVE_4, GPIO.LOW)

    if ord(k) == 105:
                GPIO.output(DRIVE_1, GPIO.LOW)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.HIGH)
                GPIO.output(DRIVE_4, GPIO.HIGH)
# - L KEY
    if ord(k) == 108:
                GPIO.output(DRIVE_1, GPIO.LOW)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.LOW)
                GPIO.output(DRIVE_4, GPIO.HIGH)
# - J KEY
    if ord(k) == 106:
                GPIO.output(DRIVE_1, GPIO.LOW)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.HIGH)
                GPIO.output(DRIVE_4, GPIO.LOW)
#FULL STOP - K Key
    if ord(k) == 107:
                GPIO.output(DRIVE_1, GPIO.LOW)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.LOW)
                GPIO.output(DRIVE_4, GPIO.LOW)

#ESC Key
    if ord(k) == 27:
                exit()
    else:
                time.sleep(.1)
                GPIO.output(DRIVE_1, GPIO.LOW)
                GPIO.output(DRIVE_2, GPIO.LOW)
                GPIO.output(DRIVE_3, GPIO.LOW)
                GPIO.output(DRIVE_4, GPIO.LOW)


def main():
    while True:
        get()

if __name__=='__main__':
    main()
