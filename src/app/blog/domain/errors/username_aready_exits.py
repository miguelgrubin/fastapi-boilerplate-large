class UserAlreadyExits(Exception):
    def __init__(self):
        super().__init__("User with this username or email already exits.")
