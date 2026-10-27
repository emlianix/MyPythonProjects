nick = input()
body = nick[1:]

if (
    nick.startswith("@")
    and 5 <= len(nick) <= 15
    and body.isalnum()
    and body == body.lower()
):
    print("Correct")
else:
    print("Incorrect")