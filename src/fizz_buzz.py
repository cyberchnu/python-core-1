def fizz_buzz(number):
    # % means that the remainder must be equal to zero when that number is divided
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


print(fizz_buzz(3))  # Output: "Fizz"
print(fizz_buzz(5))  # Output: "Buzz"
print(fizz_buzz(15))  # Output: "FizzBuzz"
print(fizz_buzz(7))  # Output: "7"
