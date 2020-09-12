from functools import wraps

def start_end_decorator(func):

  @wraps(func)
  def wrapper(*args, **kwargs):
    print('Start')
    result = func(*args, **kwargs)
    print(result)
    print('End')
    return result
  return wrapper

@start_end_decorator
def add5(x):
  return x + 5

# print_name = start_end_decorator(add5)
# result = add5(10)
# print(add5.__name__)

class CountCalls:

  def __init__(self, func):
    self.func = func
    self.nums_calls = 0

  def __call__(self, *args, **kwargs):
    self.nums_calls += 1
    print(f'This is executed {self.nums_calls} times')
    return self.func(*args, **kwargs)

@CountCalls
def say_hello():
  print('Hello')

say_hello()

def repeat(nums):
  def decorator_repeat(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(nums):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(nums=3)
def greet(name):
  print(f'Hello {name}')

greet('Vivek')
