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
