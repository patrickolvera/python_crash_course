places = ['China', 'Himalayas', 'Yosemite', 'Grand Canyon', 'Denali']
print(f'This is the original list:\n{places}')
print(f'\nThis list is sorted without changing its state:\n{sorted(places)}')
print(f'\nThis is the original list again:\n{places}')
places.reverse()
print(f'\nReverse sorted and state changed:\n{places}')
places.reverse()
print(f'\nI reversed it again!:\n{places}')
places.sort()
print(f'\nSorted with sort() method:\n{places}')
places.sort(reverse=True)
print(f'\nSorted in reverse order with .sort(reverse=True):\n{places}')