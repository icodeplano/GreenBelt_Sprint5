from flask import Flask
import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

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