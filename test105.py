str1="geeks quiz practise code"
output="code practise quiz geeks"

if __name__=="__main__":
  str2=str1.split(' ')
  print(str2[-1::-1])
  print(' '.join(str2[-1::-1]))