#to find the largest and smallest numbers from user input
largest = None
smallest = None
while True :
     num = input("Enter number: ")
     if num == 'done': break
#error handling using try/except
     try:
        n = int(num)
        if smallest is None :
           smallest = n
        elif n < smallest :
           smallest = n
        if largest is None :
           largest = n
        elif n > largest :
           largest = n
     except :
           print('Invalid input')
print("Maximun is", largest)
print("Minimum is", smallest)
