print("Welcome to the Treasure island.Your mission is to find the treasure")
Direction = input('You\'re at a crossroad,Do you want to go left or right?\n').lower() #single ' to add everything in a string and \ for escaping '
if Direction == "right" :
    print("You fell off a cliff! GAME OVER")
else :
   go =  input("You reached a river, do you want to swim across or wait for the boar? swim/wait\n").lower()
   if go == "swim":
     print("You got eaten by a crocodile! GAME OVER")
   else :
     door = input("You have 3 doors infront of you : blue,red and yellow, which one do you pick?\n").lower()
     if door == "blue":
        print("You got killed by a bear, GAME OVER")
     elif door == "red":
        print("You opened the door to medussa!statue!GAME OVER")
     else :
        print("You opened the door to the treasure cave!!!!YOU WIN")
