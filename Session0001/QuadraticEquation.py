a = float(input())  # explicitive type casting =! implicitive type casting
c = float(input())
b = float(input())

delta = ((b ** 2)) - (4 * a * c)

x1 = ((-1 * b) + (delta ** (0.5)))/(2 * a)
x2 = ((-1 * b) - (delta ** (0.5)))/(2 * a)

print(f'x1 = {x1},x2 = {x2}')
