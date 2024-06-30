guests = ['Einstein', 'Elon Musk', 'Joe Rogan']
print(f'Welcome {guests[0]}!')
print(f'Welcome {guests[1]}!')
print(f'Welcome {guests[-1]}!')

print(f'Unfortunately {guests[0]} can\'t make it.')
tardy = 'Einstein'
guests.remove(tardy)
guests.insert(0, 'Newton')

print(f'Welcome {guests[0]}!')
print(f'Welcome {guests[1]}!')
print(f'Welcome {guests[-1]}!')