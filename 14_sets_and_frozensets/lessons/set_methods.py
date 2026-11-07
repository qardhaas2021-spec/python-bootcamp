from typing import Any


s1 = {1, 2, 3, 4, 5, 'a', 'b', 'c', 4, 6}
print(s1)
# print(s1[0]) ERROR

#  SETS ARE MUTABLE 
s1.add((2026, 2027))
print(s1)

s1.remove(1)
print(s1)

# s2 = ['j,', 'k'] ERROR

print(s1)

# STR >= SET

s4 = set('helooooo')
print(s4)

# SET >= TUPLE

s5 = set((1, 3, 5, 6, 'abc'))
print(s5)

# LIST >= SET

s7 = [10, 20, 30, 40]
print(set(s7))

macs = ['172.20.10.2', '172.20.10.2', '172.20.10.2', '172.20.10.4', '172.20.10.3']
mac_addreses = set(macs)
print(mac_addreses)

class_a = ['Ali', 'Sara', 'john', 'Mia', 'Ali' ]
class_b = ['john', 'Mia', 'Leo', 'Sara', 'Leo']
set_a = set(class_a)
set_b = set(class_b)

# students are both classes
print(set_a & set_b)  

# Students only in class a
print(set_a - set_b)

# All students combined no dublicate
print(set_a | set_b)


visitors = ['user1', 'user2', 'user3', 'user2', 'user4', 'user1']

# count unique visitors
unique_visitors = set(visitors)
print(len(unique_visitors))

# check if user5 visites

print('user5' in unique_visitors)

# remove user3
unique_visitors.discard('user3')
print(unique_visitors)


sentence = 'the quick brown fox jumps over the lazy dog'
unique_letters = (set(sentence))
unique_letters.discard(' ')
print(unique_letters)
alphabet = set('abcdefghijklmnopqrstuvwxyz')
print(alphabet <= unique_letters)


#  Network security

allawed_ips = ['192.168.1.1', '192.168.1.2', '10.0.0.1', '10.0.0.2']
connected_ips = ['192.168.1.1', '192.168.1.5', '10.0.0.1', '10.0.0.3']
intruders = (set(connected_ips) - set(allawed_ips))
print(intruders)

print(set(allawed_ips) - (set(connected_ips)))
print(len(set(connected_ips)))

for i in allawed_ips:
    if i not in connected_ips:
        print(i)


set1 = {1, 2, 3, 4,}
set2 = {2, 3, 1, 4}
print(set1 == set2)
print(set1 is set2)
print([1, 2, 3, 4,] == [1, 2, 3, 4])
















