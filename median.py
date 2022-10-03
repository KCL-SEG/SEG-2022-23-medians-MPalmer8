"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def medianfunc(numbers = []):
    index = len(numbers)/2
    num = int(index)
    if len(numbers)%2:
        median = numbers[num]
        return median
    else:
        median = (numbers[num] + numbers[num - 1])/2
        return median


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(medianfunc(numbers))
