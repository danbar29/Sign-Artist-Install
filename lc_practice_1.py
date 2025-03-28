array = [1, 1, 1, 1]


if array[0]==array[1]:
    return True
else:
    return False

#print(array[1])


x = 0

y = 0

for y in array:
    # y += 1

    if y == y-1:
        print('duplicate')