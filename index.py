# def fizzbuzz(number):
#     array = []
#     for i in range(number + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             array.append("FizzBuzz")
#         elif i % 5 == 0:
#             array.append("Buzz")
#         elif i % 3 == 0:
#             array.append("Fizz")
#         else:
#             array.append(i)
#     return(array)


# print(fizzbuzz(15))


def fibonacci(number):
    n0, n1 = 0, 1
    count = 0

    if number <= 0:
        print("No negatives")
    elif number == 1:
        print(n0)
    else:
        while count < number:
            print(n0)
            nth = n0 + n1
            n0 = n1
            n1 = nth
            count += 1

fibonacci(7)