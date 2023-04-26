class Product:
    """This class takes information about a product and allows
    for various class methods to operate on certain values
    """

    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        price: float,
        supplier: str,
        purchase_price: float,
    ) -> None:
        """This constructor takes multiple values and creates a product
        whose attributes can be updated through various class methods

        Args:
            id (int): id number of the product (must be unique)
            name (str): name of the product
            description (str): short description of the product
            price (float): selling price of the product
            supplier (str): name of the supplier product is purchased from
            purchase_price (float): price that the store pays for the product
        """
        self.id = id
        self.name = name
        self.desciption = description
        self.price = price
        self.__supplier = supplier
        self.__purchase_price = purchase_price
