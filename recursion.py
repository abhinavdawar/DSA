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
      res.append(ans)
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


  def mazePath_HVD_another_way(sr, sc, er, ec, dir, dirS, ans, res):
    if(sr == er and sc == ec):
      res.append(ans)
      return 1

    count = 0
    for d in range(0,len(dir)):
      x = sr + dir[d][0]
      y = sc + dir[d][1]
      if(x >= 0 and y >= 0 and x <= er and y <= ec):
        count += mazePath_HVD_another_way(x, y , er, ec, dir, dirS, ans + dirS[d], res)

    return count


  def floodFill(sr, sc, dir, dirS, ans, res, visited):
    n = len(visited)
    m = len(visited[0])
    
    if(sr == n-1 and sc == m-1):
      res.append(ans)
      return 1

    count = 0
    visited[sr][sc] = True
    for d in range(0,len(dir)):
      x = sr + dir[d][0]
      y = sc + dir[d][1]
      if(x >= 0 and y >= 0 and x < n and y < m and visited[x][y] == False):
        count += floodFill(x, y , dir, dirS, ans + dirS[d], res, visited)

    visited[sr][sc] = False
    return count

  # it is giving wrong output
  def equalset(arr, set1, set2, idx):
    if(idx == len(arr)):
      if(sum(set1) == sum(set2)):
        print("set1 -> " + set1)
        print("set2 -> " + set2)
        return 1
      else:
        return 0
    count = 0
    count += equalset(arr, set1 + [arr[idx]], set2, idx+1)
    count += equalset(arr, set1, set2 + [arr[idx]], idx+1)
    return count


  def permutation(string, ans):
    if(len(string) == 0):
      print(ans)
      return 1
        
    count = 0
    for i in range(0, len(string)):
      ch = string[i]
      ros = string[0: i] + string[i+1:]
      count += permutation(ros , ans + ch)

    return count

# Coins, Permutation and Combination problems
  def permutationInfiniteCoins(arr, target, string):
    if(target == 0):
      print(string)
      return 1
      
    count = 0
    for ele in arr:
      if(target - ele >= 0):
        count += permutationInfiniteCoins(arr, target-ele, string+str(ele))
        
    return count


  def combinationInfiniteCoins(arr, target, string, idx):
    if(target == 0):
      print(string)
      return 1

    count = 0
    for i in range(idx, len(arr)):
      if(target - arr[idx] >= 0):
        count += combinationInfiniteCoins(arr, target-arr[i], string+str(arr[i]), i)

    return count


  def combinationSingleCoins(arr, target, string, idx):
    if(target == 0):
      print(string)
      return 1

    count = 0
    for i in range(idx, len(arr)):
      if(target - arr[i] >= 0):
        count += combinationSingleCoins(arr, target-arr[i], string+str(arr[i]), i+1)

    return count


  def permutationSingleCoins(arr, target, string):
    if(target == 0):
      print(string)
      return 1
      
    count = 0
    for i in range(0, len(arr)):
      if(arr[i] > 0 and target - arr[i] >= 0):
        val = arr[i]
        arr[i] = -val
        count += permutationSingleCoins(arr, target-val, string+str(val))
        arr[i] = val
        
    return count


  def combinationSingleCoins_subsequenceMethod(arr, target, string, idx):
    if(target == 0 or idx == len(arr)):
      if(target == 0):
        print(ans)
        return 1
      return 0

    count = 0
    if(target - arr[idx] >= 0):
      count += combinationSingleCoins_subsequenceMethod(arr, target-arr[idx], string+str(arr[idx]), idx+1)
    count += combinationSingleCoins_subsequenceMethod(arr, target, string, idx+1)

    return count