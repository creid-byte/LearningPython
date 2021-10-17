# Flag variables
numbers = [5, 3, 6, 70, 4, 2,4 ,3]

i = 0
square = 500
success = False

while i < len(numbers):
    if numbers[i]**2 > square:
        print(numbers[i], 'squared is larger than,', square)
        success = True
        break
    print(numbers[i], 'squared is not larger than,', square)
    i +=1

if success:
    print("One was large enough")
