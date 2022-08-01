from logging import error
import re

email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password = re.compile(r"[a-zA-Z0-9$%#@]{7,}[0-9]")
user_email = ''
user_password = ''

print("Welcome! Please enter a valid email:")
while True:
    try:
        user_email = input()

        if email.fullmatch(user_email):
            break
        else:
            raise error
    except:
        print("\nPlease enter a valid email!")


print(
    '''\nGreat! Now create a password that:
    Is at least 8 characters long
    Can contain any sort of letters, numbers, and '$%#@'
    Ends with a number
    ''')
while True:
    try:
        user_password = input()

        if password.fullmatch(user_password):
            break
        else:
            raise error
    except:
        print("\nPlease enter a valid password!")


print(
f'''\nYou have successfully created a valid email and password!
Email: {user_email}
Password: {user_password}
''')
