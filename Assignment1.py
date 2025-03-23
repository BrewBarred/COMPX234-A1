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

    # Initialise simulation variables
    def __init__(self):
        self.sim_active = mp.Value('b', True)
        self.print_list = printList()  # Create an empty list of print requests
        self.mThreads = []  # list for machine threads
        self.pThreads = []  # list for printer threads

    def startSimulation(self):
        # Create Machine and Printer threads
        # Write code here`
        # for every machine
        for i in range(6):
            # create a new machine process
            machine = self.machineThread(i, self.sim_active, self.print_list)
            # define the machine processes calling function
            m_process = mp.Process(target=machine.run)
            # add the new process to a list to easily track current processes
            self.mThreads.append(m_process)

        # create a manager to share lists between processes
        manager = mp.Manager()
        # setup inter-process communication
        self.mThreads = manager.list()
        self.pThreads = manager.list()



        # # for every machine
        # for i in range(self.NUM_MACHINES):
        #     # create a new machine process
        #     process = mp.Process(target=self.machineThread.run, args=(i, self))
        #     # add this machine process the machine process list for tracking
        #     self.mThreads.append(process)
        #
        # # for every printer
        # for i in range(self.NUM_PRINTERS):
        #     # create a new printer process
        #     process = mp.Process(target=self.printerThread.run, args=(i, ))
        #     # add this printer process to the printer process list for tracking
        #     self.pThreads.append(process)

        # Start all the threads
        # Write code here
        for process in self.mThreads:  #+ self.pThreads:
            print(f"Starting process: {process}")
            process.start()

        # Let the simulation run for some time
        print("Sleeping...")
        time.sleep(self.SIMULATION_TIME)
        print("Finished sleeping!")

        # Finish simulation
        self.sim_active = False

        # Wait until all printer threads finish by joining them
        # Write code here
        # for process in self.mThreads + self.pThreads:
        #     process.join()

    # Printer class
    class printerThread(mp.Process):
        MAX_PRINTER_SLEEP = 3  # Maximum sleep time for printers

        def __init__(self, printer_id, sim_active, print_list):
            #mp.Process.__init__(self)
            super().__init__()
            # reference to multi-process variables
            self.printer_id = printer_id
            self.sim_active = sim_active
            self.print_list = print_list
            print(f"Created printer process {self.printer_id}")

        def run(self):
            print(f"Running printer thread {self.printerID}")
            while self.sim_active:
                # Simulate printer taking some time to print the document
                self.printerSleep()
                # Grab the request at the head of the queue and print it
                # Write code here

        def printerSleep(self):
            print(f"Sleeping printer thread {self.printer_id}")
            sleepSeconds = random.randint(1, self.MAX_PRINTER_SLEEP)
            time.sleep(sleepSeconds)

        def printDox(self, printerID):
            print(f"Printer ID: {printerID} : now available")
            # Print from the queue
            self.print_list.queuePrint(printerID)

    # Machine class
    class machineThread(mp.Process):
        MAX_MACHINE_SLEEP = 5  # Maximum sleep time for machines

        def __init__(self, machine_id, sim_active, print_list):
            super().__init__()
            # reference to multiprocess variables
            self.machine_id = machine_id
            self.sim_active = sim_active
            self.print_list = print_list
            print(f"Created machine process {self.machine_id}")

        def run(self):
            print(f"Running machine thread {self.machine_id}")
            while self.sim_active:
                # Machine sleeps for a random amount of time
                self.machineSleep()
                # Machine wakes up and sends a print request
                # Write code here
                self.printRequest()

        def machineSleep(self):
            sleepSeconds = random.randint(1, self.MAX_MACHINE_SLEEP)
            time.sleep(sleepSeconds)

        def printRequest(self):
            print(f"Machine {id} Sent a print request")
            # Build a print document
            doc = printDoc(f"My name is machine {self.machine_id}", self.machine_id)
            # Insert it in the print queue
            self.print_list.queueInsert(doc)
