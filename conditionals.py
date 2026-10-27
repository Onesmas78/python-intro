temp = input("Temperature in Celsius: ")
temp = float(temp)

if temp < 0:  #boolean expression
    print("It's below freezing!")
elif temp < 10:
    print("It's quite cold.")
elif temp < 20:
    print("It's a bit chilly.")
elif temp < 30:   #True or False
    print("It's warm.")
else:
    print("It's hot!")



# Comparison: ==  !=  <  >  <=  >=
# Logic: and, or, not

# hott<-30-20-10-0->cold