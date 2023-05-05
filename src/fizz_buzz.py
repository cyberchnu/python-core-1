def fizz_buzz(param):
  #Type your code here
  if param % 3 == 0 and param % 5 == 0:
        return "FizzBuzz"
    elif param % 3 == 0:
        return "Fizz"
    elif param % 5 == 0:
        return "Buzz"
    else:
        return str(param)
