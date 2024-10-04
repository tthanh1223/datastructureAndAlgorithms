from ADT_abstract_data_type.my_queue import CustomQueue
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