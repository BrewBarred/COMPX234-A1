import multiprocessing as mp
import time
import random

from printDoc import printDoc
from printList import printList


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
        self.sim_active = mp.Value('b', True)
        self.print_list = printList()  # Create an empty list of print requests
        self.mThreads = []  # list for machine threads
        self.pThreads = []  # list for printer threads

    def startSimulation(self):
        print("Creating manager...")
        # create a manager to share lists between processes
        manager = mp.Manager()
        # setup inter-process communication for synchronization
        self.mThreads = manager.list()
        self.pThreads = manager.list()
        # Create Machine and Printer threads
        # Write code here`
        # for every machine
        for i in range(self.NUM_MACHINES):
            # create a new machine object
            machine = self.machineThread(i + 1, self)
            # use the new machine to create a new process
            m_process = mp.Process(target=machine.run)
            # add the new process to machine list for tracking
            self.mThreads.append(m_process)

        # for every printer
        for i in range(self.NUM_PRINTERS):
            # create a new printer object
            printer = self.printerThread(i + 1, self)
            # use the new machine to create a new process
            p_process = mp.Process(target=printer.run)
            # add the new process to printer list for tracking
            self.pThreads.append(p_process)

        print(f"Attempting to start all processes... Machine threads: {len(self.mThreads)}, Printer threads: {len(self.pThreads)}")
        # Start all the threads
        # Write code here
        # for each process in the machine and print thread lists
        # for process in self.mThreads and self.pThreads:
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

    class printerThread(mp.Process):
        def __init__(self, printerID, outer):
            super().__init__()
            self.printerID = printerID
            self.outer = outer  # Reference to the Assignment1 instance

        def run(self):
            while self.outer.sim_active:
                # Simulate printer taking some time to print the document
                self.printerSleep()
                # Grab the request at the head of the queue and print it
                # Write code here

        def printerSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_PRINTER_SLEEP)
            time.sleep(sleepSeconds)

        def printDox(self, printerID):
            print(f"Printer ID: {printerID} : now available")
            # Print from the queue
            self.outer.print_list.queuePrint(printerID)

    # Machine class
    class machineThread(mp.Process):
        def __init__(self, machineID, outer):
            super().__init__()
            self.machineID = machineID
            self.outer = outer  # Reference to the Assignment1 instance

        def run(self):
            while self.outer.sim_active:
                # Machine sleeps for a random amount of time
                self.machineSleep()
                # Machine wakes up and sends a print request
                # Write code here

        def machineSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_MACHINE_SLEEP)
            time.sleep(sleepSeconds)

        def printRequest(self, id):
            print(f"Machine {id} Sent a print request")
            # Build a print document
            doc = printDoc(f"My name is machine {id}", id)
            # Insert it in the print queue
            self.outer.print_list.queueInsert(doc)
