mountains = ["Mount Everest", "Mount Fuji", "Mount Bromo", "Mount Kilimanjaro"]

print("Original list:")
print(mountains)

print("\nAccessing an element:")
print(mountains[0])

print("\nChanging an element:")
mountains[1] = "Mount Merapi"
print(mountains)

print("\nAdding an element with append():")
mountains.append("Mount Rinjani")
print(mountains)

print("\nAdding an element with insert():")
mountains.insert(1, "Mount Semeru")
print(mountains)

print("\nRemoving an element with del:")
del mountains[1]
print(mountains)

print("\nRemoving an element with pop():")
mountains.pop()
print(mountains)

print("\nRemoving an element by value:")
mountains.remove("Mount Bromo")
print(mountains)

print("\nSorted list:")
print(sorted(mountains))

print("\nReversed list:")
mountains.reverse()
print(mountains)

print("\nSorting the list:")
mountains.sort()
print(mountains)

print("\nNumber of elements:")
print(len(mountains))