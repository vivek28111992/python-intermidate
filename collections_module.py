# collections: Counter, NameTuple, OrderedDict, DefaultDict, Deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaaaaabbbbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))


Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)


ordered_dict = {}
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)


d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])


dq = deque()
dq.append(1)
dq.append(2)

dq.appendleft(3)
print(dq)

dq.popleft()
print(dq)

dq.rotate(1)
print(dq)
