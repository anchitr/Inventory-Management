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

    operation = input("\nAre you (A)dding or (S)ubtracting from the quantity? ")

    if operation.upper() == "A":
        try:
            # Prompt user on quantity to add
            add_quant = int(input("\nHow many units are being added? "))

        except ValueError:
            return "Invalid amount. Please try again."

        prod_quant[1] += add_quant

        return f"\n{add_quant} units were added to inventory!\n"

    elif operation.upper() == "S":
        try:
            # Prompt user on quantity to subtract
            minus_quant = int(input("\nHow many units are being subtracted? "))

        except ValueError:
            return "Invalid amount. Please try again."

        # Check if current quantity lower than user minus quant
        if prod_quant[1] < minus_quant:
            return f"\nError! There are only {prod_quant[1]} unit(s) left."

        # Else subtract quantity as expected
        else:
            prod_quant[1] -= minus_quant

            return f"\n{minus_quant} units were subtracted from inventory!\n"

    # Catch all for invalid options entered by the user
    else:
        return "\nInvalid option. Please try again."
