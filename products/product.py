class Product:
    """This class takes information about a product and allows
    for various class methods to operate on certain values
    """

    def __init__(
        self,
        product_id: int,
        name: str,
        description: str,
        price: float,
        supplier: str,
        purchase_price: float,
    ) -> None:
        """This constructor takes multiple values and creates a product dict
        whose attributes can be updated through various class methods

        Args:
            id (int): id number of the product
            name (str): name of the product
            description (str): short description of the product
            price (float): selling price of the product
            supplier (str): name of the supplier product is purchased from
            purchase_price (float): price that the store pays for the product
        """

        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.__supplier = supplier
        self.__purchase_price = purchase_price

        self.product_dict = {
            "product_id": product_id,
            "name": name,
            "description": description,
            "price": price,
            "supplier_info": (self.__supplier, self.__purchase_price),
        }

    def __str__(self) -> str:
        """This method returns all public attribute information
        of a product in a formatted string

        Returns:
            str: string of formatted product info
        """

        return (
            f"Product ID: {self.product_dict['product_id']}\n"
            f"Product Name: {self.product_dict['name']}\n"
            f"Product Description: {self.product_dict['description']}\n"
            f"Product Price: ${self.product_dict['price']:.2f}\n"
        )

    def __view_supplier_info(self) -> str:
        """This private class method takes a product id and returns
        the supplier name and price the store pays per unit
        of the product

        Returns:
            str: return string of formatted private product info
        """
        return (
            f"The supplier information for the {self.product_dict['name']} is:\n"
            f"Supplier Name: {self.product_dict['supplier_info'][0]}\n"
            f"Purchase Price: {self.product_dict['supplier_info'][1]}\n"
        )

    def update_price(self, new_price: float) -> None:
        """This method allows user to update the price of a product

        Args:
            new_price (float): The new price of the product
        """
        try:
            if (self.price != new_price) and (new_price > 0):
                self.product_dict["price"] = new_price
        except:
            return "Please enter a valid new price"

    def update_name(self, new_name: str) -> None:
        """This method allows the user to update the name of the product

        Args:
            new_name (str): The new name of the product
        """
        try:
            self.product_dict["name"] = new_name

        except:
            return "Please enter a valid name"

    def __gt__(self, other: object) -> bool:
        """A magic method that checks if a product's price is greater
        than or equal to anothers

        Args:
            other (object): product object being compared

        Returns:
            bool: returns True or False based on condition
        """
        return self.price >= other.price


if __name__ == "__main__":
    sample_products = [
        [1, "Sony Walkman", "A device to listen to music", 132.26, "Sony", 70.31],
        [2, "Radio", "A device to listen to AM/FM", 25.97, "RadioShack", 13.21],
        [3, "iPod", "A portable music player", 278.34, "Apple", 189.04],
        [4, "iPhone", "Cell phone and MP3 player", 793.99, "Apple", 589.07],
        [5, "iPod Nano", "Ultra-portable MP3 player", 589.13, "Apple", 461.84],
    ]

    product_lst = []

    for item in sample_products:
        args = item
        product = Product(*args)

        product_lst.append(product)

    for i in product_lst:
        print(i.__str__())

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

        product_lst[user_product1_id - 1] > product_lst[user_product2_id - 1]

        if True:
            return (
                f"Product {user_product1_id} is more expensive than {user_product2_id}"
            )

        else:
            return f"Product {user_product1_id} is cheaper than {user_product2_id}"

    print(compare_price(product_lst))
