def get_supp_info(product_lst: list) -> str:
    """This function takes in a list of products, prompts the
    user for input on which product id they want to search.
    Once they enter a valid product id, the system calls on
    the private class method __view_supplier_details() and returns
    a string of the info

    Args:
        product_lst (list): List of product objects

    Returns:
        str: String of supplier info for product
    """

    # Catch invalid user input
    try:
        user_pid_input = int(input("\nPlease enter the Product ID of the product: "))

    except ValueError:
        return "\nInvalid Product ID. Please try again."

    # Catch invalid product id
    try:
        product = product_lst[user_pid_input - 1]

    except IndexError:
        return "\nProduct ID does not exist. Please try again."

    # Return the result of the view_supplier_details private class method
    return product._Product__view_supplier_details()
