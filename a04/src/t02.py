"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from functions import queue_combine
from Queue_array import Queue

source1 = Queue()
source2 = Queue()

source1.insert(1)
source1.insert(2)
source1.insert(3)
source1.insert(4)
source1.insert(5)


source2.insert(6)
source2.insert(7)
source2.insert(8)
source2.insert(9)
source2.insert(10)

target = queue_combine(source1, source2)

for value in target:
    print(value)
