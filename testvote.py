from collections import Counter

l=["john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"]

if __name__=="__main__":
   count=Counter(l)
   print(count)
   d=dict()
   for i in count.values():
      d[i]=[]
   for key,value in count.items():
       d[value].append(key)
   print(d)
   m=sorted(d.keys(),reverse=True)[0]
   if len(d[m])>1:
      print(sorted(d[m],reverse=False)[0])
   else:
      print(d[m][0])

      
       