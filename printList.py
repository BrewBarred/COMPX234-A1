from printDoc import printDoc


class printList:
    class Node:
        # Constructor
        def __init__(self, doc):
            #
            self.document = doc
            # head of the list
            self.next = None

    def __init__(self):
        # the maximum number of documents that can be in the queue
        self.MAX_SIZE = 5
        # the current size of the queue
        self.queue_size = 0
        # the first document in the queue
        self.head = None
        # the last document in the queue
        self.tail = None

    # Insert a print request in the queue
    def queueInsert(self, doc):
        # create a node that can be added to the queue using the passed doc
        new_node = printList.Node(doc)
        # if the queue is empty, start a queue
        if self.head is None:
            self.head = new_node
        # else if the queue has a head, but no tail
        elif self.tail is None:
            self.tail = new_node
        # else, the queue is full, replace the tail
        elif self.queue_size >= self.MAX_SIZE:
            print("!!!!!!Attention: Overwrite!!!!!!")
            self.tail.next = new_node

        # increment request count to easily find tail of queue
        self.queue_size = self.queue_size + 1
        print(f"Inserted a request in the queue from {new_node.document.getSender()}\n"
              f"Number of requests in the queue {self.queue_size}")

        # return the new_node incase it is needed
        return new_node

    # Method to print the head of the list
    def queuePrint(self, printerID):
        # Only print if there is a node in the list
        if self.head is not None:
            currNode = self.head
            print(":::::")
            print(f"Printer {printerID} Printing the request from Machine ID: {currNode.document.getSender()} {currNode.document.getStr()}")
            print(":::::")
            # Once printed, remove the node from the queue
            self.head = self.head.next
            self.queue_size -= 1

    # Print the contents of the entire list ---for debugging ---
    # Doesn't remove any nodes from the list
    def queuePrintAll(self):
        currNode = self.head

        print("LinkedList:", end=" ")

        # Traverse through the LinkedList
        while currNode is not None:
            # Print the data at current node
            print(currNode.document.getStr(), end=" ")
            # Go to next node
            currNode = currNode.next

        print()

# allows devs to test this the output of this queue when this script is directly executed
if __name__ == "__main__":
    # create a print queue to track the documents being printed
    queue = printList()
    # make 6 documents with unique string content and ids for testing purposes
    for i in range(1, 7):
        # create a new printable document
        doc = printDoc(f"Test Machine {i}", i)
        # attempt to add this document into the queue
        queue.queueInsert(doc)
