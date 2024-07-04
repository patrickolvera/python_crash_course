mountains = [
    "Denali",  # Highest in North America[^1^][1]
    "Mount Whitney",  # Highest in contiguous US[^1^][1]
    "Mount Rainier",  # Most prominent in contiguous US[^1^][1]
    "Mauna Kea",  # Tallest from base to summit[^1^][1]
    "Mount Elbert",  # Highest in Rocky Mountains[^1^][1]
    "Grand Teton",  # Northernmost 4000-meter summit[^1^][1]
    "Mount Mitchell",  # Highest in eastern US[^1^][1]
    "Mount Washington"  # Most prominent in eastern US[^1^][1]
]

print(mountains[0])
print(mountains[-1])

mountains.insert(0, 'Mount Katahdin')
mountains.append('Mount Everest')
print(f'Mountains =\n{mountains}')

popped_item = mountains.pop(0)
print(f'Popped item = {popped_item}')

mountains.remove('Denali')
print(f'Removed an item with .remove():\n{mountains}')

del mountains[5]
print(f'Item deleted with "del mountains[5]":\n{mountains}')

print(f'sorted(list) returns a sorted list without changing its state:\
      \n{sorted(mountains)} ')

mountains.reverse()
print(f'reversed with .reverse() method:\n{mountains}')

mountains.sort()
print(f'list sorted with .sort():\n{mountains}')

mountains.sort(reverse=True)
print(f'sorted in reverse order with .sort(reverse=True):\
     \n{mountains}')

print(f'return the length of the list with len():\
      \n{len(mountains)}')