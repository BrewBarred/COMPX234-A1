import marshal
import multiprocessing as mp
from multiprocessing import Pool, freeze_support
import pickle
import time
import random
import types
import time
from multiprocessing.managers import BaseManager

from printDoc import printDoc
from printList import printList

# Counting semaphore – integer value can range over an unrestricted domain
# • Counting semaphores can be used to control access to a given resource consisting of a finite
# number of instances.
# • The semaphore is initialized to the number of resources available.
# • Each process that wishes to use a resource performs a wait() operation on the semaphore
# (thereby decrementing the count).
# • When a process releases a resource, it performs a signal() operation (incrementing the
# count).

PRINT_LIST = printList()


class Assignment1:
    # Simulation Initialisation parameters
    NUM_MACHINES = 50  # Number of machines that issue print requests
    NUM_PRINTERS = 5  # Number of printers in the system
    # TODO: Change back to 30 seconds before submission
    SIMULATION_TIME = 7  # Total simulation time in seconds
    MAX_PRINTER_SLEEP = 3    # Maximum sleep time for printers
    MAX_MACHINE_SLEEP = 5    # Maximum sleep time for machines

    # Initialise simulation variables
    def __init__(self):
        self.sim_active = None
        self.print_list = printList()  # Create an empty list of print requests
        self.mThreads = []  # list for machine threads
        self.pThreads = []  # list for printer threads

    def startSimulation(self):
        print("Creating manager...")

        # #freeze_support()
        # with BaseManager() as manager:
        #     manager.register('printList', printList)
        #     manager.start()
        #     queue = manager.printList()
        # Register the custom linked list
        BaseManager.register('printList', printList)
        manager = BaseManager()
        manager.start()
        self.print_list = manager.printList()
        self.print_list.queuePrintAll()

        print("Manager started successfully!")
        # # create a manager to share lists between processes
        # # BaseManager.register("sim_active", mp.Value('b', True))
        # # BaseManager.register("mThreads", mp.Manager().list)
        # # BaseManager.register("pThreads", mp.Manager().list)
        # # BaseManager.register("printList", printList)
        # # manager = BaseManager()
        # # manager.start()
        # lock = mp.Lock()
        # print("Setting up inter-process lists...")
        # # self.print_list = manager.Queue()
        # # self.mThreads = manager.list()
        # # self.pThreads = manager.list()
        # 
        # print("Creating machine threads...")
        # ids = ((i + 1) for i in range(self.NUM_MACHINES))
        # print(f"IDs: {ids}")
        # 
        # for i in range(self.NUM_MACHINES):
        #     machine = self.machineThread(i + 1, self)
        #     process = mp.Process(target=machine.run)
        #     self.mThreads.append(process)
            #mp.Process(target=machine.run, args=(self,))

        # with mp.Pool(self.NUM_MACHINES) as pool:
        #     machine = self.machineThread(ids, self)
        #     pool.map(machine.run, ids)
            #pool.map(self.machineThread.run, ids)
            # pool.starmap(self.machineThread.run, self)
            # self.mThreads.append(self.machineThread(i + 1, self.sim_active, self.print_list))

        #TODO: Confirm if this is supposed to be a QUEUE object or not
        # setup inter-process communication for synchronization
        #self.print_list = manager.Queue()

        # Create Machine and Printer threads
        # Write code here`
        # for every machine
        # for i in range(self.NUM_MACHINES):
        #     # create a new machine object
        #     machine = self.machineThread(i + 1, self)
        #     # use the new machine to create a new process
        #     m_process = mp.Process(target=machine.run)
        #     print(m_process)
        #     # add the new process to machine list for tracking
        #     self.mThreads.append(m_process)
        #
        # print("Creating printer threads...")
        # # for every printer
        # for i in range(self.NUM_PRINTERS):
        #     # create a new printer object
        #     printer = self.printerThread(i + 1, self)
        #     # use the new machine to create a new process
        #     p_process = mp.Process(target=printer.run)
        #     # add the new process to printer list for tracking
        #     self.pThreads.append(p_process)

        # print(f"Attempting to start all processes... Machine threads: {len(self.mThreads)}, Printer threads: {len(self.pThreads)}")
        # # Start all the threads
        # # Write code here
        # for process in self.mThreads:
        #     print(f"Starting process: {process}...")
        #     process.start()
        #     print("Process started!")
        # for each process in the machine and print thread lists
        # for process in self.pThreads:
        #     # start the process
        #     print(f"Starting process: {process}")
        #     process.start()

        # let the simulation run for some time
        time.sleep(self.SIMULATION_TIME)

        # Finish simulation
        self.sim_active = False

        # Wait until all printer threads finish by joining them
        # Write code here
        # for process in self.mThreads + self.pThreads:
        #     process.join()
        print("Processing complete!")

    class PrintListManager(BaseManager):
        pass

    # Machine class
    class machineThread(mp.Process):
        def __init__(self, machineID, outer):
            super().__init__()
            self.machineID = machineID
            self.outer = outer
            # self.sim_active = sim_active
            # self.print_list = print_list

        def run(self):
            while self.outer.sim_active:
                # Machine sleeps for a random amount of time
                self.machineSleep()
                # Machine wakes up and sends a print request
                # Write code here
                self.printRequest(self.machineID)

        def machineSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_MACHINE_SLEEP)
            time.sleep(sleepSeconds)

        def printRequest(self, id):
            print(f"Machine {id} Sent a print request")
            # Build a print document
            doc = printDoc(f"My name is machine {id}", id)
            # Insert it in the print queue
            self.outer.print_list.queueInsert(doc)

    class printerThread(mp.Process):
        # def __init__(self, printerID, outer):
        #     super().__init__()
        #     self.printerID = printerID
        #     self.outer = outer  # Reference to the Assignment1 instance
        def __init__(self, printerID, outer):
            super().__init__()
            self.printerID = printerID
            self.outer = outer
            # self.sim_active = sim_active
            # self.print_list = print_list

        def run(self):
            while self.outer.sim_active:
                # Simulate printer taking some time to print the document
                self.printerSleep()
                # Grab the request at the head of the queue and print it
                # Write code here
                self.printDox(self.printerID)

        def printerSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_PRINTER_SLEEP)
            time.sleep(sleepSeconds)

        def printDox(self, printerID):
            print(f"Printer ID: {printerID} : now available")
            # Print from the queue
            self.outer.print_list.queuePrint(printerID)

        # def __getstate__(self):
        #     """called when pickling - this hack allows subprocesses to
        #        be spawned without the AuthenticationString raising an error"""
        #     state = self.__dict__.copy()
        #     conf = state['_config']
        #     if 'authkey' in conf:
        #         #del conf['authkey']
        #         conf['authkey'] = bytes(conf['authkey'])
        #     return state
        #
        # def __setstate__(self, state):
        #     """for unpickling"""
        #     state['_config']['authkey'] = AuthenticationString(state['_config']['authkey'])
        #     self.__dict__.update(state)
