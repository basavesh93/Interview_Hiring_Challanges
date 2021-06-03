# Generate diamond pattern
def drawDiamond(n):
    for i in range(n):
        print('  ' * (n - i - 1) + '/\\  ' * (i + 1))
        print('  ' * (n - i - 1) + '\\/  ' * (i + 1))
    for j in range(n):
        if (j + 1) * (j + 1) != n * n:
            print('  ' * (j + 1) + '/\\  ' * (n - j - 1))
            print('  ' * (j + 1) + '\\/  ' * (n - j - 1))


data = [5, 2, 5, 3, 1, 4]
for i in range(len(data)):
    if i != 0:
        drawDiamond(data[i])