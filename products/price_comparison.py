def compare_price(products: list) -> str:
    """This function takes a list of product objects, prints them out and
    requests the user to enter the ids of the products whose prices they
    want compared

    Args:
        products (list): List of product objects

    Returns:
        str: Message indicating whether the first product is more
        expensive or cheaper than the second product
    """
    print("Here are the following products in inventory:")

    for i in products:
        print(f"{i.product_id}: {i.name}")

    print("-" * 15)  # Separator line between product info and input prompt

    # Retrieve user input for the two products being compared
    try:
        user_product1_id = int(
            input("Please enter the id of the first comparison product: ")
        )
        user_product2_id = int(
            input("Please enter the id of the second comparison product: ")
        )

    # Handle errors if user enters id that doesn't exist in the product list
    except IndexError:
        return "One of the Product ID's is invalid. Please try again."

    # Store first product object
    first_product = products[user_product1_id - 1]

    # Store second product object
    second_product = products[user_product2_id - 1]

    first_product > second_product  # Compare prices of products

    if True:
        return (
            f"Product {first_product.name} is more expensive than {second_product.name}"
        )

    else:
        return f"Product {first_product.name} is cheaper than {second_product.name}"
