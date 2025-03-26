# 1 Defining a function

# def greet( gender,  name  ):
#  return f"Welcome {gender}. {name}"


# # 2 Calling and using a function
# greetStudent1 = greet( "Mr", "Fayaz" )
# greetStudent2 = greet( "Mr", "Abrar" )
# greetStudent3 = greet( "Ms", "Nosheen" )
# print( greetStudent1 )
# print( greetStudent2 )
# print( greetStudent3 )


def calc( ops , a , b ) :
 a = int(a)
 b = int(b)
 if ( ops == "+" ):
  return a + b
 elif ( ops == "-" ):
  return a - b
 elif ( ops == "*" ):
  return a * b
 elif ( ops == "/" ):
  return a / b

num1 = input( "Enter your first number" )
num2 = input( "Enter your second number" )
ops = input( "Enter arithmetic operation" )

result = calc( ops , num1 , num2 )
print(result)

