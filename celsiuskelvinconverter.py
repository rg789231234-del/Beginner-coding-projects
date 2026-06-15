finalvalue=0

convertchoice=input("Would you like to convert to A: Celsius to Kelvin or B: Kelvin to Celsius? ").upper()
initialvalue=float(input("Enter your temperature value here for your chosen conversion:"))

if convertchoice=="A":
    finalvalue=initialvalue+273.15
    print("Your converted temperature is", finalvalue, "K")

elif convertchoice=="B":
    finalvalue=initialvalue-273.15
    print("Your converted temperature is", finalvalue, "degrees Celsius")

else:
    print("Error, an invalid choice was input. Please select either A or B")

        