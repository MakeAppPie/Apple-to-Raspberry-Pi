#PSPythonStuff.py
class PSPythonStuff:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def montyPythonFunction(self,a,b):
        return a+b*b
         
class PSMorePythonStuff(PSPythonStuff):
    def __init__(self,a,b):
        PSPythonStuff.__init__(self,a,b)
    def montyPythonFunction(self):
        return self.a+self.b*self.b
    
class PSStillMorePythonStuff(PSPythonStuff):
    def __init__(self,a,b,c):
        PSPythonStuff.__init__(self,a,b)
        self.c=c
    def montyPythonFunction(self):
        return self.a+self.b*self.c
