
places = ["Japan", "Switzerland", "Paris", "South Korea", "London"]

print("Original list:")
print(places)

print("\nAlphabetical order:")
print(sorted(places))

print("\nOriginal list:")
print(places)

print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

print("\nOriginal list:")
print(places)

print("\nReversed list:")
places.reverse()
print(places)

print("\nBack to original order:")
places.reverse()
print(places)

print("\nSorted alphabetically:")
places.sort()
print(places)

print("\nSorted in reverse alphabetical order:")
places.sort(reverse=True)
print(places)