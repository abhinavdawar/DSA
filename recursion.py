
class Recursion:
  
  def printIncreasing(a, b):
    if (a > b):
      return
    print(a)
    Recursion.printIncreasing(a+1, b)

  
  def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * Recursion.factorial(x-1))

  
  def printDecreasing(a, b):
    if(a > b):
      return
    Recursion.printDecreasing(a+1, b)
    print(a)

  
  def printIncreasingDecreasing(a, b):
    if (a > b):
      return
    print(a)
    Recursion.printIncreasingDecreasing(a+1, b)
    print(a)

  
  def power(a, b):
    if (b == 0):
      return 1
    return a * Recursion.power(a, b-1)


  def maximumInArray(arr, idx):
    pass 


  def minimumInArray(arr, idx):
    pass 


  def find(arr, idx, data)
  
  
  def firstIndex(arr, idx, data):
    pass 


  def lastIndex(arr, idx, data):
    pass