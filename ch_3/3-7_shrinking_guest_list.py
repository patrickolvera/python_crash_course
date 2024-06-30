guests = ['Einstein', 'Elon Musk', 'Joe Rogan']
print(f'Welcome {guests[0]}!')
print(f'Welcome {guests[1]}!')
print(f'Welcome {guests[-1]}!')

print('We have found a bigger table!')
guests.insert(0, 'Cleopatra')
guests.insert(2, 'Henry Ford')
guests.append('Juluis Cesar')

print(f'Welcome {guests[0]}!')
print(f'Welcome {guests[1]}!')
print(f'Welcome {guests[2]}!')
print(f'Welcome {guests[3]}!')
print(f'Welcome {guests[4]}!')
print(f'Welcome {guests[5]}!')

print('We can only invite 2 people to dinner.')
popped = guests.pop()
print(f'Sorry {popped}, I can\'t invite you.')
popped = guests.pop()
print(f'Sorry {popped}, I can\'t invite you.')
popped = guests.pop()
print(f'Sorry {popped}, I can\'t invite you.')
popped = guests.pop()
print(f'Sorry {popped}, I can\'t invite you.')

print(f'{guests[0]}, you are still invited!')
print(f'{guests[1]}, you are still invited!')
del guests[0]
del guests[0]
print(guests)