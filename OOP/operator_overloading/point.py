class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def __str__(self):
        return '({x}, {y})'.format(x = self.x, y = self.y)
    
    # + 연산자 오버로딩
    def __add__(self, n):#1
        self.x += n
        self.y += n
        return self
    
    '''
    def __radd__(self, n):
        self.x += n
        self.y += n
        return self
    '''
    
if __name__=="__main__":
    p1 = Point(2, 2)
    p2 = p1 + 3

    
    #p2 = 3 + p1
    print(p2)
