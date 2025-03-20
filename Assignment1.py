import multiprocessing as mp
import time
import random

from printDoc import printDoc
from printList import printList


class Assignment1:
    # Simulation Initialisation parameters
    NUM_MACHINES = 50  # Number of machines that issue print requests
    NUM_PRINTERS = 5  # Number of printers in the system
    SIMULATION_TIME = 30  # Total simulation time in seconds
    MAX_PRINTER_SLEEP = 3  # Maximum sleep time for printers
    MAX_MACHINE_SLEEP = 5  # Maximum sleep time for machines

    # Initialise simulation variables
    def __init__(self):
        self.sim_active = True
        self.print_list = printList()  # Create an empty list of print requests
        self.mThreads = []  # list for machine threads
        self.pThreads = []  # list for printer threads

    def startSimulation(self):
        # Create Machine and Printer threads
        # Write code here
        for i in range(6):
            machine = self.machineThread(i, self)
            m_process = mp.Process(target=machine.run)
            self.mThreads.append(m_process)



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
        for process in self.mThreads + self.pThreads:
            print(f"Starting process: {process}")
            process.run()

        # Let the simulation run for some time
        print("Sleeping...")
        time.sleep(self.SIMULATION_TIME)
        print("Finished sleeping!")

        # Finish simulation
        self.sim_active = False

        # Wait until all printer threads finish by joining them
        # Write code here
        for process in self.mThreads + self.pThreads:
            process.join()

    # Printer class
    class printerThread(mp.Process):
        def __init__(self, printerID, outer):
            #mp.Process.__init__(self)
            super().__init__()
            self.printerID = printerID
            self.outer = outer  # Reference to the Assignment1 instance
            print(f"Created printer process {printerID}")

        def run(self):
            print(f"Running printer thread {self.printerID}")
            while self.outer.sim_active:
                # Simulate printer taking some time to print the document
                self.printerSleep()
                # Grab the request at the head of the queue and print it
                # Write code here

        def printerSleep(self):
            print(f"Sleeping printer thread {self.printerID}")
            sleepSeconds = random.randint(1, self.outer.MAX_PRINTER_SLEEP)
            time.sleep(sleepSeconds)

        def printDox(self, printerID):
            print(f"Printer ID: {printerID} : now available")
            # Print from the queue
            self.outer.print_list.queuePrint(printerID)

    # Machine class
    class machineThread():
        def __init__(self, machineID, outer):
            super().__init__()
            #mp.Process.__init__(self)
            self.machineID = machineID
            self.outer = outer  # Reference to the Assignment1 instance
            print(f"Created machine process {machineID}")

        def run(self):
            print(f"Running machine thread {self.machineID}")
            while self.outer.sim_active:
                # Machine sleeps for a random amount of time
                self.machineSleep()
                # Machine wakes up and sends a print request
                # Write code here
                self.printRequest()

        def machineSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_MACHINE_SLEEP)
            time.sleep(sleepSeconds)

        def printRequest(self):
            print(f"Machine {id} Sent a print request")
            # Build a print document
            doc = printDoc(f"My name is machine {self.machineID}", self.machineID)
            # Insert it in the print queue
            self.outer.print_list.queueInsert(doc)
