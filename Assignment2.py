# # Convert Time (hh, min, sec) into Seconds
# hours = int(input("Enter hours: "))
# minutes = int(input("Enter minutes: "))
# seconds = int(input("Enter seconds: "))

# total_seconds = (hours * 3600) + (minutes * 60) + seconds

# print("Total Seconds =", total_seconds)


# Convert Celsius to Fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# print("Temperature in Fahrenheit =", fahrenheit)

# Convert Distance from Feet and Inches into Meters and Centimeters
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = (feet * 12) + inches
cm = total_inches * 2.54
meter = cm / 100

print("Distance in Meters =", meter)
print("Distance in Centimeters =", cm)