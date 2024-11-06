class Discount:
    
    # Handles discount calculations for loyalty members and bulk purchases

    @staticmethod
    def loyalty_discount(total):
        # Applies a 10% discount for loyalty members
        return total * 0.9

    @staticmethod
    def bulk_discount(total):
        # Applies a 20% discount for bulk orders 5+ items
        return total * 0.8
