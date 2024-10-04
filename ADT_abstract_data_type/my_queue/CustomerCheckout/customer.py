import random

class Customer:
    """
    Represents a customer in the grocery store checkout simulation.

    Attributes:
    ----------
    id : int
        Unique identifier for the customer.
    arrival_time : int
        Time the customer arrives at the checkout.
    number_of_items : int
        Number of items the customer wants to purchase.
    service_time : int
        Time required to serve the customer, calculated based on the number of items.

    Methods:
    -------
    __str__():
        Returns a string representation of the customer.
    """
    def __init__(self, id):
        self.id = id
        self.arrival_time = 0
        self.number_of_items = random.randint(1, 50)
        self.service_time = self.number_of_items * 2

    def __str__(self):
        return f"Customer {self.id} buy {self.number_of_items} items costs {self.service_time} seconds"


