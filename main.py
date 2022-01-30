

def listMultiple(arr1,arr2):
  s = set(arr1) # 0(a)
  for e in arr2: # 0 (b)
    if e in s: # 0 (1)
      return True # 0 (1)
    
  return False # 0 (1)

  # 0 (a+b)

print(listMultiple(['a','b','f','d','s','e','l'],['b''e','w','p','a']))

print(listMultiple([],[]))