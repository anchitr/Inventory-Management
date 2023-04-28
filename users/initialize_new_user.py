from .user import User


def init_new_user() -> object:
    """This function will be executed upon running the inventory
    management program and will request the user to enter their
    information.

    Returns:
        list: The program will return a list of user info
    """
    try:
        user_name = input(
            "Please enter your first and last name separated by a space: "
        )
        names = user_name.split(" ")

        first_name = names[0]
        last_name = names[1]

    except IndexError:
        return "User name is invalid. Please try again."

    password = input("Please enter a simple password: ")

    new_user = User(first_name=first_name, last_name=last_name, password=password)

    return new_user
