# Write your code below this line 👇
counts = []


def prime_checker(number):
    i = number
    while i > 0:
        if number % i == 0:
            counts.append(i)
            i -= 1
        else:
            i -= 1

    if 1 in counts and number in counts and not len(counts) > 2:
        print("Prime Number")
    else:
        print("Not a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
