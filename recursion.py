
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

  
  # Fetch all the index in array at which particular data is present
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
      
    recAns = subSequence(idx+1, str)
    myAns = recAns.copy()
    for s in recAns:
      myAns.append(str[idx] + s)
    return myAns

  # Here, ans is type string and res is type array which will store all ans
  def subSequence_other_way(str, idx, ans, res):
    if(idx == len(str)):
      res.add(ans)
      return 1

    count = 0
    count += subSequence_other_way(str, idx+1, ans+str[idx], res)
    count += subSequence_other_way(str, idx+1, ans, res)
    return count


  def mazePath_HVD(sr, sc, er, ec):
    if(er == sr and ec == sc):
      return [""]

    myAns = []
    if(sr+1 <= er):
      vertical = mazePath_HVD(sr+1, sc, er, ec)
      for s in vertical:
        myAns.append("V" + s)

    if(sc+1 <= ec):
      horizontal = mazePath_HVD(sr, sc+1, er, ec)
      for s in horizontal:
        myAns.append("H" + s)

    if(sr+1 <= er and sc+1 <= ec):
      diagonal = mazePath_HVD(sr+1, sc, er, ec)
      for s in diagonal:
        myAns.append("D" + s)

    return myAns


  def mazePath_HVD_other_way(sr, sc, er, ec, ans, res):
    if(sr == er and sc == ec):
      res.append(ans)
      return 1

    count = 0
    if(sr+1 <= er):
      count += mazePath_HVD_other_way(sr+1, sc, er, ec, ans+"V", res)

    if(sc+1 <= ec):
      count += mazePath_HVD_other_way(sr, sc+1, er, ec, ans+"H", res)

    if(sr+1 <= er and sc+1 <= ec):
      count += mazePath_HVD_other_way(sr+1, sc, er, ec, ans+"D", res)
    return count