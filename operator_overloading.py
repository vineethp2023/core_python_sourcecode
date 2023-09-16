class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return (x,y)
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

p1 = point(2,3)
p2 = point(5,8)
print(p1+p2)