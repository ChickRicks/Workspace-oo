from my_libraries.shapes2d import Point, Circle
from my_libraries.coordsystems import CartesianBoard



def workspace():
    
   
    pt1= Point(1,12,54)
    pt1.printCoord()
    
    
    circ2= Circle(2, 13, 15, 4)
    circ2.printCoord()
    
    pt3 = Point(3,17,22)
    pt4 = Point(4,17,27)
   
    dashboard= CartesianBoard()
    dashboard.inserShape(pt1)
    dashboard.inserShape(circ2)
    
    dashboard.showShapes()
    
    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()
    
    print('\nRemoção de uma das formas!')
    
    dashboard.removeShape(pt1)
    dashboard.showShapes() 
    
    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()
    
    circ2.area()
    circ2.perimeter()
    
    print('\nVamos pegar uma das formas e atualizar:')
    
    my_copy_of_circ2= dashboard.getShape('Circle_2')
    my_copy_of_circ2.updateCoord(17,22,5)
    my_copy_of_circ2.printCoord()
    
    print('\nO objeto original:')
    circ2.printCoord()
    
    print('\nNote que a atualização da cópia alterou o objeto original!')
    
    circ2.area()
    circ2.perimeter()
    circ2.pointIn(pt1)
    circ2.pointIn(pt3)
    circ2.pointIn(pt4)
    
    print("\nSuccessful exit")



if __name__ == "__main__":

    workspace()
