#1

def rSigma(num):
    if num <= 0:
        return 0
    else:
        return int(num) + rSigma(num - 1)


print(rSigma(5))
print(rSigma(2.5))
print(rSigma(-1))


#2

def rFact(num):
    if num <= 0:
        return 1
    else:
        return int(num) * rFact(int(num) - 1)


print(rFact(3))
print(rFact(6.5))


#3
def floodFill(canvas2D, startXY, newColor):
    def fill(x, y, original_color, new_color):
        if (
            0 <= x < len(canvas2D[0]) and
            0 <= y < len(canvas2D) and
            canvas2D[y][x] == original_color
        ):
            canvas2D[y][x] = new_color
            fill(x + 1, y, original_color, new_color)
            fill(x - 1, y, original_color, new_color)
            fill(x, y + 1, original_color, new_color)
            fill(x, y - 1, original_color, new_color)

    x, y = startXY
    original_color = canvas2D[y][x]
    fill(x, y, original_color, newColor)

canvas2D = [
    [1, 1, 1, 2, 2],
    [1, 1, 3, 3, 3],
    [1, 1, 3, 3, 3],
    [2, 3, 3, 3, 3],
    [2, 3, 3, 3, 3]
]
startXY = [2, 2]
newColor = 1

floodFill(canvas2D, startXY, newColor)

for row in canvas2D:
    print(row)
