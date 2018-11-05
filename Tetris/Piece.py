import arcade
import Constants

class Shape:
    color: arcade.color.ATOMIC_TANGERINE
    position: () #{'x':0, 'y':0}
    shapeType: ""
    squaresArr: [ ]

    # TODO : change shapyType magic string to Constants
    def __init__(self, position, color=arcade.color.ATOMIC_TANGERINE, shapeType="I"): 
        self.position = position
        self.color = color
        self.shapeType = shapeType

    # TODO : Give self.shapeType instead of 'I'
    def getShapeArray(self):
        return Constants.SHAPES['I'][Constants.ROTATION['1']]
   
    def drawShape(self):
        squaresArr = self.getShapeArray()
        # arcade.start_render()
        for row in range(4):
            for col in range(4):
                if squaresArr[row][col] == '1':
                    # TODO : change position and color
                    arcade.draw_rectangle_filled(300+(col*25), 300+(row*25), 25, 25, arcade.color.BABY_BLUE)
                    arcade.draw_rectangle_outline(300+(col*25), 300+(row*25), 25, 25, arcade.color.CORNFLOWER_BLUE, 1)
        # arcade.finish_render()
        # arcade.run()

    
    def fall(self):
        pass

    def checkCollidings(self):
        pass

    def rotateRight(self):
        pass

    def rotateLeft(self):
        pass