weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
new_weight = weight * 0.45359237;
new_height = height * 0.0254;
body_mass_index =  new_height / (new_height * new_height);
print(f"Your BMI = {body_mass_index}");

