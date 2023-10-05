"""
Adrian 
    - Take a picture and post it to the website
    - Whenever someone posts, an LED blinks

    - Take the picture ✓
    - Preview the picture ✓
    - Upload pic to site ✓
    - Blink LED

"""

from flask import Flask, render_template
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

LED_PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)
camera = PiCamera()

@app.route("/")
def take_picture():
    camera.start_preview()
    sleep(5) # TODO add "wait for button" instead of sleep(5)
    camera.capture('image.jpg')

    camera.stop_preview()
    camera.close()

    # return "<p>I've taken a picture of you. Check out this cool LED!</p>"
    return render_template('index.html')


@app.route("/blink")
def blink():
    for _ in range(10):
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(1)
    return "<p>Blinked an LED.</p>"


app.run(debug = True)
GPIO.cleanup()