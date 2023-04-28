def view_all_products(product_lst: list) -> list:
    """This function takes in a list of product objects
    and prints the __str__ method for all of them while
    storing the strings into a list

    Args:
        product_lst (list): List of product Objects

    Returns:
        list: List of product info strings
    """
    all_product_info = []

    for item in product_lst:
        output = item.__str__()

        all_product_info.append(output)

    return all_product_info
