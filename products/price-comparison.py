def compare_price(products: list) -> str:
    for i in products:
        print(f"{i.product_id}: {i.name}")

    try:
        user_product1_id = int(
            input("Please enter the id of the first comparison product: ")
        )
        user_product2_id = int(
            input("Please enter the id of the second comparison product: ")
        )

    except IndexError:
        return "One of the Product ID's is invalid. Please try again."

    products[user_product1_id - 1] > products[user_product2_id - 1]

    if True:
        return f"Product {user_product1_id} is more expensive than {user_product2_id}"

    else:
        return f"Product {user_product1_id} is cheaper than {user_product2_id}"
