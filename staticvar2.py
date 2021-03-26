class SampleClass:
   count=0
   def __init__(self):
     self.a=2
     self.b=3
   def increase(self):
       SampleClass.count+=1
s2=SampleClass()
s2.increase()
print(s2.count)

if __name__=="__main__":
    s3=SampleClass()
    s3.increase()
    print(s2.count)
    print(SampleClass.count)
    print(dir(s3))
    print(vars(s3))

