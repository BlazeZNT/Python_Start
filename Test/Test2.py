from test import Triangle

class colored_Triangle(Triangle):
    def __init__(self,a,b,colour):
        super().__init__(a,b)
        self.colour = colour
         
        