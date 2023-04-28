def view_all_inventory(inventory_lst: list) -> list:
    """This function loops through a list of lists and presents
    the product id, name, and current quantity

    Args:
        inventory_lst (list): List of product objects and quantities

    Returns:
        list: List of strings containing product id, name,
        and quantity in inventory
    """
    # Initialize empty list to store formatted strings
    all_inventory_info = []

    # Create header row
    headers = f"{'ID' : <5}{'Name' : <15}{'Quantity' : <5}"

    all_inventory_info.append(headers)  # Insert header row string

    for lst in inventory_lst:
        # Insert formatted string of id, name, and quantity
        output = f"{lst[0].product_id : <5}{lst[0].name : <15}{lst[1] : <5}"

        all_inventory_info.append(output)  # Append to final list

    return all_inventory_info
