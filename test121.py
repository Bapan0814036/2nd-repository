def checkempty(str1,str2):
   if len(str1)==0:
      return False
   else:
      while(len(str1)!=0):
         index=str1.find(str2)
         if index==-1:
            return False
         else:
           str1=str1[:index]+str1[index+len(str2):]
      return True

if __name__=="__main__":
   str1="GEEGEEKSKS"
   str2="GEEKS"
   print(checkempty("GEEGEEKSKS","GEEKS"))