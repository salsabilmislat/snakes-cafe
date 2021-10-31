print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type ""quit"" **")
print("**************************************")

print("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")

print("***********************************")
print("** What would you like to order? **")
print("***********************************")

menu_dictionarie={   
"Wings":0,
"Cookies":0,
"Spring Rolls":0,
"Salmon":0,
"Steak":0,
"Meat Tornado":0,
"A Literal Garden":0,
"Ice Cream":0,
"Cake":0,
"Pie":0,
"Coffee":0,
"Tea":0,
"Unicorn Tears":0,

}


item=input("> ").title()
print("\n")
while item !="Quit":
    if(item in menu_dictionarie):
        menu_dictionarie[item]=menu_dictionarie[item]+1
      # print (menu_dictionarie[item])
        print (f"** {menu_dictionarie[item]} order of {item} have been added to your meal **")
        print("\n")
        item=input("> ").title()
       # for newitem in menu_dictionarie:
           # if (menu_dictionarie[newitem]>0):
              
    #elif:
     #    print("the item you ordered is not on the menu")
    elif(item =="Quit"):
        break


      