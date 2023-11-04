def factorial(n):
    aux = 1
    for i in range(n):
        aux *= i+1
    print(aux)
factorial(2)