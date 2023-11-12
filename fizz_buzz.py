random_number = int(input("Please enter a random number"))


def fizz_buzz(random_number):
    for num in range(0, random_number):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizz_buzz(random_number)
