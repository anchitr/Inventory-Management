def view_single_product(product_lst: list) -> str:
    """This function takes in a list of product objects and
    prompts the user to enter the product id of the product whose
    info he is searching for. The function then locates the product
    with the id entered by the user and returns the __str__ method
    for that specific product object.

    Args:
        product_lst (list): List of product objects

    Returns:
        str: Output of product info
    """

    try:
        user_pid_input = int(input("Please enter the Product ID of the product: "))

        for item in product_lst:
            if item.product_id == user_pid_input:
                return item.__str__()

    except IndexError:
        return "That Product ID does not exist. Please try again. "
