print("Welcome to BMI calculator please input your data.")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_as_float = float(height)
weight_as_int = int(weight)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)