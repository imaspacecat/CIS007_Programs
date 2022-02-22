POUND_TO_KILOGRAM = 0.45359237
INCH_TO_METER = 0.0254
weight, height = eval(input("Enter your weight in pounds and height in inches separated by commas: "))
bmi = (weight * POUND_TO_KILOGRAM) / ((height * INCH_TO_METER) ** 2)
print("BMI is", bmi)
