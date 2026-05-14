#Write a program to:
#Take the temperature in Celsius as input (string format).
#Convert it into a float.
#Calculate the equivalent temperature in Fahrenheit using the formula: Fahrenheit=(Celsius×9/5​)+32
#Print the result in both Celsius and Fahrenheit.


temperature = int(input("enter temp in celcius : "))
print(float(temperature))

celsius = 45
in_fahrenheit = (celsius*9/5)+32

print("in celsius->",celsius,"\nin fahrenheit->",in_fahrenheit)