#на вход N и выдает число от - N до N

N = int(input('Введите число '))
print(*range(-N, N+1))