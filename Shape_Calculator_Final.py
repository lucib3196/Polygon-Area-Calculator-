class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def __str__(self):
        return f'Rectangle(width={self.w}, height={self.h})'

    def set_width(self, width):
        self.w = width
        
    def set_height(self , height ):
        self.h = height
    
    def get_area(self):
        rec_area = (self.w * self.h)
        return rec_area
    
    def get_perimeter(self):
        return ((2 * self.w) + (2 * self.h))

    def get_diagonal(self):
        return(( (self.h ** 2) + (self.w ** 2) ) **(.5))

    def get_picture(self):
        if self.h > 50 or self.w > 50:
            return "Too big for picture."
        else:
            row = self.w * '*'
            picture = ''
            for column in range(self.h):
                picture += row + '\n'
            return(picture)

    def get_amount_inside(self,shape):
        amount_inside = int(self.get_area()/ shape.get_area())
        return(amount_inside)
class Square(Rectangle):
    def __init__(self, side):
        self.w = side
        self.h = side

    def set_side(self,side):
        self.w = side
        self.h = side

    def __str__(self):
        return f'Square(side={self.w})'

print(Rectangle(5,5).get_diagonal())
