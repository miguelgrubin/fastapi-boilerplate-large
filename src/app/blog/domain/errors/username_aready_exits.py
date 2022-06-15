class UsernameAlreadyExits(Exception):
    def __init__(self, username: str):
        super().__init__(f"User with username {username} already exits.")
