import array as arr

numbers = arr.array('i', [10, 11, 12, 12, 13])

numbers.remove(12)

print(numbers)  #output: array('i', [10, 11, 12, 13])

print(numbers.pop(2)) # output: 12  -> index of 12 is 2

print(numbers)  # output: array('i', [10, 11, 13])