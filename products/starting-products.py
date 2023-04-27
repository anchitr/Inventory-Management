from product import Product  # Import Product class


def init_product_list() -> list:
    """This function initializes 5 products to start as part
    of the store's inventory

    Returns:
        list: A list of product objects
    """
    # Define starting product information
    starting_products = [
        [1, "Sony Walkman", "Retro MP3 player", 132.26, "Sony", 70.31],
        [2, "Radio", "AM/FM listening device", 25.97, "RadioShack", 13.21],
        [3, "iPod Nano", "A portable MP3 player", 278.34, "Apple", 189.04],
        [4, "iPhone", "Cellphone and MP3 player", 793.99, "Apple", 589.07],
        [5, "Kann Max", "Audiophile grade HiFi DAP", 2788.13, "A&K", 734.84],
    ]

    product_lst = []

    for item in starting_products:
        args = item
        product = Product(*args)

        product_lst.append(product)

    return product_lst
