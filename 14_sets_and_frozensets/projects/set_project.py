math = {'Ahmed', 'Ali', 'Mohamed', 'Omar'}
science = {'Ali', 'Mohamed', 'Khalid', 'Amiin'}
english = {'Ahmed', 'Ali', 'Mohamed', 'Omar'}
m1 = math.intersection(science)
m2 = math.difference(science)
print(f'In math and science: {m1}')
print(f'Only in math: {m2}')

all_students = math | science | english
print(f'All students: {all_students}')

print(f" Ahmed in english: {'Ahmed' in english}")
print(f'Totol unique students: {len(all_students)}')


borrowed_by_ahmed = {'Python Book', 'Math Book', 'History Book', 'Science Book'}

borrowed_by_ali = {'Math Book', 'English Book', 'Science Book', 'Geography Book'}

available_book = {'Python Book', 'English Book', 'Art Book', 'Music Bookmn'}

both = borrowed_by_ahmed.intersection(borrowed_by_ali)
only_ahmed = borrowed_by_ahmed.difference(borrowed_by_ali)
only_ali = borrowed_by_ali.difference(borrowed_by_ahmed)

print(f'books borrowed by both Ahmed and Ali: {both}')
print(f'books have only ahmed but not ali: {only_ahmed}')
print(f'books does only ali have but not ahmed: {only_ali}')
all_borrowed = borrowed_by_ahmed.union(borrowed_by_ali)
still_available = available_book.difference(all_borrowed)
art_available = "Art Book" in available_book

print(f'books are borrowed by anyone: {all_borrowed}')
print(f'books are available: {still_available}')
print(f'art book are available: {art_available}')

s1 = {'a,', 'b', 'c'}
s2 = {'c', 'd', 'e'}
s3 = s1.intersection(s2)
print(s3)
s4 = s2.difference(s1)
print(s4)

s5 = s1.union(s2)
print(s5)

s6 = s1.symmetric_difference(s2)
print(s6)

s7 = s1.issubset(s2)
print(s7)

s8 = s1 | s2
print(s8)


