# vehicles = ['motorcycle', 'car', 'plane', 'boat']
# print(f'I would like to own a Ninja 660 {vehicles[0]}!')
# print(f'I normally drive a {vehicles[1]}.')
# print(f'Sometimes I fly on a {vehicles[2]}.')
# print(f'My friend used to have a {vehicles[3]}.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.insert(0,'hyabusa')
motorcycles.append('ducati')
del motorcycles[1]
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
first_owned = motorcycles.pop(1)
print(f"The first motorcyle I owned was a {first_owned.title()}")
motorcycles.remove('suzuki')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')
