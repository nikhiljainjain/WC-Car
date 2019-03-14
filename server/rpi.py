import requests
import ast
import RPi.GPIO as GPIO
from time import sleep

pin_x = 17
pin_y = 22
pin_z = 23
pin_w = 24

def init():
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(pin_x, GPIO.OUT)
 GPIO.setup(pin_y, GPIO.OUT)
 GPIO.setup(pin_z, GPIO.OUT)
 GPIO.setup(pin_w, GPIO.OUT)

def forward(sec):
 init()
 GPIO.output(pin_x, True)
 GPIO.output(pin_y, True)
 GPIO.output(pin_z, False) 
 GPIO.output(pin_w, False)
 sleep(sec)
 GPIO.cleanup()

def reverse(sec):
 init()
 GPIO.output(17, False)
 GPIO.output(22, True)
 GPIO.output(23, False) 
 GPIO.output(24, True)
 sleep(sec)
 GPIO.cleanup()

print "forward"
forward(10)

print "reverse"
reverse(20)


head = {
        'Host': 'multi-threading-nikhiljainjain17.c9users.io',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': 'c9.live.user.click-through=ok',
        'Upgrade-Insecure-Requests': '1',
        'If-None-Match': 'W/"1a-QTTE0q9So4pDu7x71Fzj3+8LQyg"',
        'Cache-Control': 'max-age=0'
    }

req = requests.post("https://multi-threading-nikhiljainjain17.c9users.io/rpi",headers=head)

a = req.content
#b = ast.literal_eval(a.decode("utf-8"))


print(a)