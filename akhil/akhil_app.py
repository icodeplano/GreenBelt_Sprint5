from flask import Flask, request
# import gpiozero
from time import sleep

# LED_PIN = 11

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(LED_PIN, GPIO.OUT)

"""
Akhil's Site
    - Input a link
    - if the link is a credible source of information,
        then it blinks an LED and make the site say "it's a reliable source"
    - else [...]
"""

app = Flask(__name__)


def is_credible(link: str):
    whitelist = [".org", ".gov", "texas"]
    blacklist = [
        "wikipedia",
        "reddit",
        "ifunny",
        "twitter",
        "tiktok",
    ]

    for bad_link in blacklist:
        if bad_link in link:
            return False

    for good_link in whitelist:
        if good_link in link:
            return True


@app.route("/")
def main_page():
    html = """
        <form method="POST">
            <label>Enter a link:</label>
            <input name="text">
            <input type="submit">
        </form>
        """

    return html


@app.route("/", methods=["POST"])
def my_form_post():
    source_link = request.form["text"]

    if is_credible(source_link):
        return f"your source {source_link} is credible"
    else:
        return f"your source {source_link} is not credible"

app.run(debug=True)

# @app.route("/blink")
# def blink():
#     for _ in range(10):
#         GPIO.output(11, GPIO.HIGH)
#         sleep(1)
#         GPIO.output(11, GPIO.LOW)
#         sleep(1)
#     return "<p>Blinked an LED.</p>"


# ---------------------------------------------


# # Step 1: get the link from the user
# user_link = input("enter a link: ")
# # Step 2: Check if it's credible. If it is, do something
# if is_credible(user_link):
#     for i in range(3):
#         print(f"Pretend like an LED just blinked. {i}")
#         time.sleep(0.5)

#     print("It IS a reliable source!!! KaBOOM")

# # Step 3: Else, do something else
# else:
#     print("CODE RED")
#     print("Pretend like you see a red website, lol.")
