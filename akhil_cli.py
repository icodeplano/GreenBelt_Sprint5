"""
Akhil's Site
    - Input a link
    - if the link is a credible source of information, then it blinks an LED and make the site say "it's a reliable source"
    - else [...]
"""
import time


def is_credible(link: str):
    whitelist = [".org", ".gov", "texas"]
    blacklist = [
        "wikipedia",
        "youtube",
        "reddit",
        "ifunny",
        "twitter",
        "tiktok",
    ]

    if link in whitelist:
        return True
    
    elif link in blacklist:
        return False
    
    # Deal with what if it's in neither the white nor blacklist


# Step 1: get the link from the user
user_link = input("enter a link: ")
# Step 2: Check if it's credible. If it is, do something
if is_credible(user_link):
    for i in range(3):
        print(f"Pretend like an LED just blinked. {i}")
        time.sleep(0.5)

    print("It IS a reliable source!!! KaBOOM")

# Step 3: Else, do something else
else:
    print("CODE RED")
    print("Pretend like you see a red website, lol.")