from flask import Flask
import RPi.GPIO as GPIO
import gpiozero
from time import sleep

# LED_PIN = 11

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(LED_PIN, GPIO.OUT)

"""
Akhil's Site
    - Input a link
    - if the link is a credible source of information, then it blinks an LED and make the site say "it's a reliable source"
    - else [...]
"""

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