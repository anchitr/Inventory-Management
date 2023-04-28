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
            f"\nProduct ID: {self.product_dict['product_id']}\n"
            f"Product Name: {self.product_dict['name']}\n"
            f"Product Description: {self.product_dict['description']}\n"
            f"Product Price: ${self.product_dict['price']:.2f}\n"
        )

    def __view_supplier_details(self) -> str:
        """This private class method takes a product id and returns
        the supplier name and price the store pays per unit
        of the product

        Returns:
            str: return string of formatted private product info
        """
        return (
            f"\nThe supplier information for the {self.product_dict['name']} is:\n"
            f"Supplier Name: {self.product_dict['supplier_info'][0]}\n"
            f"Purchase Price: {self.product_dict['supplier_info'][1]}\n"
        )

    def update_price(self, new_price: float) -> None:
        """This method allows user to update the price of a product

        Args:
            new_price (float): The new price of the product
        """
        # Check if price is different and greater than 0
        if (self.price != new_price) and (new_price > 0):
            self.price = new_price  # Update price class attribute

            # Update price in product dict
            self.product_dict["price"] = new_price

    def update_name(self, new_name: str) -> None:
        """This method allows the user to update the name of the product

        Args:
            new_name (str): The new name of the product
        """
        # Update class attribute to new name
        self.name = new_name

        # Update product dict info with new name
        self.product_dict["name"] = new_name

    def get_price(self) -> float:
        """This method gets the price of the product. For unittest
        purposes only.

        Returns:
            float: Product price as float
        """
        return self.price

    def get_name(self) -> str:
        """This method gets the name of a product. For unittest
        purposes only.

        Returns:
            str: Name of the product
        """
        return self.name

    def __gt__(self, other: object) -> bool:
        """A magic method that checks if a product's price is greater
        than or equal to anothers

        Args:
            other (object): product object being compared

        Returns:
            bool: returns True or False based on condition
        """
        return self.price >= other.price
