def calculate_fuel(distance):
    if distance >= 10:
       return distance * 10
    else:
       return 100
result = (calculate_fuel(5))
print(result)
