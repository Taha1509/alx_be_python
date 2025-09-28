
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = float(input("Enter the temperature to convert:"))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

if temperature_type == "c":
    converted = convert_to_fahrenheit(temperature)
    print (f"{temperature}c is {converted}f")

elif temperature_type == "f":
    converted = convert_to_celsius(temperature)
    print (f"{temperature}f is {converted}c")

else: 
    print ("Invalid temperature. Please enter a numeric value.")



    