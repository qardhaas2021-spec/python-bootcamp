# TUPLES VS LISTS
# tuples are more faster and efficient then lists
# tuples are saver then lists
# tuples can be used as keys in dictionaries
# Storage efficiency
import sys
l1 = [1, 2, 3, 4, 5]
t1 = (1, 2, 3, 4, 5)
print(f'find the size of the list: {sys.getsizeof(l1)}')
print(f'find the size of the tuple: {sys.getsizeof(t1)}')


t1 = (1, 1.1, '1', (1, 3)) * 2
print(t1[-1])



