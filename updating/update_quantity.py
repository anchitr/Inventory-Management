def change_quant(inventory_lst: list) -> str:
    """This function takes in a list of product objects and quantity lists
    and updates the value for a single product in the list. It then
    returns a string that lets the user know that the quantity was
    updated.

    Args:
        inventory_lst (list): List of product objects and quantities

    Returns:
        str: String to let user know the operation succeeded
    """

    user_pid = int(input("\nPlease select the product id to be updated: "))

    prod_quant = inventory_lst[user_pid - 1]

    operation = input("Are you (A)dding or (S)ubtracting from the quantity? ")

    if operation.upper() == "A":
        # Prompt user on quantity to add
        add_quant = int(input("How many units are being added? "))

        prod_quant[1] += add_quant

        return f"\n{add_quant} units were added to inventory!\n"

    elif operation.upper() == "S":
        # Prompt user on quantity to subtract
        minus_quant = int(input("How many units are being subtracted? "))

        # Check if current quantity lower than user minus quant
        if prod_quant[1] < minus_quant:
            return f"\nError! There are only {prod_quant[1]} units left."

        # Else subtract quantity as expected
        else:
            prod_quant[1] -= minus_quant

            return f"\n{minus_quant} units were subtracted from inventory!\n"
