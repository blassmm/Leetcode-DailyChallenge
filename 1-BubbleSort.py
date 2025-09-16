array = [64, 34, 25, 12, 22, 11, 90]

while True:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    if array == sorted(array):
        break

print(array)