
message = "This is abrar hussain and this is something or some dummy text and so and so on"

words = message.split()

fruits = { 
 "apple" : 15,
 'oranges' : 16,
 'bananas' : 12,
 'watermelon' : 1
 }

# print(fruits['apple'])
fruits['lemon'] = 19

print( words )

listOfWords = {}

for word in words:
 if word not in listOfWords:
  listOfWords[word] = 1
 else:
  listOfWords[word] += 1  

print(listOfWords)

# for k , v in message.items():
#  print( k, v )