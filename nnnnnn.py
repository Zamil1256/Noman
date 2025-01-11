#BMI calculator
weight=float(input("Enter your weight in Kg="))
height=float(input("Enter your height in m ="))

if height>0:
    BMI=weight/(height*height)
    print(f"Your BMI is:{BMI:.2f}")
    if BMI<18.5:
        print("category=Underweight")
    elif BMI<18.5 and BMI>=24.9:
        print("category=Healthy weight")
    elif BMI<25.0 and BMI>=29.0:
        print("category=Overweight")
    elif BMI>=30.0:
         print("category=Obesity")
else:
    print("Error! Height must be zero.")         
                    
