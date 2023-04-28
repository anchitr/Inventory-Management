def init_inventory(product_lst: list) -> list:
    """This function takes a list of product objects
    and creates a separate list of quantities and zips
    the two lists together.

    Args:
        product_lst (list): List of product objects

    Returns:
        list: Zipped list of product objects and quantities
    """

    # Create default starting quantity list of 10 for each product
    starting_quant = [10 for i in range(len(product_lst))]

    # Zip the two lists together to create product/quantity lists in one list
    current_inventory = list(zip(product_lst, starting_quant))

    return current_inventory  # Return the list of lists
