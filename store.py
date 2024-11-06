from ebook import Ebook
from customer import Customer
from cart import Cart
from invoice import Invoice

class Store:

    def __init__(self):
        self.__ebooks = []
        self.__customers = []

    def add_ebook(self, ebook):
        # Adds an ebook to the store catalog
        self.__ebooks.append(ebook)

    def remove_ebook(self, title):
        # Create an empty list to store ebooks after filtering
        filtered_ebooks = []

        # Iterate through the existing ebooks
        for ebook in self.__ebooks:
            # Check if the ebook title does not match the given title
            if ebook.get_title() != title:
                # If it does not match add the ebook to the filtered list
                filtered_ebooks.append(ebook)

        # Update the __ebooks list with the filtered ebooks
        self.__ebooks = filtered_ebooks

    def add_customer(self, customer):
        # Adds a customer to the store records
        self.__customers.append(customer)

    def remove_customer(self, name):
        # Remove a customer from the store by name
        # Create an empty list to store customer after filtering
        filtered_customers = []

        # Iterate through the existing customer
        for customer in self.__customers:
            # Check if the customer name does not match the given name
            if customer.get_name() != name:
                # If it does not match add the customer to the filtered list
                filtered_customers.append(customer)

        # Update the __customers list with the filtered customers
        self.__customers = filtered_customers

    def get_ebook_catalog(self):
        # Returns the store ebook catalog
        return self.__ebooks

    def get_customer_list(self):
        # Returns the list of customers
        return self.__customers

    def __str__(self):
        # Create a string summary of the store current state using string concatenation
        return "Store with " + str(len(self.__ebooks)) + " e-books and " + str(len(self.__customers)) + " customers."

