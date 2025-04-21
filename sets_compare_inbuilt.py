set1 = {"Java", "Python", "C++"}
set2 = {"Java", "Python", "C++"}
set3 = {"Java", "Python", "C++", "JavaScript"}

print(f"Is Both sets are equal? {set1 == set2}")
print(f"Is Both sets are equal? {set1 == set3}")

print(f"Is set1 subset of set3? {set1.issubset(set3)}")


set2 = {1, 2, 3}
set1 = {1, 2}
print(f"Is Proper subset? {set2 > set1}")  # True, set2 is a proper superset of set1


set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {1, 2}

# Perform the following operations:
# 1. Find the union of set_a and set_b
# 2. Find the intersection of set_b and set_c
# 3. Find the symmetric difference between set_a and set_b either in set a or set b but not both.
# 4. Check if set_c is a subset of set_a
# 5. Check if set_b is a disjoint with set_a - if no common elements return True or False

print(f"set_a: {set_a}")
print(f"set_b: {set_b}")
print(f"set_c: {set_c}")

union_ab = set_a.union(set_b)
intersection_bc = set_b.intersection(set_c)
symmetric_difference_ab = set_a.symmetric_difference(set_b)
is_subset = set_c.issubset(set_a)
is_superset = set_a.issuperset(set_c)
is_disjoint = set_a.isdisjoint(set_b)
is_proper_subset = set_c < set_a

#print the results
print(f"Union of set_a and set_b: {union_ab}")
print(f"Intersection of set_b and set_c: {intersection_bc}")
print(f"Symmetric difference between set_a and set_b: {symmetric_difference_ab}")
print(f"Is set_c a subset of set_a? {is_subset}")
print(f"Is set_a a superset of set_c? {is_superset}")
print(f"Is set_a disjoint with set_b? {is_disjoint}")
print(f"Is set_c a proper subset of set_a? {is_proper_subset}")
