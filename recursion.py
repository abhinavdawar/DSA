
class Recursion:
  
  def printIncreasing(a, b):
    if (a > b):
      return
    print(a)
    printIncreasing(a+1, b)

  
  def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

  
  def printDecreasing(a, b):
    if(a > b):
      return
    printDecreasing(a+1, b)
    print(a)

  
  def printIncreasingDecreasing(a, b):
    if (a > b):
      return
    print(a)
    printIncreasingDecreasing(a+1, b)
    print(a)

  
  def power(a, b):
    if (b == 0):
      return 1
    return a * power(a, b-1)


  def maximumInArray(arr, idx):
    if (idx == len(arr)):
      return -1e9
    maxSF = maximumInArray(arr, idx+1)
    return max(maxSF, arr[idx])
    

  def minimumInArray(arr, idx):
    if (idx == len(arr)):
      return 1e9
    minSF = minimumInArray(arr, idx+1, ans)
    return min(minSF, arr[idx])


  def find(arr, idx, data):
    if (idx == len(arr)):
      return -1e9
    if(arr[idx] == data):
      return idx
    return find(arr, idx+1, data)
    
  
  def firstIndex(arr, idx, data):
    if(idx == len(arr)):
      return -1
    ans = firstIndex(arr, idx+1, data)
    if(arr[idx] == data):
      return idx
    return ans


  def lastIndex(arr, idx, data):
    if(idx == len(arr)):
      return -1
    smallRes = lastIndex(arr, idx+1, data)
    if(smallRes != -1):
      return smallRes
    if(arr[idx] == data):
      return idx
    return -1

  
  # Fetch all the index in array at which particular data is       present
  def allIndex(arr, idx, data):
    if(idx == len(arr)):
      return []
    myAns = allIndex(arr, idx+1, data)
    if(arr[idx] == data):
      myAns.append(idx)
    return myAns

  
  def subSequence(idx, str):
    if(idx == len(str)):
      return [""]
    recAns = Recursion.subSequence(idx+1, str)
    myAns = recAns.copy()
    for s in recAns:
      myAns.append(str[idx] + s)
    return myAns