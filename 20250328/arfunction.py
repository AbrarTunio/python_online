# def square(  num  ):
#  num = int( num )
#  return f"The Square of provided number is {num*num}"

# number = input( "Enter your fav number: " )
# result = square( number ) 

# print( result )


# def power( num , expo=2 ):
#  return f"The exponented value of {num} is: { num**expo }"

# result = power( 5 , 3 )
# print( result )

# def sum_all(*numbers):
#     return sum(numbers)

# print( sum_all( 1 , 2,  3 )  )


# square = lambda x: x * x
# print( square(5) )

numbers = [1, 2, 3, 4, 5]

squared = list(   map(  lambda x: x ** 2, numbers  )  )

print(squared)  # Output: [1, 4, 9, 16, 25]
