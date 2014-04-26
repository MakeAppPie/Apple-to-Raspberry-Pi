#Objects_01
class PDPythonStuff:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;
  #      self.d = 10;
    def myFunction(self,a,b):
        return a + b*b

    def montyFunction(self):
        return self.a + self.b * self.b

    def montyFunctionToo(self):
        return self.a + self.d *self.d
    
# test implementation of the class
c=PDPythonStuff(5,25)
print('my Function =',c.myFunction(5,25))
print('my Function =',c.myFunction(4,25))
print('my Function =',c.montyFunction())
c.a =4
print('my Function =',c.montyFunction())
print('my Function =',c.montyFunctionToo())
