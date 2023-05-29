from enum import Enum
from queue import Queue
class TestAndSet:
    def __init__(self):
        self.lock = 0

    def tas(self):
        # Atomically set the lock to True and return the previous value
        return_value = self.lock
        self.lock = 1
        return return_value

    def release(self):
        # Release the lock by setting it to False
        self.lock = 0

class Process:
    def __init__(self, name, tas_lock):
        self.state = Process.State.Ready
        self.name = name
        self.tas_lock = tas_lock

    class State(Enum):
        Ready = 0
        Running = 1
        Waiting = 2
        Done = 3

    def Sleep(self):
        self.state = Process.State.Waiting

    def Wakeup(self):
        self.state = Process.State.Ready

    def Run(self):
        self.state = Process.State.Running

    def Done(self):
        self.state = Process.State.Done

    def __str__(self):
        return self.name

    def process_function(self):
        print("Process {} is trying to enter the critical section.".format(self.name))
        while self.tas_lock.tas():
            self.Sleep()
            # If TAS returns 1, the lock was already taken, so the process waits
            print("Process {} is waiting to enter the critical section.".format(self.name))
        self.Run()
        print("Process {} entered the critical section.".format(self.name))
        # Simulate some work being done in the critical section
        print("Process {} is working in the critical section.".format(self.name))
        # Release the lock
        self.tas_lock.release()
        self.Done()
        print("Process {} exited the critical section.".format(self.name))

# Test code
if __name__ == "__main__":
    test_lock = TestAndSet()

    p1 = Process("p1", test_lock)
    p2 = Process("p2", test_lock)

    # Start the processes
    p1.process_function()
    p2.process_function()
