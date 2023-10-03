class Point():

    def __init__(self,n,x,y):
        self._n= n
        self._x= x
        self._y= y


    def updateCoord(self,x,y):
        self._x= x
        self._y= y

    
    def getType(self):
        return 'Point_'
        
        
    def getNumber(self):
        return self._n
    

    def printCoord(self):
        print(f'\nO ponto {self._n} possui as coord: ({self._x}, {self._y}).')        




class Circle(Point):
    
    """ O círculo herda do ponto suas funcionalidades e adiciona raio"""
    """ É necessário definir as funções membro para o círculo operar"""
    
    def __init__(self,n,x,y,radius):
        
        super().__init__(n, x, y)
        self.radius= radius
        
    
    def getType(self):
        """ Atencção!!! Polimorfismo aplicado"""
        return 'Circle_'
        
    
    def updateCoord(self,x,y,radius):
        super().updateCoord(x, y)
        self.radius= radius

    
    def printCoord(self):
        
        print(f'\nO círculo {self._n} possui origem em: ({self._x}, {self._y})')
        print(f'E o seu raio é {self.radius}')
        
    
    def pointIn(self,pt):
        """Detecta aonde um ponto está relacionado ao círculo"""
        if (pow((self._x - pt._x),2) + pow((self._y - pt._y), 2) < pow(self.radius,2)):
            print(f'\nO ponto pt{pt._n} está dentro do círculo')
        elif (pow((self._x - pt._x),2) + pow((self._y - pt._y), 2) > pow(self.radius,2)):
            print(f'\nO ponto pt{pt._n} está fora do círculo')
        else:
            print(f'\nO ponto pt{pt._n} pertence ao círculo')
    
    def area(self):
        print(f'\nA área do círculo é {self.radius*self.radius*3}')
    
    
    def perimeter(self):
        print(f'\nO perímetro do círculo é {self.radius*2*3}')


class Line():
    def __init__(self,x1,x2,y1,y2,n1,n2,n):
        self.x1 = Point._x
        self.pt2 = Point()

class triangle():
    def __init__(self,pt1,pt2,pt3):
        pass
    pass