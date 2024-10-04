class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0,value)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

def hot_potato(name_list,num):
    sim_queue = CustomQueue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
        print(sim_queue)
    return sim_queue.dequeue()

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_rear(self, value):
        self.items.insert(0, value)

    def add_front(self, value):
        self.items.append(value)

    def remove_rear(self):
        return self.items.pop()

    def remove_front(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == '__main__': print(hot_potato(["A","B",'C',"D","E","F"],1))


