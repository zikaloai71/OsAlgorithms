import threading

queue = []
max_size = 5
lock = threading.Lock()
condition = threading.Condition(lock)

class Producer(threading.Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if len(queue) == max_size:
                print("Queue is full, producer is waiting")
                condition.wait()
            else:
                item = 1 # Producing new item
                queue.append(item)
                print(f"Produced item {item}")
                condition.notify()
            condition.release()

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Queue is empty, consumer is waiting")
                condition.wait()
            else:
                item = queue.pop(0)
                print(f"Consumed item {item}")
                condition.notify()
            condition.release()

if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
