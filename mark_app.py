"""
Mark 
    - Generate a random password
    - If wrong password, tell user to reload page
    - If correct, LED blinks
"""


from flask import Flask

# import RPi.GPIO as GPIO
# from gpiozero import LED
from time import sleep

# LED_PIN = 11

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/blink")
# def blink():
#     for _ in range(10):
#         # GPIO.output(11, GPIO.HIGH)
#         sleep(1)
#         # GPIO.output(11, GPIO.LOW)
#         sleep(1)
#     return "<p>Blinked an LED.</p>"


@app.route("/")
def main_page():
    page_text = "you have to enter a password or else"

    return f"<p>{page_text}</p>"


def generate_password() -> str:
    # for testing...
    return "pass123"


# led = LED(16)

def test_enter_password():
    actual = generate_password()
    password = input("Enter the password or else: ")
    
    # - If wrong password, tell user to reload page
    if password != actual:
        print("reload the page or i will track your ip address  ")

    # - If correct, LED blinks
    else:  # they must be correct...
        print("Blinking LED... You won. :(")

        # loop 10 times
        for i in range(10):
            # turn it on
            # led.on()
            print("on")
            # wait 0.2s
            sleep(0.2)
            # off
            # led.off()
            print("off")
            # wait 0.2s
            sleep(0.2)


