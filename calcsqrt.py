#! /usr/bin/env python3

# Shirin Nagle
#Calculate the square root of a number

def sqrt(x):
  """
  Calculate the square root of argument x.
  """
  # Check that x is positive
  if x < 0:
    print("Error: Negative value supplied")
    return -1
  else:
    print ("The number is positive")

  #Initial guess for the sqaure root
  z = x / 2.0
  counter = 1 
  #Continuously improve the guess
  
  while abs(x - (z*z)) > .0000001:  
    z -= (z*z - x) / (2*z)
    counter += 1
    print(z)
   # print(counter)
  # return counter
  return z
  
print(sqrt(63.0))

