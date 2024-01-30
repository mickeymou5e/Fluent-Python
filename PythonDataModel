import math

class Vector:
  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return f'Vector({self.x!r},{self.y!r})' # the repr method shows the way to output a readable pythonistic way to see the object you created
                                           # What the !r does is gets the standard representation of the attribute to diplay
  def __bool__(self):
    return bool(self.x or self.y)

  def __abs__(self):
    return math.hypot(self.x,self.y)
