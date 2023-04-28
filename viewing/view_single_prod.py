def view_single_product(product_lst: list) -> str:
    """This function takes in a list of product objects and
    prompts the user to enter the product id of the product whose
    info he is searching for. The function then locates the product
    with the id entered by the user and returns the __str__ method
    for that specific product object.

    Args:
        product_lst (list): List of product objects

    Returns:
        str: Output of product info using __str__ method
    """

    try:
        # Prompt user for the id of the product they want to view
        user_pid_input = int(input("Please enter the Product ID of the product: "))

    # Catch invalid user input for product id
    except ValueError:
        return "\nInvalid input. Please try again."

    try:
        # Assign the product object from the list to a variable
        user_product = product_lst[user_pid_input - 1]

    # Return error string in case user enters invalid product id
    except IndexError:
        return "\nProduct ID does not exist. Please try again."

    return user_product.__str__()
