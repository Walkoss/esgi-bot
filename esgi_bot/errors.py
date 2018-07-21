class AuthError(RuntimeError):
    print("Invalid username and/or password !")


class ValueNotFound(RuntimeError):
    print("Invalid entry or value not found !")
