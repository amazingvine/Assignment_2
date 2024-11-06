class Cart:

    def __init__(self, customer):
        self.__customer = customer
        self.__items = []
        self.__order_date = None

    def add_item(self, ebook):
        # Adds an ebook to the cart
        self.__items.append(ebook)

    def remove_item(self, ebook_title):
        # Removes an ebook from the cart by title
        # Create an empty list to store the filtered items
        filtered_items = []

        # Iterate through the existing items in the cart
        for ebook in self.__items:
            # Check if the ebook title does not match the given title
            if ebook.get_title() != ebook_title:
                # If it does not match add the ebook to the filtered list
                filtered_items.append(ebook)

        # Update the __items list with the filtered items
        self.__items = filtered_items

    def get_items(self):
        # Returns the items in the cart
        return self.__items

    def set_order_date(self, order_date):
        # Sets the order date for the cart
        self.__order_date = order_date

    def get_order_date(self):
        # Returns the order date of the cart
        return self.__order_date

    def calculate_total(self, apply_discount=False):
        # Calculates the total price with optional discounts and VAT
        total = sum(item.get_price() for item in self.__items)
        if apply_discount:
            total *= 0.9
        if len(self.__items) >= 5:
            total *= 0.8
        # Including VAT
        return total * 1.08  

    def __str__(self):
        # Returns a string representation of the cart details
        return "Cart with " + str(len(self.__items)) + " items for customer " + self.__customer.get_name()
