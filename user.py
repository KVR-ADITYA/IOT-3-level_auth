import getpass


class User:
    def __init__(self, username, pwd):
        self.username = username
        self.password = pwd
        print(self.password)

    @staticmethod
    def register():
        username = input("Enter Username: ")
        pwd = getpass.getpass("Password: ")
        # Check validity of both from the gateway
        User(username, pwd)
