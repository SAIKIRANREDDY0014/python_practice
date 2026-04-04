class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self,outer):
      self.name = "Inner Class"
      self.outer = outer

    def display(self):
      print(f"This is the {self.name}")
      print(f"This is the {self.outer.name}")
      

outer = Outer()
print(outer.name)
inner = outer.Inner(outer)
inner.display()
