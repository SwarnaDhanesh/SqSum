class Point:
   x=1
   y=3
   z=5
   def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z     
   def SqSum(self):
       return self.x**2+self.y**2+self.z**2
pass
SSum=Point(1,3,5)
print(SSum.SqSum())
