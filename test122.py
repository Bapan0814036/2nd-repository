def rotate(str1,d,reverse):
    if reverse:
       str2=str1[:d]
       str1=str1[d:]+str2
    else:
       str2=str1[len(str1)-d:]
       str1=str2+str1[:len(str1)-d]
    return str1

if __name__=="__main__":
   print(rotate("GeeksforGeeks",2,True))

   