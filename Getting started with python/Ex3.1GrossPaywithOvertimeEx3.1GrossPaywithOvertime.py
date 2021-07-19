#Input - Getting data from user
hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hour)
r = float(rate)
#Applying Conditional statements to Check for certain conditions and then execute or skip a
#sequence of statements
if h <= 40 :
   pay = h * r
else :
   pay = 40 * r + (h-40) * r * 1.5
print(pay)
