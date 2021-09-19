# Tasks Python Core
Your task is to write programming code according to the requirements:
- your working directory is *src*;
- use files that are identified in the same way as tasks (functions); 
- write your solution within the appropriate functions;
- you may use different IDE, just copy paste your code to the files in repo;
- press 'commit changes' and check the tests

## Task 0. Say "Hello!"
Create a function **hello()** that returns the string "Hello!".

## Task 1. Return the Sum of Two Numbers
Create a function **addition(param1, param2)** that takes two numbers as arguments and return their sum.  

*Examples*
```plaintext
addition(3, 2) ➞ 5
addition(-3, -6) ➞ -9
addition(7, 3) ➞ 10
```
    
## Task 2. FizzBuzz Interview Question
Create a function **fizz_buzz(number)** that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz":
- If the number is a multiple of 3 the output should be "Fizz".
- If the number given is a multiple of 5, the output should be "Buzz".
- If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
- If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
- The output should always be a string even if it is not a multiple of 3 or 5.  

*Examples*
```plaintext
fizz_buzz(3) ➞ "Fizz"
fizz_buzz(5) ➞ "Buzz"
fizz_buzz(15) ➞ "FizzBuzz"
fizz_buzz(4) ➞ "4"
```
    
## Task 3. Area of a Triangle
Write a function **tri_area(base, height)** that takes the base and height of a triangle and return its area.  
*Notes.*
- The area of a triangle is: *(base * height) / 2*

*Examples*
```plaintext
tri_area(3, 2) ➞ 3
tri_area(7, 4) ➞ 14
tri_area(10, 10) ➞ 50
```
    
## Task 4. Let's Fuel Up!
A vehicle needs 10 times the amount of fuel than the distance it travels. However, it must always carry a minimum of 100 fuel before setting off.
Create a function **calculate_fuel(distance)** which calculates the amount of fuel it needs, given the distance.  
*Notes.*  
- Distance will be a number greater than zero.
- Return 100 if the calculated fuel turns out to be less than 100.

*Examples*
```plaintext
calculate_fuel(15) ➞ 150
calculate_fuel(23.5) ➞ 235
calculate_fuel(3) ➞ 100
```

## Task 5. Both Zero, Negative or Positive
Write a function **both(number1, number2)** that returns *True* if both numbers are:
- Smaller than 0, OR ...
- Greater than 0, OR ...
- Exactly 0  
Otherwise, return False.  
*Notes.*  
Inputs will always be two numbers.

*Examples*
```plaintext
both(6, 2) ➞ True
both(0, 0) ➞ True
both(-1, 2) ➞ False
both(0, 2) ➞ False
```

## Task 6. Integer in Range?
Create a function **int_within_bounds(number, lower_bound, upper_bound)** that validates whether a *number* is within the bounds of *lower* and *upper*. Return *False* if *number* is not an integer.  

*Notes.*  
The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) to an upper bound.
Bounds will be always given as integers.

*Examples*
```plaintext
int_within_bounds(3, 1, 9) ➞ True
int_within_bounds(6, 1, 6) ➞ False
int_within_bounds(4.5, 3, 8) ➞ False
```

## Task 7. Two Makes Ten
Create a function **makes10(a, b)** that takes two arguments. Both arguments are integers, *a* and *b*. Return *True* if one of them is *10* or if their sum is *10*.

*Examples*
```plaintext
makes10(9, 10) ➞ True
makes10(9, 9) ➞ False
makes10(1, 9) ➞ True
```

## Task 8. Summing the Squares
Create a function **squares_sum(n)** that takes a number *n* and returns the sum of all square numbers up to and including *n*.
```plaintext
squares_sum(3) ➞ 14
# 1² + 2² + 3² =
# 1 + 4 + 9 =
# 14
```
*Notes.*  
Remember that *n* is included in the total.

*Examples*
```plaintext
squares_sum(3) ➞ 14
squares_sum(12) ➞ 650
squares_sum(13) ➞ 819
```

## Task 9. Give Me the Even Numbers
Create a function **sum_even_nums_in_range(start, stop)** that takes two parameters *(start, stop)*, and returns the sum of all even numbers in the range.
```plaintext
sum_even_nums_in_range(10, 20) ➞ 90
# 10, 12, 14, 16, 18, 20
```
*Notes.*  
Remember that the *start* and *stop* values are inclusive.

*Examples*
```plaintext
sum_even_nums_in_range(51, 150) ➞ 5050
sum_even_nums_in_range(63, 97) ➞ 1360
```

## Task 10. Find the Mean of All Digits
Create a function **mean(number)** that returns the mean of all digits of the given *number*.

*Notes.*  
The mean of all digits is the *sum of digits / how many digits* there are (e.g. mean of digits in 512 is *(5+1+2)/3(number of digits) = 8/3=2*).  
The mean will always be an integer.

*Examples*
```plaintext
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
```


