import multiprocessing as mp
from multiprocessing.managers import BaseManager

from printList import printList


class MyManager(BaseManager):
    pass

# Register the custom linked list
MyManager.register('printList', printList)

def startSimulation():
    print("Creating manager...")

    mp.set_start_method("spawn", True)  # ✅ Windows-friendly

    manager = MyManager()
    manager.start()  # ✅ Start manager before using it

    queue = manager.printList()  # ✅ Now you can share the custom linked list

    print("Manager started successfully!")
    return queue  # You can return it for other processes to use

if __name__ == "__main__":
    queue = startSimulation()
