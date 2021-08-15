x_1 = 1001000

if x_1 == 0:
    x_0 = 1
else:
    while x_1 % 10 == 0:
        x_1 = x_1 // 10

    if x_1 == 1:
        x_0 = 1
    else:
        x_0 = 0

print(x_0)