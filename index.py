def fizzbuzz(number):
    array = []
    for i in range(number + 1):
        if i % 3 == 0 and i % 5 == 0:
            array.append("FizzBuzz")
        elif i % 5 == 0:
            array.append("Buzz")
        elif i % 3 == 0:
            array.append("Fizz")
        else:
            array.append(i)
    return(array)


print(fizzbuzz(15))