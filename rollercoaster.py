print("Welcome to the rollercoaster ride")
height = int(input("How tall are you?in cm\n"))
bill = 0
if height < 120:
   print("Sorry you need to grow taller to ride!")
else :                                            #Dont forget the colon after the if else statements
   print("Congratulations you can ride")
   age = int(input("How old are you?\n"))
   if age <12:
      bill = 5
      print("Kids tickets are 5 Euros")
   elif age<=18:
      bill = 7
      print("Youth tickets are 7 Euros")
   elif age >= 45 and age<=55:
      print("Everything is going to be okay, have a free ride on us!")
   else :
      bill = 12
      print("Adult tickts are 12 Euros")
photos = input("Do you want a photo?Y/N\n")
if photos == "Y":                           #for a character you need to add == and put the char in quotes
   bill += 3
else :
   bill = bill
print (f"your total bill is : {bill} Euro")
      