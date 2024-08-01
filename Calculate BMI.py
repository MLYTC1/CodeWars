def bmi(weight, height):
    bmi_1 = weight/height**2
    if bmi_1 <= 18.5:
        return "Underweight"
    if bmi_1 <= 25.0:
        return "Normal"
    if bmi_1 <= 30.0:
        return "Overweight"
    if bmi_1 > 30:
        return "Obese"
