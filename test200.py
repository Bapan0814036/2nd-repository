from collections import Counter

l=['a','b','c','a','d','e','e','g','b','g','d','a','c','a','a','g']
if __name__=="__main__":
   count=Counter(l)
   d=dict()
   print(count)
   for i in count.values():
     d[i]=[]
   for keys,values in count.items():
      d[values].append(keys)
   m=sorted(d.keys(),reverse=True)[0]
   print(m)
   print(d)
   if len(d[m])>1:
      print(sorted(d[m],reverse=False)[0]+'  '+"is the winner")
   else:
      print(d[m][0])
