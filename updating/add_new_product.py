from products import product


def new_product(product_lst: list) -> list:
    """This function takes a list of product objects,
    initializes a new instance of the Product class and
    appends the resulting object into the list and returns
    it.

    Args:
        product_lst (list): List of product objects

    Returns:
        list: List of product objects with new object
    """
    # Use list comp to create a list of all existing product ids
    prod_id_lst = [item.product_id for item in product_lst]

    # Assign the new product's id as the last value of the id list plus 1
    new_prod_id = prod_id_lst[-1] + 1

    # Prompt user for product name
    user_prod_name = input("Please enter the name of the product: ")

    # Prompt user for product description
    user_prod_description = input("Please enter the description of the product: ")

    try:
        # Prompt user for product price
        user_prod_price = float(
            input("Please enter the price of the product (up to 2 decimals): ")
        )

    # Catch invalid price input from user
    except ValueError:
        return "\nInvalid input. Please try again."

    # Prompt user for product supplier name
    user_prod_supplier = input(
        "Please enter the company the product is purchased from: "
    )

    try:
        # Prompt user for product supplier price
        user_prod_s_price = float(
            input("Please enter how much the supplier charges (up to 2 decimals): ")
        )

    # Catch invalid price input from user
    except ValueError:
        return "\nInvalid input. Please try again."

    # Compile all arguments into a single list
    args = [
        new_prod_id,
        user_prod_name,
        user_prod_description,
        user_prod_price,
        user_prod_supplier,
        user_prod_s_price,
    ]

    # Pass in args list and create a new instance of Product
    new_product = product.Product(*args)

    product_lst.append(new_product)  # Append new object to original list

    return product_lst  # Return list of objects with new product
