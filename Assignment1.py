import multiprocessing as mp
from multiprocessing import Process as process
import time
import random
from multiprocessing import Pool

from printDoc import printDoc
from printList import printList

class Assignment1:
    # Simulation Initialisation parameters
    NUM_MACHINES = 50        # Number of machines that issue print requests
    NUM_PRINTERS = 5         # Number of printers in the system
    SIMULATION_TIME = 30     # Total simulation time in seconds
    MAX_PRINTER_SLEEP = 3    # Maximum sleep time for printers
    MAX_MACHINE_SLEEP = 5    # Maximum sleep time for machines

    # Initialise simulation variables
    def __init__(self):
        self.sim_active = True
        self.print_list = printList()  # Create an empty list of print requests
        self.mProcesses = []             # list for machine processes
        self.pProcesses = []             # list for printer processes

    def startSimulation(self):
        # Create Machine and Printer threads
        # Write code here

        # for each machine available
        for _ in range(self.NUM_MACHINES):
            # start a new process
            process(target="")



        # Start all the threads
        # Write code here

        # Let the simulation run for some time
        time.sleep(self.SIMULATION_TIME)

        # Finish simulation
        self.sim_active = False

        # Wait until all printer threads finish by joining them
        # Write code here

    # Printer class
    class printerThread(mp.Process):
        def __init__(self, printerID, outer):
            mp.Process.__init__(self)
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
            mp.Process.__init__(self)
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

"""
    Task 1: Your first task is to use the starter code given in Assignment1Task and
            implement the following bevahiour for the machines and printers. Implement the machines
            and printers as threads in Java and processes in Python.
    
        1. The machines sleep for some time and then wake up and send a print request.
        2. Printers also sleep for some time. When they wake up they print the document at the
           head of the queue.
        
        
    Example output:
    
        Machine 21 Sent a print request
        Machine 22 Sent a print request
        Inserted a request in the queue from 22
        !!!!!!Attention: Overwrite!!!!!!
        Number of requests in the queue 5
        Machine 11 Sent a print request
        Inserted a request in the queue from 11
        !!!!!!Attention: Overwrite!!!!!!
        
    Task 2: Your second task is to design and implement a solution using the synchronization
            solutions discussed in the lectures to resolve the problem of overwriting. Your solution will,

        1. Control the machines’ access to the print queue such that no overwriting takes place.
           We consider that the size of our queue is 5. If there are 5 messages in the queue
           already, then no machine should be allowed to send a print request, until a printer
           prints one of the messages and makes space available.
        2. Control the machines’ and printers’ access to the print queue such that no two devices
           (machines and printers) are accessing the queue at the same time.
           
"""