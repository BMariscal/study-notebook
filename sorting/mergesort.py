def merge(lst):
  lstlen = len(lst)
  if lstlen == 0 or lstlen == 1:
    return lst[:lstlen]
  midway = lstlen // 2
  lst1 = lst[0:midway] 
  lst2 = lst[midway:lstlen]

  newlst1 = merge(lst1)
  newlst2 = merge(lst2)
  newlst =  sort(newlst1, newlst2)
  return newlst

def sort(lst1, lst2):
  newlst = []
  lst1indx = 0
  lst2indx = 0

  while lst1indx < len(lst1) and lst2indx < len(lst2):
    if lst1[lst1indx] <= lst2[lst2indx]:
      newlst.append(lst1[lst1indx])
      lst1indx+=1
    else:
      newlst.append(lst2[lst2indx])
      lst2indx+=1
  
  newlst.extend(lst1[lst1indx:])
  newlst.extend(lst2[lst2indx:])
  return newlst

    
