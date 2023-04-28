def change_price(product_lst: list) -> str:
    """This function will take a list of product objects, search
    for a product specified by the user, and call the Product.update_price
    class method.

    Args:
        product_lst (list): List of product objects

    Returns:
        str: Output message of change in price
    """
    try:
        # Prompt user for which product they want to update
        user_pid_input = int(input("\nPlease enter the Product ID of the product: "))

    except ValueError:
        return "\nInvalid input. Please try again."

    try:
        # Assign the product object from the list to a variable
        product = product_lst[user_pid_input - 1]

    # Return error string in case user enters invalid product id
    except IndexError:
        return "\nProduct ID does not exist. Please try again."

    # Prompt the user to enter the new price and convert value to float
    new_price = float(input("\nPlease enter the new price: "))

    # Call update_price class method of Product
    product.update_price(new_price)

    return f"\n{product.name}'s price was updated to ${new_price:.2f}"
