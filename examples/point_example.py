class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        return (self._x, self._y) == (other._x, other._y)

    def __hash__(self):
        return hash((self._x, self._y))
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    # @x.setter
    # def x(self, value):
    #     self._x = value
    
    
p = Point(2,3)
print( hash(p) )
# p.x = 7
# p.y = 9
p.z = 12
print( hash(p) )
p2 = Point(2,3)
print(p2 == p)
print(p.z)

d = {}
d[p] = "Location1"
print( d[p2] )

