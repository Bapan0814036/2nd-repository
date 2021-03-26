def replacechar(input,c1,c2):
   test=map(lambda x:x if(x!=c1 and x!=c2) else c1 if(x==c2) else c2,input)
   return ''.join(test)

if __name__=="__main__":
   print(replacechar("teststr",'t','s'))
