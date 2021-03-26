class Bird:
  def intro(self):
    print("There are many type of birds")
  def flight(self):
    print("Most of the birds can fly some cannot")

class Sparrow(Bird):
   def flight(self):
      print("Sparrows can fly")

class Ostrich(Bird):
   def flight(self):
      print("Ostrich cannot fly")


if __name__=="__main__":
  obj_bird=Bird()
  obj_sparrow=Sparrow()
  obj_ostrich=Ostrich()
  obj_bird.intro()
  obj_sparrow.intro()
  obj_ostrich.intro()
  obj_ostrich.flight()
  obj_sparrow.flight()
  obj_bird.flight()
  
  