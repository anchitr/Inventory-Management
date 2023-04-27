class User:
    """This class is meant to store information
    about the user currently operating the program
    """

    def __init__(self, first_name: str, last_name: str, password: str) -> None:
        """This constructor takes the user's info as arguments and stores
        it for viewing and confirming actions in the main program

        Args:
            first_name (str): First name of the user
            last_name (str): Last name of the user
            password (str): Password decided by user (should be simple)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.__password = password

        self.user_info = []

        self.user_info.append(self.first_name, self.last_name, (self.__password))

    def __repr__(self) -> str:
        """This function returns the first and last name of the
        user in a greeting message

        Returns:
            str: Greeting message adressing the user
        """
        return f"Greetings {self.user_info[0]} {self.user_info[1]}!"
