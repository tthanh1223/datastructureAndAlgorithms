from ADT_abstract_data_type.my_queue import CustomQueue
import random


def hot_potato(name_list, num):
    """
    Simulates the Hot Potato game with a fixed counting number.

    Parameters:
    ----------
    name_list : list
        A list of names representing participants in the game.
    num : int
        The number of passes before the potato is removed.

    Returns:
    --------
    str
        The name of the last remaining participant.
    """
    sim_queue = CustomQueue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())  # Pass the potato
        sim_queue.dequeue()  # Remove the potato from the queue
        print(sim_queue)  # Print the current state of the queue

    return sim_queue.dequeue()  # Return the last participant


def hot_potato_randomly(name_list):
    """
    Simulates the Hot Potato game with a randomly chosen counting value for each pass.

    Parameters:
    ----------
    name_list : list
        A list of names representing participants in the game.

    Returns:
    --------
    str
        The name of the last remaining participant.
    """
    sim_queue = CustomQueue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        # Randomly choose the number of passes between 0 and the size of the queue
        for i in range(random.randint(0, len(name_list))):
            sim_queue.enqueue(sim_queue.dequeue())  # Pass the potato
        sim_queue.dequeue()  # Remove the potato

    return sim_queue.dequeue()  # Return the last participant


if __name__ == '__main__':
    name_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    winner = hot_potato_randomly(name_lst)
    print(f"The winner is: {winner}")
