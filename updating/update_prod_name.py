def change_name(product_lst: list) -> str:
    """This function will take a list of product objects, search
    for a product specified by the user, and call the Product.update_name
    class method.

    Args:
        product_lst (list): List of product objects

    Returns:
        str: Output message of change in name
    """
    # Catch invalid input
    try:
        # Prompt user for which product they want to update
        user_pid_input = int(input("\nPlease enter the Product ID of the product: "))

    except ValueError:
        return "\nInvalid input. Please try again."
        # Assign the product object from the list to a variable

    # Catch invalid product id
    try:
        # Assign the product object from the list to a variable
        product = product_lst[user_pid_input - 1]

    except IndexError:
        return "\nProduct ID does not exist. Please try again."

    # Prompt the user to enter the new name
    new_name = input("\nPlease enter the new name: ")

    # Call update_price class method of Product
    product.update_name(new_name)

    return f"\n{product.name}'s name was updated to {new_name}"
