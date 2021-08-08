from collections import OrderedDict, defaultdict, deque
import heapq
import statistics as stat

"""
1.1. Unpacking a Sequence into Separate Variables
Problem
You have an N-element tuple or sequence that you would like to unpack into a collection
of N variables.
"""


def unpackseq():
    """
    Unpacking sequence
    mismatch of elelments will give ValueError
    use throw away values var usually "_"
    """
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    #name, shares, price, date = data
    name, shares, price, (year, mon, day) = data
    #print(name, shares, price, date)
    print(name, shares, price, year, mon, day)

    s = 'Hello'
    a, b, c, d, e = s
    print(a, b, c, d, e)

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data


"""
1.2. Unpacking Elements from Iterables of Arbitrary Length
Problem
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception.
"""

#grades = [3, 3, 4, 6, 5]


def drop_first_last(grades):
    """
    Unpacking using *
    """
    first, *middle, last = grades
    return stat.mean(middle)

# print(drop_first_last(grades))


def put_first():
    sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
    *trailing, current = sales_record
    trailing_avg = sum(trailing) / len(trailing)
    return trailing_avg, (trailing_avg + current) / 2

# print(put_first())


records = [
    ('foo', 1, 2),
    ('bar', 'hello', 'mister'),
    ('foo', 3, 4),
    ('foo', 1, 2, 3)
]


def do_foo(x, y, *z):
    print('foo =>', x, y, *z)


def do_bar(*s):
    print('bar =>', *s)


""" for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args) """

items = [1, 10, 7, 4, 5, 9]
head, *tail = items

#print(head, tail)


def sum(items):
    head, *tail = items
    print(head, tail)
    return head + sum(tail) if tail else head

# print(sum(items))


"""
1.3. Keeping the Last N Items
Problem
You want to keep a limited history of the last few items seen during iteration or during
some other kind of processing.
"""


def search(lines, pattern, history=5):
    """
    Keeping the history of the last N items of
    """
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('../log.txt') as f:
        """ for line, prevlines in search(f, 'python', 2):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20) """
        pass

# using deque function , O(1) - deque, O(N) - lists
q = deque(maxlen=4)
q.append(1)
""" print(q.append(2), q)
print(q.append(3), q)
print(q.append(4), q)
print(q.append(5), q)
print(q.appendleft(10), q)
print(q.append(11), q)
print(q.pop(), q)
print(q.popleft(), q) """

"""
1.4. Finding the Largest or Smallest N Items
Problem
You want to make a list of the largest or smallest N items in a collection.
"""
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
# print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

"""
1.5. Implementing a Priority Queue
Problem
You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.
"""


class PriorityQueue:
    """
    Implementing a priorityQueue using heappush() and heappop() O(logN)
    """

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # queue consists of tuple
        # priority negated to make highest priority the lowest in the list
        # index needed to retain insert order of the items of the same priority
        heapq.heappush(self._queue, (-priority, self._index, item))
        print(self._queue, self._index)
        self._index += 1

    def pop(self):
        # returns the last items in the list
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


""" q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), -4)
q.push(Item('spam'), 3)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
q.push(Item('another'), 2) """

"""
1.6 Mapping Keys to Multiple Values in a Dictionary
The choice of whether or not to use lists or sets depends on intended use. Use a list if
you want to preserve the insertion order of the items. Use a set if you want to eliminate
duplicates (and don’t care about the order).
"""
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
d['c'].add(2)
d['c'].add('w')
# print(d)

d = {}  # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
# print(d)

"""
1.7. Keeping Dictionaries in Order
Problem
You want to create a dictionary, and you also want to control the order of items when
iterating or serializing.
"""
d = dict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

"""
1.8. Calculating with Dictionaries
Problem
You want to perform various calculations (e.g., minimum value, maximum value, sort‐
ing, etc.) on a dictionary of data.
"""
prices = {
    'ACME': (45.23, 11),
    'AAPL': (612.78, 3),
    'IBM': (205.55, 10),
    'HPQ': (37.20, 20),
    'FB': (10.75, 10)
}

#print(min(zip(prices.values(), prices.keys())))
#print(sorted(zip(prices.values(), prices.keys())))
#print(sorted(zip(prices.keys(), prices.values())))

# just on dict will find min on key, not value
# print(min(prices.values()))
# get the key of the min value
min_key = (min(prices, key=lambda k: prices[k]))
min_value = prices[min_key]

#print(f'{min_key} has the lowest value {min_value[0]}')

"""
1.9. Finding Commonalities in Two Dictionaries
Problem
You have two dictionaries and want to find out what they might have in common (same
keys, same values, etc.).
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
# print(a.keys() & b.keys()) # { 'x', 'y' }
# Find keys in a that are not in b
# print(a.keys() - b.keys()) # { 'z' }
# Find (key,value) pairs in common
# print(a.items() & b.items()) # { ('y', 2) }

# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
# print(c)

"""
1.10. Removing Duplicates from a Sequence while Maintaining Order
Problem
You want to eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
# with open(somefile,'r') as f:
# for line in dedupe(f):


a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))

b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
#print(list(dedupe2(b, key=lambda d: (d['x'], d['y']))))
#print(list(dedupe2(b, key=lambda d: d['x'])))

"""
1.11. Naming a Slice Problem
Your program has become an unreadable mess of hardcoded slice indices and you want
to clean it up.
"""
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 24)
PRICE = slice(31, 35)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

sl = slice(6, 30, 3)
print(sl.start, sl.stop, sl.step)

s = 'we are here and there'
print(sl.indices(len(s)))

for i in range(*sl.indices(len(s))):
    print(s[i], i)

"""
1.12. Determining the Most Frequently Occurring Items in a Sequence
"""
