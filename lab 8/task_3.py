user_creds = {
    "admin": "admin",
    "user456": "psw123",
    "user426": "psw121",
    "user457": "psw122",
    "user423": "psw156",
    "user434": "psw125",
    "user446": "psw126",
}

for login, password in user_creds.items():
    if login == "admin" and password == "admin":
        print("Brzydka strona")
    else:
        print("Twoja strona")