from .user import User


def init_new_user() -> list:
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
        input_info = user_name.split(" ")

        user_password = input("Please enter a simple password: ")

        new_user = User(input_info[0], input_info[1], user_password)

        return new_user.user_info

    except:
        return "Could not create user. Please try again."
