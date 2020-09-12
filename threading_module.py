from threading import Thread, Lock, current_thread
from queue import Queue
import time

database_value = 0

def increase(lock):
  global database_value

  with lock:
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy

def worker(q, lock):
  while True:
    value = q.get()
    # processing...
    with lock:
      print(f'{current_thread().name} got {value}')
    q.task_done()

if __name__ == '__main__':
    lock = Lock()
    print('start value ', database_value)

    q = Queue()

    num_threads = 10

    for i in range(num_threads):
      thread = Thread(target=worker, args=(q, lock))
      thread.daemon=True
      thread.start()

    for i in range(1, 21):
      q.put(i)

    q.join()

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value ', database_value)
    print('end main')
