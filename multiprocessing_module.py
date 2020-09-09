import multiprocessing
from multiprocessing import Pool

def spawn(nums):
  print(f'Spawned {nums}')

def job(nums):
  return nums * 2

if __name__ == '__main__':
    # for i in range(55):
    #   p = multiprocessing.Process(target=spawn, args=(i,))
    #   p.start()
    # p.join()

  p = Pool(processes=20)
  data = p.map(job, range(20))
  p.close()
  print(data)
