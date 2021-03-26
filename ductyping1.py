class India():
   def capital(self):
     print("New Delhi is capital of india")
   def language(self):
     print("Hindi is primary language")
   def type(self):
     print("India is a developing country")

class USA():
   def capital(self):
     print("Washington is capital of india")
   def language(self):
     print("English is primary language")
   def type(self):
     print("USA is a developed country")

if __name__=="__main__":
    obj_ind=India()
    obj_usa=USA()
    for country in (obj_ind,obj_usa):
        country.capital()
        country.language()
        country.type()



