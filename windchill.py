print ("\n")

T = float(input("What is the temperature? "))

degree = input("Fahrenheit or Celsius (F/C)? ")

print ("\n")

if degree.capitalize() == "C":
    print (f"{T} degrees Celcius is equal to:")
    T = (T * 1.8) + 32
    print (f"{T} degrees Farenheight")

form_temp = float("{0:.2f}".format(T))

print ("\n")

V = 5
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 10
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 15
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 20
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 25
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 30
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 35
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 40
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 45
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 50
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 55
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

V = 60
calc_temp = 35.74 + ( 0.6215 * T ) - 35.75 * ( V ** 0.16 ) + (0.4275 * T) * (V**0.16)
final_temp = float("{0:.2f}".format(calc_temp))
print (f"At temperature {form_temp}F, and wind speed {V} mph, the windchill is: {final_temp}F"  )

print ("\n")