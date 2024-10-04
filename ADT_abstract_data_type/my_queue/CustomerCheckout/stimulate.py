import random
from cashier import *  # Ensure you have the Cashier class and necessary functions defined
from customer import Customer

def new_customer_arrival(current_second):
    """Randomly decides if a new customer arrives with a 20% chance."""
    if 3600 <= current_second < 7200:  # Between 1 hour and 2 hours (e.g., busy time)
        return random.randrange(1, 61) == 1  # More frequent arrivals
    else:
        return random.randrange(1, 181) == 1  # Normal frequency


def simulate_checkout(num_seconds, num_cashiers):
    """
    Simulates the customer checkout process.

    Parameters:
    ----------
    num_seconds : int
        The duration of the simulation in seconds.
    num_cashiers : int
        The number of cashiers available to serve customers.

    Returns: None
    """
    cashiers = [Cashier() for _ in range(num_cashiers)]
    waiting_times = []
    customers_served = 0

    for current_second in range(num_seconds):
        # Check if a new customer arrives
        if new_customer_arrival(current_second):
            customer = Customer(customers_served + 1)
            # Find the cashier with the shortest line
            chosen_cashier = min(cashiers, key=lambda c: c.line.size())
            chosen_cashier.add_customer_to_line(customer)

        # Process each cashier
        for cashier in cashiers:
            if not cashier.busy() and not cashier.line.is_empty():
                cashier.serve_next_customer()  # Serve the next customer

            finished_cashier = cashier.tick()  # Process the current customer
            if finished_cashier:
                waiting_times.append(finished_cashier.service_time)  # Track service time
                customers_served += 1

    # Calculate and print average waiting time
    average_wait = sum(waiting_times) / len(waiting_times) if waiting_times else 0
    print(f'Average wait time: {average_wait:.2f} seconds, Customers served: {customers_served}')


if __name__ == '__main__':
    for i in range(10):
        print(f"Simulation {i + 1}: ", end='')
        simulate_checkout(18 * 60 * 60, 12)  # 18 hours simulation with 12 cashiers
