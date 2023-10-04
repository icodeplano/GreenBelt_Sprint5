"""
Adrian 
    - Take a picture and post it to the website
    - Whenever someone posts, an LED blinks

    - Take the picture
    - Upload pic to site
    - Preview the picture
    - Blink LED

"""

from flask import Flask

# import RPi.GPIO as GPIO
import gpiozero
from time import sleep

# LED_PIN = 11

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/blink")
def blink():
    for _ in range(10):
        GPIO.output(11, GPIO.HIGH)
        sleep(1)
        GPIO.output(11, GPIO.LOW)
        sleep(1)
    return "<p>Blinked an LED.</p>"
