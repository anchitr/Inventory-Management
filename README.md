# Inventory Management Program

## Objective
Create an interactive command-line text program that allows a user to manage inventory for an audio player store. The user should be able to:
- View product and inventory information
- Update product attributes such as name and price
- Add new products to the store's offerings
- Update inventory counts
- Compare prices between two products

## User Guide
1. Locate and run the **inventory_management_program.py** in the main folder
2. Follow the text prompts and provide first and last name, and a password
3. User will be greeted by main menu prompt that will highlight the following choices:
   1. (V)iew Information on Inventory or Products
   2. (U)pdate Inventory, Product, or User Information
   3. (C)ompare prices between 2 products
   4. (Q)uit the Program
4. The program will prompt the user to enter the character of their choice, the characters to enter in the program will **always** be capitalized within parentheses (*ex.* p(R)oduct, choice would be 'R')
5. Starting out, the program will initialize a list of 5 default products each with a starting inventory of 10
6. User can view, update, compare prices and once finished, they can enter **"Q"** to quit the program

**To view the flowchart below, please install Markdown Preview (shd101wyy.markdown-preview-enhanced), and Markdown Preview Mermaid Support (bierner.markdown-mermaid) in VSCode and show preview**

## All User Choice Flows

```mermaid
flowchart TD;
    id1(Main Menu)-->|V|id2(View);
    id1(Main Menu)-->|U|id3(Update);
    id1(Main Menu)-->|C|id4(Compare);
    id1(Main Menu)-->|Q|id5(Quit);

    id2(View)-->|P|id6(Product);
    id2(View)-->|I|id7(Inventory);
    id6(Product)-->|S|id8(Single);
    id8(Single)-->|R|id15(Product Info)
    id8(Single)-->|U|id16(Supplier Info)
    id6(Product)-->|A|id9(All);

    id3(Update)-->|I|id10(Inventory);
    id3(Update)-->|P|id11(Product);
    id11(Product)-->|R|id12(Price)
    id11(Product)-->|N|id13(Name)
    id11(Product)-->|A|id14(New Product)

```
