class Customer:

    def __init__(self, name, contact_info, loyalty_member=False):
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_member = loyalty_member
        self.__cart = []

    def get_name(self):
        # Returns the name of the customer
        return self.__name

    def set_name(self, name):
        # Sets the name of the customer
        self.__name = name

    def is_loyalty_member(self):
        # Returns whether the customer is a loyalty member
        return self.__loyalty_member

    def add_to_cart(self, ebook):
        # Adds an ebook to the customer cart
        self.__cart.append(ebook)

    def remove_from_cart(self, ebook_title):
        # Removes an ebook from the customer cart by title
        # Create an empty list to store the filtered cart items
        filtered_cart = []

        # Iterate through the existing cart
        for ebook in self.__cart:
            # Check if the ebook title does not match the given title
            if ebook.get_title() != ebook_title:
                # If it does not match, add the ebook to the filtered cart
                filtered_cart.append(ebook)

        # Update the __cart with the filtered cart
        self.__cart = filtered_cart

    def get_cart(self):
        # Returns the items in the customer cart
        return self.__cart

    def clear_cart(self):
        # Clears the customer cart
        self.__cart = []

    def __str__(self):
        # Returns a string representation of the customer details
        return "Customer: " + self.__name + ", Loyalty Member: " + str(self.__loyalty_member)

