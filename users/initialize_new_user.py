from .user import User


def init_new_user() -> object:
    """This function will be executed upon running the inventory
    management program and will request the user to enter their
    information.

    Returns:
        list: The program will return a list of user info
    """

    # Get user first and last names
    user_first_name = input("Please enter your first name: ")

    user_last_name = input("Please enter your last name: ")

    # Get user password
    password = input("Please enter a simple password: ")

    # If user does not enter input for a field, assign default values to vars
    if user_first_name == "":
        user_first_name = "John"

    if user_last_name == "":
        user_last_name = "Doe"

    if password == "":
        password = "password"

    # Create list of arguments
    args = [user_first_name, user_last_name, password]

    # Pass in the args and create a new User object
    new_user = User(*args)

    return new_user
