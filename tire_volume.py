#import math module 
import math

#asks the user to input values for the width, aspect ratio, and diameter of the tire
width = float(input("Enter the width of the tire in mm (ex 205): "))
ar = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

#calculates the approximate volume of the tire
firstPar = (width * ar) + (2540 * diameter)
numerator =  ( math.pi*width**2)*( ar * firstPar )
volume = numerator/(10000000000)

#rounds the volume to two decimal points
volume = round(volume, 2)

#prints the volume of the tire for the user to see
print("\n")
print (f"The approximate volume of this tire is {volume} liters.")

#adds the curent date and time, 
with open("volume.txt", "at") as volume_file:

    from datetime import datetime

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print(f"{now:%Y-%m-%d}, {current_time}, {int(width)}, {int(ar)}, {int(diameter)}, {volume}", file=volume_file)

print("\n")
buy = input ("Would you like to buy tires with these dimensions? (yes/no)")

if buy.casefold() == "yes":
    phone_number = input("Please enter your phone number (ex: 801-765-4321): ")
    with open("volume.txt", "at") as volume_file:
        print(f"Please contact CX at {phone_number}", file=volume_file)
    print("Thank you! We will reach out to you shortly.")