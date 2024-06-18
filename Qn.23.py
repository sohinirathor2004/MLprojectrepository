conversion_type = input("Enter the conversion type (C to F or F to C): ").strip().upper()

temperature = float(input("Enter the temperature value: "))

if conversion_type == "C TO F":
    converted_temperature = (temperature * 9/5) + 32
    print(temperature,"°C is equal to", converted_temperature,"°F")
elif conversion_type == "F TO C":
    converted_temperature = (temperature - 32) * 5/9
    print(temperature,"°F is equal to",converted_temperature,"°C")
else:
    print("Invalid conversion type. Please enter 'C to F' or 'F to C'.")
