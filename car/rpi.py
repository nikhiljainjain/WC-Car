import requests
import ast
import RPi.GPIO as GPIO
from time import sleep

pin_x = 17
pin_y = 22
pin_z = 23
pin_w = 24
sec = 1 #time(seconds) for moving in particular direction

head = {
        'Host': 'www.domain.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'If-None-Match': 'W/"1a-QTTE0q9So4pDu7x71Fzj3+8LQyg"',
        'Cache-Control': 'max-age=0'
    }


def send():
    req = requests.post("http://www.yourdoamin.com/rpi/",headers=head)
    content = req.content
    json_data = ast.literal_eval(content.decode("utf-8"))
    direction = json_data['btn']
    print(direction)
    return direction


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin_x, GPIO.OUT)
    GPIO.setup(pin_y, GPIO.OUT)
    GPIO.setup(pin_z, GPIO.OUT)
    GPIO.setup(pin_w, GPIO.OUT)

def reverse():
 GPIO.output(pin_x, True)
 GPIO.output(pin_y, False)
 GPIO.output(pin_z, True)
 GPIO.output(pin_w, False)

def forward():
 GPIO.output(17, False)
 GPIO.output(22, True)
 GPIO.output(23, False)
 GPIO.output(24, True)

def left():
 GPIO.output(pin_x, True)
 GPIO.output(pin_y, False)
 GPIO.output(pin_z, False)
 GPIO.output(pin_w, True)

def right():
 GPIO.output(17, False)
 GPIO.output(22, True)
 GPIO.output(23, True)
 GPIO.output(24, False)

init()
while (True):
    do_x = send()
    if (do_x == 2):
        forward()
    elif (do_x == 8):
        reverse()
    elif (do_x == 4):
        left()
    elif (do_x == 6):
        right()
    elif (do_x == 5):
        sleep(5)
    sleep(4)
