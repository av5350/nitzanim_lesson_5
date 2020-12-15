LIMIT_CHARS = 8

user_name = input("Enter your username: ")

if "@" in user_name and "." in user_name:
    password = input("Enter your password:")

    if "#" in password and len(password) >= LIMIT_CHARS:
        print("BOOOOM!!!! You're in")
    else:
        print("Password Invalid")
else:
    print("Username Invalid")