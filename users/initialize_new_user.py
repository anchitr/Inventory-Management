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

    new_user = User(
        first_name=user_first_name, last_name=user_last_name, password=password
    )

    return new_user
