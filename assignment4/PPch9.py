#1
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
for phenotype in celegans_phenotypes:
    print(phenotype)


#2
half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
for value in half_lives:
    print(value, end='')

#3
more_whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1,3]
more_whales = []
for count in more_whales:
    more_whales.append(count + 1)
print(more_whales)

#4
alkaline_earth_metals = [[4, 9.012], [112, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]
for inner_list in alkaline_earth_metals:
    print(inner_list[0])
    print(inner_list[1])

number_and_weight = []
for inner_list in alkaline_earth_metals:
    number_and_weight.append(inner_list[0])
    number_and_weight.append(inner_list[1])

#5
def mystery_function(values):
    """(list) -> list

    Return a copy of the list, values, and the sublists it contains.
    The tope_level sublists have their elements reversed in the returned list.number_and_weight

    mystery_function([[1, 2, 3], [4, 5, 6]]) [[3, 2, 1], [6, 5, 4]]
    """
    return mystery_function

#6
text = "quit"

text = input("Please enter a chemical formula(or 'quit' to exit): ")
if text == "quit":
    print("...exiting program")
elif text == "H2O":
         print("Water")
        
elif text == "NH3":
        print("Ammonia")
    
elif text == "CH4":
        print("Methane")
    
else:
        print("Unkown Compount")

#7
country_populations = [1295, 23, 7, 3, 47, 21]
total =  0
for population in country_populations:
    total += population
print(country_populations)

#8
print('rat_1')
print('rat_2')
print('1 weighed more then 2')
print('1 weighed less than 2')

#9
for number in range(33, 50):
    print(number)


#10
for number in range(10):
    print(10 - number, end='')

#11
sum = 0
count = 0
for number in range(2, 23):
    sum += number
    count += 1
average = sum / count

#12
def remove_neg(num_list):
    """(list of number) -> NoneType
    Remove the negative numbers from the list num_list.count

    numbers = [-5, 1, -3, 2]]
    remove_neg(numbers)
    numbers
    [1, 2]
    """
    for item in num_list:
        if item < 0:
            num_list.remove(item)
    
    return(num_list)


#13
for width in range(1, 8):
    print('T' * width)

#14
for width in range(1, 8):
    print('T' * width)
#15
width = 1
while width < 8:
    print('T' * width)
    width += 1

#16
week = 1
print(week)

week = 0
print(week)
