def calculate_fuel(distance):
    if distance >= 10:
        return 100 + distance * 10
    else:
        return 100


print(calculate_fuel(10))
print(calculate_fuel(15))
print(calculate_fuel(23.5))
print(calculate_fuel(1))
