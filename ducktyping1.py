class India:
   def capital(self):
     print("Delhi is the capital of India")
   def language(self):
     print("Hindi is the language")
   def type(self):
     print("India is a developing country")

class USA:
   def capital(self):
      print("Washington is the capital of USA")
   def language(self):
      print("English is the language of USA")
   def type(self):
      print("USA is developed country")


def fun(obj):
   obj.capital()
   obj.language()
   obj.type()


if __name__=="__main__":
  obj_india=India()
  obj_usa=USA()
  fun(obj_india)
  fun(obj_usa)

   