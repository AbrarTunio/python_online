#defining a function

def message():
 return ("Welcome to CodePro")

# calling a function 
# m1 =  message()

# print( len(m1)  )
# print( m1 )


# defining an arithmetic function

def sqr(   num   ):
 return num*num

# a = sqr( 2 )
# print( a )


def expo( num , e = 2  ):
 return num**e

a = expo( 2 )

b = sqr ( a )




def summation( **num  ):
 value = 0
 for k , v in num.items():
  value = value + v
 # result = sum( num )
 return value


print( summation( num1= 1 , num2 = 2 , num3= 3 , num4= 4 ) )


