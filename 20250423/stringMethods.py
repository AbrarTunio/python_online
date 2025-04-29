# names = [ "fayaz" ]

# names.append( "nosheen" )

# names.pop()

# names.append( "abdul" )


# print( len( names )  , "->" ,  names)

# color = [ "green" , "kaana" , "blue" , "orange"]
# color.insert( 2 , "red" )
# color.remove("kaana")

# print(color)

# colors = [ "green" , "kaana" , "blue" , "orange"]

# for color in colors:
# 	if color == "banana":
# 		colors.remove(color)
# 		print(color, "is removed")
# 	else:
# 		print(f"{color} is not fruit")  


colors = [ "green" , "kaana" , "blue" , "orange"]
removed_colors = []


for color in colors:
	if "e" in color:
		removed_colors.append(color)
		print(color, "is removed")
	elif "a" in color:
		removed_colors.append(color)	
		print(color,"is removed")
	else:
		print(f"{color} is not fruit")  



print(colors)
print(removed_colors)