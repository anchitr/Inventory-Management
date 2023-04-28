"""
Anchit Rao
Class: CS 521 - Spring 2
Date: April 25, 2023
Term Project
Description of Project:
This is a program that allows a manager of a store to view store inventory,
product details, add new products, and monitor stock transactions.
"""

from greeters import greeting, salutation
from products import product, starting_products, price_comparison
from inventory import initialize_inventory
from users import initialize_new_user
from viewing import view_all_inv, view_all_prod, view_single_prod
from updating import update_quantity, update_prod_price, update_prod_name


# TODO:
# - [x] Write program docstring
# - [x] Create Product class
#   - [x] Must have init() class method that takes at least 1 arg
#   - [x] Must have 1 private and 2 public class attributes
#   - [x] Must have 1 private and 2 public class methods
#   - [x] Must have __repr__ or __str__ class method
#   - [x] Must have one magic class method (not including above requirements)
# - Create User class
#   - [x] Private password attribute
#   - [x] Public name update method
# - Identify best way of handling inventory control (dict v nested lists)
# - [x] Identify best method of storing product details (external csv v dict)
# - [x] Create starting list of products
# - Design user prompts and input acceptance
# - Design unittests for public class method testing
#
#


def main_menu() -> str:
    """Function that presents the main menu choices
    for the user

    Returns:
        str: String of user choices
    """
    main_menu_text = (
        f"\nWhat would you like to do?\n"
        f"(V)iew Information on Inventory or Products\n"
        f"(U)pdate Inventory, Product, or User Information\n"
        f"(C)ompare prices between 2 products\n"
        f"(Q)uit the Program\n"
    )
    return main_menu_text


if __name__ == "__main__":
    print(greeting.hello_user())

    # Initialize list of default starting products
    products = starting_products.init_product_list()

    # ---------------- BEGIN UNITTEST SECTION ----------------

    # Initialize instance of test product
    test_product = product.Product(
        10, "Fake iPod", "Generic brand iPod", 293.45, "CNW", 34.83
    )

    # Call update_price class method on test product
    test_product.update_price(368.73)

    assert test_product.get_price() == 368.73, "Price unittest failed!"

    # Call update_name method on test product
    test_product.update_name("Walkman")

    assert test_product.get_name() == "Walkman", "Name unittest failed!"

    # ---------------- END UNITTEST SECTION ----------------

    # Initialize list of default starting inventory
    current_inventory = initialize_inventory.init_inventory(products)

    # Call function to start onboarding new user
    new_user = initialize_new_user.init_new_user()

    print(f"\n{new_user.__repr__()}")

    while True:
        # Print all available main menu options
        print(main_menu())

        # Initialize input variable for the main menu choice
        user_main_choice = input(
            "Please type the character in parentheses of your choice: "
        )

        # -------------- BEGIN HANDLING OF ALL VIEWING OPTIONS ----------------
        if user_main_choice.upper() == "V":
            print("Would you like to view (P)roduct or (I)nventory information?")

            user_selection = input("\nEnter the character of your choice: ")

            # If user chooses to view Inventory information
            if user_selection.upper() == "I":
                print("\nHere is the current inventory for the store:\n")

                # Get a list of prod obj and quantities and print output
                all_inventory = view_all_inv.view_all_inventory(current_inventory)

                for item in all_inventory:
                    print(item)

            # If user chooses to view Product information
            elif user_selection.upper() == "P":
                print(
                    "\nWould you like view info for a (S)ingle product or (A)ll products?"
                )

                user_prod_view = input("\nEnter the character of your choice: ")

                # If user selects information for all Products
                if user_prod_view.upper() == "A":
                    print("\nHere is the info for all products sold in store:\n")

                    all_products = view_all_prod.view_all_products(products)

                    for item in all_products:
                        print(item)

                # If user selects to information for a single Product
                elif user_prod_view.upper() == "S":
                    print(
                        "\nYou have chosen to search for a single product's information.\n"
                    )

                    prod_info = view_single_prod.view_single_product(products)

                    print(prod_info)

                # Catch all for invalid characters in viewing block
                else:
                    print("\nInvalid option. Please try again.")

        # -------------- END HANDLING OF VIEWING OPTIONS ----------------------

        # -------------- BEGIN HANDLING OF ALL UPDATE OPTIONS -----------------
        elif user_main_choice.upper() == "U":
            print("Would you like to update (I)nventory or (P)roduct Info?")

            user_selection = input("\nEnter the character of your choice: ")

            # If user selects to update Inventory quantity
            if user_selection.upper() == "I":
                # Run inventory update function
                quant_change = update_quantity.change_quant(current_inventory)

                print(quant_change)

            # If user selects to update Product info
            elif user_selection.upper() == "P":
                print("\nWould you like to update product (N)ame or p(R)ice")

                user_prod_update = input("\nEnter the character of your choice: ")

                if user_prod_update.upper() == "N":
                    name_change = update_prod_name.change_name(products)

                    print(name_change)

                elif user_prod_update.upper() == "R":
                    # Call the change_price function
                    price_change = update_prod_price.change_price(products)

                    print(price_change)  # Print the resulting string

                # Handle invalid inputs inside product update section
                else:
                    print("\nInvalid option. Please try again.")

            # Catch all for invalid characters in updating block
            else:
                print("\nInvalid option. Please try again.")

        # -------------- END HANDLING OF UPDATE OPTIONS ----------------------

        # -------------- BEGIN HANDLING OF COMPARE OPTION ---------------------
        elif user_main_choice.upper() == "C":
            print(price_comparison.compare_price(products))

        # -------------- END HANDLING OF COMPARE OPTION -----------------------

        elif user_main_choice.upper() == "Q":
            print(salutation.good_bye())
            break
