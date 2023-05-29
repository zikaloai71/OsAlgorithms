from enum import Enum
from queue import Queue

class Process:
    def __init__(self , name):
        self.state = Process.State.Ready
        self.name = name

    class State(Enum):
        Ready = 0
        Running = 1
        Waiting = 2
        done = 3

    def Sleep(self):
        self.state = Process.State.Waiting

    def Wakeup(self):
        self.state = Process.State.Ready
    def Run(self):
        self.state = Process.State.Running
    def Done(self):
        self.state = Process.State.done
    

    def __str__(self):
        return self.name

class Semaphore:
    class Value(Enum):
        Zero = 0
        One = 1

    def __init__(self):
        self.q = Queue()
        self.value = Semaphore.Value.One

    def P(self,  p):
            if self.value == Semaphore.Value.One:
                self.value = Semaphore.Value.Zero
                # print("Process {} is in critical section".format(p))
                p.Run()
            else:
                # add the process to the waiting queue
                # print("Process {} is in waiting state".format(p))
                self.q.put(p)
                p.Sleep()

    def V(self, process):
            process.Done()
            if self.q.qsize() == 0:
                s.value = Semaphore.Value.One
            else:
                # select a process from waiting queue
                p = self.q.queue[0]
                # remove the process from waiting as it has
                # been sent for CS
                self.q.get()
                p.Run()
# test code
if __name__ == "__main__":

        s = Semaphore()

        p1 = Process("p1")
        p2 = Process("p2")

        s = Semaphore()

        s.P(p1)
        print( " the state of p1 is {}".format(p1.state))
        s.P(p2)
        print( " the state of p2 is {}".format(p2.state))

        s.V(p1)
        print( " the state of p1 is {}".format(p1.state))
        print( " the state of p2 is {}".format(p2.state))

        s.V(p2)
        print( " the state of p2 is {}".format(p2.state))


