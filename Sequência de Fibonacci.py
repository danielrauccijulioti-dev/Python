n = int(input("quantos termos gostaria de ver? "))

n1,  n2 = 0, 1

for int in range(n):
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2
