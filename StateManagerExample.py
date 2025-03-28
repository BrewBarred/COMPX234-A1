from multiprocessing import Manager, Process, freeze_support, Pool


# Define a function that adds items to a shared list
def add_to_list(shared_list):
    for i in range(5):
        shared_list.append(i)
        print(f"Added {i} to list")

if __name__ == '__main__':
    freeze_support()

    # Create a manager object
    with Manager() as manager:
        # Create a shared list
        shared_list = manager.list()

        # Create and start multiple processes
        processes = [Process(target=add_to_list, args=(shared_list,)) for _ in range(3)]
        for process in processes:
            process.start()

        # Wait for all processes to complete
        for process in processes:
            process.join()

        # Print the shared list
        print(f"Shared list: {list(shared_list)}")

    with Pool(5) as p:
        print(p.map(add_to_list, [shared_list,]))
