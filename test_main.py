# Importing classes from modules

from ebook import Ebook
from customer import Customer
from cart import Cart
from invoice import Invoice
from store import Store

def test_add_modify_remove_ebook():
    print("=== Testing Add/Modify/Remove E-book ===")
    print()
    
    # Step 1: Initialize the store
    
    store = Store()
    
    # Step 2: Add an ebook to the store catalog
    
    ebook1 = Ebook("Python Programming", "Ahmad", "2023-01-01", "Education", 20.0)
    store.add_ebook(ebook1)
    print("Added e-book: " + str(ebook1))
    
    # Step 3: Modify the e book price
    ebook1.set_price(18.0)
    print("Modified e-book price: " + str(ebook1.get_price()))
    
    # Step 4: Remove the e book from the catalog
    store.remove_ebook("Python Programming")
    
    # Print the catalog to confirm removal
    titles = []
    for ebook in store.get_ebook_catalog():
        titles.append(ebook.get_title())

    titles_str = ""
    for title in titles:
        titles_str += title + ", "

    # Remove the comma and space
    if titles_str.endswith(", "):
        titles_str = titles_str[:-2]

    print("E-book catalog after removal: " + titles_str + "\n")

def test_add_modify_remove_customer():
    print("=== Testing Add/Modify/Remove Customer ===")
    print()

    # Step 1: Initialize the store
    store = Store()
    
    # Step 2: Add a customer to the store customer records
    customer1 = Customer("Mouza", "mouza@example.com", loyalty_member=True)
    store.add_customer(customer1)
    print("Added customer: " + str(customer1))

    # Step 3: Modify the customer name
    customer1.set_name("Mouza Alia")
    print("Modified customer name: " + customer1.get_name())
    
    # Step 4: Remove the customer from the records
    store.remove_customer("Mouza Alia")

    # Print customer list to confirm removal
    customer_names = []
    for customer in store.get_customer_list():
        customer_names.append(customer.get_name())

    customer_names_str = ""
    for name in customer_names:
        customer_names_str += name + ", "

    # Remove the comma and space
    if customer_names_str.endswith(", "):
        customer_names_str = customer_names_str[:-2]

    print("Customer list after removal: " + customer_names_str + "\n")

def test_add_ebooks_to_cart():
    print("=== Testing Adding E-books to Cart ===")
    
    # Step 1: Initialize the store and a customer
    store = Store()
    customer1 = Customer("Jawaher", "jawaher@example.com", loyalty_member=True)
    store.add_customer(customer1)
    
    # Step 2: Create ebooks and add them to the store catalog
    ebook1 = Ebook("Data Science", "Ali", "2022-06-15", "Education", 25.0)
    ebook2 = Ebook("Machine Learning", "Khalifa", "2023-09-21", "Education", 30.0)
    store.add_ebook(ebook1)
    store.add_ebook(ebook2)
    
    # Step 3: Add ebooks to the customer cart
    cart = Cart(customer1)
    cart.add_item(ebook1)
    cart.add_item(ebook2)

    # Print cart contents to confirm addition
    item_titles = []
    for item in cart.get_items():
        item_titles.append(item.get_title())

    item_titles_str = ""
    for title in item_titles:
        item_titles_str += title + ", "

    # Remove the comma and space
    if item_titles_str.endswith(", "):
        item_titles_str = item_titles_str[:-2]

    print("Cart contents after adding items: " + item_titles_str + "\n")

def test_apply_discounts():
    print("=== Testing Applying Discounts ===")
    print()

    # Step 1: Initialize a customer and their cart
    customer1 = Customer("Saeed", "saeed@example.com", loyalty_member=True)
    cart = Cart(customer1)
    
    # Step 2: Add multiple item to the cart
    ebook1 = Ebook("Algorithms", "Hamdan", "2021-11-11", "Education", 40.0)
    ebook2 = Ebook("Advanced Math", "Fatima", "2022-08-08", "Education", 50.0)
    ebook3 = Ebook("Quantum Physics", "Aisha", "2023-05-05", "Science", 45.0)
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    cart.add_item(ebook3)
    
    # Step 3: Apply loyalty discount and calculate the total
    total_with_loyalty_discount = cart.calculate_total(apply_discount=True)
    print("Total with loyalty discount (10%): $" + format(total_with_loyalty_discount, ".2f"))
    
    # Step 4: Add more items to qualify for bulk discount 5+ five items
    cart.add_item(Ebook("Chemistry", "Zayed", "2022-10-10", "Science", 30.0))
    cart.add_item(Ebook("Biology", "Mashael", "2023-03-03", "Science", 35.0))
    
    # Step 5: Calculate total with both loyalty and bulk discounts applied
    total_with_bulk_discount = cart.calculate_total(apply_discount=True)
    print("Total with loyalty + bulk discount (20% for 5+ items): $" + format(total_with_bulk_discount, ".2f") + "\n")

def test_invoice_generation():
    print("=== Testing Invoice Generation ===")
    print()

    # Step 1: Initialize customer and their cart
    customer1 = Customer("Zayed", "zayed@example.com", loyalty_member=True)
    
    # Step 2: Create ebooks and add them to the cart
    ebook1 = Ebook("Artificial Intelligence", "Ahmad", "2023-07-07", "Technology", 55.0)
    ebook2 = Ebook("Blockchain Basics", "Alyazya", "2022-02-02", "Technology", 45.0)
    cart = Cart(customer1)
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    
    # Step 3: Set the order date for the cart
    cart.set_order_date("2024-11-06")
    
    # Step 4: Generate the invoice with detailed order information
    invoice = Invoice(customer1, cart)
    print("Generated Invoice:")
    print(invoice.generate_invoice())

def main():
    print("=== Running All Test Cases ===\n")
    # Run each test case function to verify all features
    test_add_modify_remove_ebook()
    test_add_modify_remove_customer()
    test_add_ebooks_to_cart()
    test_apply_discounts()
    test_invoice_generation()

# execute call main function 
if __name__ == "__main__":
    main()
