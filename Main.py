import multiprocessing as mp
from Assignment1 import Assignment1

if __name__ == "__main__":
    mp.freeze_support()
    sim = Assignment1()
    sim.startSimulation()
