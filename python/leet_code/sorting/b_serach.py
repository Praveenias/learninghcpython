a=[1,2,3,4,5,6,7,8,9]

def bsearch(seq,v,l,r):
    if r-l == 0:
      return False
    mid = (l+r)//2
    if seq[mid] == v:
      return True
    if v < seq[mid]:
      return bsearch(seq,v,l,mid)
    else:
      return bsearch(seq,v,mid+1,r)

print(bsearch(a,10,0,len(a)))
    
    
        
