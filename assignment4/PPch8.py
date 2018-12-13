kingdoms = ['Backteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdoms[0])
print(kingdoms[5])
print(kingdoms[:3])
print(kingdoms[2:4])
print(kingdoms[4:])
print(kingdoms[1:0])

print(kingdoms[-6])
print(kingdoms[-1])
print(kingdoms[-6:-3])
print(kingdoms[-4:-1])
print(kingdoms[-2:])
print(kingdoms[-1:-2])


appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
appointments.append('16:30')
print(appointments)

ids = [4353, 2314, 2956, 3382, 9362, 3900]
ids.remove(3382)
print(ids)
ids.index(9362)
ids.insert(ids.index(9362) +1, 4499)
ids = ids + [5566, 1830]
print(ids)


akaline_earth_metals = [4, 12, 20, 38, 56, 88]
akaline_earth_metals[5], akaline_earth_metals[-1]
len(akaline_earth_metals)
max(akaline_earth_metals)
print(akaline_earth_metals)

temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
temps.sort()
cool_temps = temps[0:2]
warm_temps=temps[2:]
temps_in_celsius=cool_temps + warm_temps
print(temps)

def same_first_last(L):
    """(list) -> bool
    Precondition: len(L) >= 2

    Return True if and only if first item of list is the same as the last

    same_first_last([3, 4, 2, 8, 3])
    True
    same_first_last(['apple', 'banana', 'pear'])
    False
    same_first_last([4.0, 4.5])
    False
    """
    return L[0] == L[-1]

def is_longer(L1, L2):
    """(list, list) -> bool
    
    Return True if and only if the length of L1 is longer than the length of L2

    is_longer([1, 2, 3], [4, 5])
    True
    is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    False
    is_longer(['a', 'b', 'c'], [1, 2, 3])
    False
    """
    return len(L1) > len(L2)


units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units[0])
print(units[-1] or units[1])
print(units[0][0])
print(units[1][0])
print(units[0][1])
print(units[1][0:2])
