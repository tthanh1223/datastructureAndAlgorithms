from customer_checkout import CustomerCheckout
class Cashier:
    """
    Represents the cashier at the checkout.
    Attributes:
    ----------
    line : CustomerCheckout
        The queue of customers waiting to be served.
    current_customer : Customer
        The customer currently being served.
    time_remaining : int
        Time remaining to finish serving the current customer.

    Methods:
    -------
    add_customer_to_line(customer): Add a customer to the cashier's line.
    serve_next_customer(): Serves the next customer in line.
    tick(): Decreases the time remaining for the current customer.
    busy(): Checks if the cashier is currently busy serving a customer.
    __str__(): Returns a string representation of the cashier's status.
    """
    def __init__(self):
        self.line = CustomerCheckout()
        self.current_customer = None
        self.time_remaining = 0

    def add_customer_to_line(self, customer):
        """Adds a customer to the cashier's line."""
        self.line.add_customer(customer)

    def serve_next_customer(self):
        """Serves the next customer in the cashier's line."""
        if self.line.is_empty():
            return None
        self.current_customer = self.line.get_customers()
        self.time_remaining = self.current_customer.service_time

    def tick(self):
        """Decreases the time remaining for the current customer and return the customer"""
        if self.current_customer:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                finished_customer = self.current_customer
                self.current_customer = None
                return finished_customer
        return None

    def busy(self):
        """Checks if the cashier is currently busy serving a customer."""
        return self.current_customer is not None

    def __str__(self):
        return f"Cashier (Busy: {self.busy()})"
