#A function definition specifies the name of a new function and the sequence of
#statements that execute when the function is called
def computepay(h,r) :
      if h <= 40 :
         pay = h * r
      else :
         pay = 40 * r + (h-40) * 1.5 * r
         return(pay)
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hours)
r = float(rate)
p = computepay(h,r)
print(p)
