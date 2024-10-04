from customer import Customer
class CustomerCheckout:
    """
    Represents the customer queue at the checkout.

    Methods:
    -------
    add_customer(customer): Adds a customer to the queue.
    get_customers(): Retrieves and removes the customer at the front of the queue.
    is_empty(): Checks if the queue is empty.
    size(): Returns the number of customers in the queue.
    __str__(): Returns a string representation of the queue.
    """
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        """
        Adds a customer to the checkout queue.
        """
        self.customers.append(customer)

    def get_customers(self):
        """
        Removes and returns the next customer in the queue.
        """
        if not self.is_empty():
            return self.customers.pop(0) #Serve the customer at the front of the queue
        raise IndexError('No customers in line')

    def size(self):
        return len(self.customers)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.customers) == 0

    def __str__(self):
        return f"Queue Size: {self.size()}, Customers: {[str(c) for c in self.customers]}"
