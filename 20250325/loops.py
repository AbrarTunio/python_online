fruits = [ "Apple" , "Kiwi" , "Melon" , "Stra" , "Lemon"  ]

# for f in fruits:
#  print( "I love:" , f  )
# print(  len( fruits ) )

numberOfFruits = len( fruits )

# while numberOfFruits > 0:
#  print(f"I love {fruits[numberOfFruits-1]}")
#  numberOfFruits -= 1

count = 0
while count < numberOfFruits:
 print(f"I love , {fruits[count]}")
 count += 1

import random as r
# print( r.randint(1,5) )

computerGuess = r.randint(1,5)
while True:
 guess = input("Guess number provided by Computer")
 if int(guess) > computerGuess:
  print("Your Guess it higher, guess again between 1 - 5")
  continue 
 elif int(guess) < computerGuess:
  print("Your Guess it low, guess again between 1 - 5")
  continue 
 else:
  print("Guessed Right")
  break
 