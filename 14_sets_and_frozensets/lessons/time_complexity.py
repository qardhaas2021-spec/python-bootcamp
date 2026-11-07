# TIME COMPLEXITY
import time
import sys
l1 = list(range(1_000_000))
start = time.time()

# print(start)

bv = 456789 in l1
end = time.time()
print(f"time taken to check if 456789 is in l1: {end - start:.6f}")

print('#' * 50)

l2 = set(range(1_000_000))
start = time.time()
bv = 456789 in l2
end = time.time()
print(f"time taken to check if 456789 is in l2: {end - start:6f}")

print(f"list of memory used by l1: {sys.getsizeof(l1)}")
print('#' * 50)
print(f"set of memory used by l2: {sys.getsizeof(l2)}")

