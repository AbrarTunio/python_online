# At initial user is asked if he is fasting or not
# if he is fasting, then display the message that restaurant is closed
# if he is not fasting then display the message please enter
# within the if (Nested if) user is asked to order from the menu
# and user is shown list of items in the menu
# on choosing the name or number the on the menu that item would be
# served and bill displayed.

condition = input("Are you fasting or not?")

if condition == "fasting":
 print("Visit us after Iftar!")
else:
 print("Please Enter")
 print("---------------")
 print("Please order from the menu below")
 print("1. Biryani\n 2. Zinger\n 3. Pakore & Samasey\n 4. Kerhai ")
 order = input("Choose your number:")
 if order == "1":
  print("Your order of biryani will be served in 20 min")
 elif order == "2":
  print("Your order of Zinder will be served in 20 min") 
 elif order == "3":
  print("Your order of Pakroe and Samosey will be served in 20 min")
 elif order == "4":
  print("Your order of Kerhai will be served in 20 min")   

