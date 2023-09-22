from time import sleep

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



test_enter_password()