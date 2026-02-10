# Fibonacci Sequence
#Name: Chinmay PC
#USN: 1RUA25BCA0021


def fibonacci(n1, n2):
    print(n1)
    print(n2)

    for i in range(3, 11):
        temp = n1 + n2
        print(temp)
        n1 = n2
        n2 = temp

fibonacci(0, 1)
