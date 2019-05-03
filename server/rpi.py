import requests
import ast
import RPi.GPIO as GPIO
from time import sleep

pin_x = 17
pin_y = 22
pin_z = 23
pin_w = 24
sec = 5 #time(seconds) for moving in particular direction

head = {
        'Host': 'wscar.somedomain.com',
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
    req = requests.post("http://www.somedomain.com/rpi/",headers=head)
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

def reverse(sec):
 init()
 GPIO.output(pin_x, True)
 GPIO.output(pin_y, False)
 GPIO.output(pin_z, True) 
 GPIO.output(pin_w, False)
 sleep(sec)
 GPIO.cleanup()

def forward(sec):
 init()
 GPIO.output(pin_x, False)
 GPIO.output(pin_y, True)
 GPIO.output(pin_z, False) 
 GPIO.output(pin_w, True)
 sleep(sec)
 GPIO.cleanup()

def left(sec):
 init()
 GPIO.output(pin_x, True)
 GPIO.output(pin_y, False)
 GPIO.output(pin_z, False) 
 GPIO.output(pin_w, True)
 sleep(sec)
 GPIO.cleanup()

def right(sec):
 init()
 GPIO.output(pin_x, False)
 GPIO.output(pin_y, True)
 GPIO.output(pin_z, True) 
 GPIO.output(pin_w, False)
 sleep(sec)
 GPIO.cleanup()


while (True):
    do_x = send()
    if (do_x == 2):
        forward(sec)
    elif (do_x == 8):
        reverse(sec)
    elif (do_x == 4):
        left(sec)
    elif (do_x == 6):
        right(sec)
    sleep(1)
