from Test import Triangle

class ColoredTriangle(Triangle):
    def __init__(self,a,b,colour):
        super().__init__(a,b)
        self.colour = colour
        
    def describe(self):
        msg = super().describe()
        return msg + f". I am {self.colour}"

    
         
        