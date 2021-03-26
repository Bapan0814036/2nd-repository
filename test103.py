from collections import Counter
l=['a','b','c','d','a','b','b','a','c','s','d','d']

if __name__=="__main__":
   count=Counter(l)
   print(count)
   d=dict()
   for i in count.values():
      d[i]=[]
   for key,value in count.items():
      d[value].append(key)
   m=sorted(d.keys(),reverse=True)[0]
   if len(d[m])>1:
      print(sorted(d[m],reverse=False)[0])
   else:
      print(d[m][0])
   print(d)


