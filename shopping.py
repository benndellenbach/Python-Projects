print ( "\n"                                   )
print ( "Welcome to the Shopping Cart Program!")
print ( "\n"                                   )

shopping_list = []
shopping_item = -1

list_price    = []
item_price    = -1

while True:
    print        ( "Please select one of the following:" )
    print        ( "1. Add item"                         )
    print        ( "2. View cart"                        )
    print        ( "3. Remove item"                      )   
    print        ( "4. Compute total"                    )
    print        ( "5. Quit"                             )
    print        ( "\n"                                  )
    
    action = int ( input ( "Please enter an action: " )  )
    print        ( "\n"                                  )
    
    if action == 1:
        #  In the notes in this section, I was trying to add a confirmation loop that 
        #  only ended when I was done adding items. If I could get some tips on how
        #  to do this in Python, that would be awesome!

        #loop_1 = True
        #while True:
            shopping_item = input ( "What item would you like to add? "           )
            print                 ( "\n"                                          )

            item_price = input    ("What is the price of " + shopping_item + "? " )
            print                 ( "\n"                                          )
            
            shopping_list.append  (shopping_item.capitalize()                     )
            list_price.append     (float(item_price)                              )

            print                 (shopping_item + " has been added to the cart." )
            print                 ( "\n"                                          )

            #confirm = True
            #while confirm == True:
            #    again = input ("Would you like to add another item? (yes/no) ")
            #    if again is "yes":
            #        confirm == False
            #    elif again is "no":
            #        loop_1 == False
            #        confirm == False
            #    else:
            #        print("Sorry, that is not a valid response.")

    
    if action == 2:

        print ("The contents of the shopping cart are:" ) 
        print ( "\n"                                    )

        for i in range(len(shopping_list)):
            print (str(i+1), ".", shopping_list[i], "\t ", "-", "${:,.2f}".format(float(list_price[i])))

        print ( "\n"                                    )

    if action == 3:

        index = int ( input ( "Which item (number) would you like to remove?" ) )
        print       ( "\n"                                                      )

        index = index - 1

        if index >= 0 and index < len(shopping_list):
            shopping_list.pop(index)

            print ( "Item removed." )
            print ( "\n"            )

        else:
            print ( "Sorry, that is not a valid item number." )
            print ( "\n"                                      )

    if action == 4:

       total = 0
       total = total + sum(map(float,list_price))

       print ( "The total price of the items in the shopping cart is" , "${:,.2f}".format( total ) )
       print ( "\n"                                                                                )
    
    if action == 5:
        print ( "Thank you. Goodbye." )
        print ( "\n"                  )
        break