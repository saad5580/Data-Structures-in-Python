"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue


def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    target = Queue()
    for _ in range(len(source1) - 1, -1, -1):
        target.insert(source1.remove())

    for _ in range(len(source2) - 1, -1, -1):
        target.insert(source2.remove())
    return target


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    # for value in range(len(source) - 1, -1, -1):
    #     if value > key:
    #         target1.insert(source.remove(value))
    #     elif value < key:
    #         target2.insert(source.remove(value))
    value = 0
    while not source.is_empty():
        value = source.remove()
        if value > key:
            target1.insert(value)
        elif value <= key:
            target2.insert(value)

    return target1, target2
