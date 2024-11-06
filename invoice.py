class Invoice:
    def __init__(self, customer, cart):
        """Initialize the Invoice with a customer and their cart"""
         # Store customer information
        self.__customer = customer 
        # Store cart information
        self.__cart = cart          

    def generate_invoice(self):
        """Generates a detailed invoice for the cart's contents"""
        # Check if the customer is a loyalty member for discount eligibility
        apply_discount = self.__customer.is_loyalty_member()  
        
        # Calculate the total cost of items in the cart including any applicable discount
        total = self.__cart.calculate_total(apply_discount)
        
        # Start building the invoice details string
        invoice_details = "Customer: " + self.__customer.get_name() + "\n"
        invoice_details += "Items:\n"
        
        # Append each item in the cart to the invoice details
        for item in self.__cart.get_items():
            invoice_details += "- " + item + "\n"
        
        # Add the total cost to the invoice details g
        invoice_details += "Total with VAT: $" + str(round(total, 2)) + "\n"
        
        # Return the complete invoice details
        return invoice_details  

    def __str__(self):
        """Returns the invoice as a string"""
        # Generate and return the invoice as a string
        return self.generate_invoice()  
