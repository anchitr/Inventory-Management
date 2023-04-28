def inv_prod_update(inventory_lst: list, product_lst: list) -> list:
    """This function will be called after adding a new product to create
    a new entry in the inventory with the starting quantity of 10. It
    returns a list of product object and quantity lists.

    Args:
        inventory_lst (list): List of lists (product obj, quantity)
        product_lst (list): List of product objects

    Returns:
        list: _description_
    """

    # Check if the length of the lists are equal (should not be)
    if len(inventory_lst) == len(product_lst):
        return "No new products to update"

    else:
        # Assign the new product object to a variable
        new_product = product_lst[-1]

        # Create a list with the product object and a starting quantity of 10
        add_to_inv = [new_product, 10]

        # Append the new list of prod obj and quantity to inventory list
        inventory_lst.append(add_to_inv)

        return inventory_lst  # Return update inventory list
