# Write a function called my_buzz that takes a number. 
# If the number is divisible by 3, it should return “Fizz”. 
# If it is divisible by 5, it should return “Buzz”. If it is divisible by both 3 and 5, it should return “FizzBuzz”.Otherwise, same no
def my_buzz(x):
    x=int(x)
    if x%3 == 0:
        if x%5 == 0:
            print("FizzBizz")
        else:
            print("Fizz")
    if x%5 == 0 and x%3 != 0:
        print("Buzz")

my_buzz(input("input"))