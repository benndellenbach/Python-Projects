# Asks the user for all necessary values for the purchase
print ("\n")
chd     = float( input( "What is the price of a child's meal? " ) )
adl     = float( input( "What is the price of an adults meal? " ) )
chd_qty = float( input( "How many children are there? "         ) )
adl_qty = float( input( "How many adults are there? "           ) )
str     = float( input( "What is the sales tax rate? "          ) )
print ("\n")

# Calculates the subtotal
adl_sub = ( adl * adl_qty )
chd_sub = ( chd * chd_qty )
sub     =   chd_sub + adl_sub 
tax     = ( sub * str ) / 100
ttl     =   sub + tax 

# Formats values to the necessary decimals and stores values as floating 
# points
float_adl      = "{:.0f}".format( adl_qty )
float_chd      = "{:.0f}".format( chd_qty )
float_adl_sub  = "{:.2f}".format( adl_sub )
float_chd_sub  = "{:.2f}".format( chd_sub )
float_sub      = "{:.2f}".format( sub     )
float_tax      = "{:.2f}".format( tax     )
float_ttl      = "{:.2f}".format( ttl     )

# Displays the subtotals, computed sales tax, and the 
# total price of the purchase.

print (  "----------------------------------------------------"             )
print ( f"Number of adult meals purchased: ".ljust(46) + f"{float_adl}"     )
print ( f"Number of child meals purchased: ".ljust(46) + f"{float_chd}"     )
print ( f"Cost of all adults' meals: ".ljust(45)       + f"${float_adl_sub}")
print ( f"Cost of all childrens' meals: ".ljust(45)    + f"${float_chd_sub}")
print ( f"Subtotal:".ljust(45)                         + f"${float_sub}"    )
print ( f"Sales Tax:".ljust(45)                        + f"${float_tax}"    )
print ( f"Total:".ljust(45)                            + f"${float_ttl}"    )
print (  "----------------------------------------------------"             )
print (  "\n"  )

# Asks user for payment amount
pmt = float( input( "What is the payment amount? "          ) )
print ( "\n" )

# Calculates the change, them formats it to two decimals and stores 
# it as a floating point
chg        = ( pmt - ttl )
format_chg = "{:.2f}".format( chg )


# Displays the amount of change owed to the customer
print (  "----------------------------------------------------" )
print ( f"Change:".ljust(45)             + f"${format_chg:25}"  )
print (  "----------------------------------------------------" )
print ( "\n" )