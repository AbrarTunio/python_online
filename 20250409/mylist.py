fruits = [ "Apple" , "Mango" , "Watermelon" , "Banana" ]

x = [ "Abrar" , 15 , 18.02 , True , [ "Tomato" , "Kiwi" ]  ]

# fruits = list( "Apple" , "Mango" , "Watermelon"  )

# fruits = list()

# print( "Abrar likes to eat" , fruits[0] )

# print( fruits[ :3 ] ) 

print( fruits )
print( "Before mutation" )

fruits[1] = "Kiwi"

print( fruits )
print( "After mutation" )

# fruits.append( "Mango" )
fruits.insert( 3 , "Mango" )
print( fruits )
print("After Insertion")

print("------------")
print(  fruits.pop() ) 

fruits.sort()
print(fruits)


