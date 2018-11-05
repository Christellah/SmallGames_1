import arcade
import Piece

SCREEN_W = 800
SCREEN_H = 600

arcade.open_window(SCREEN_W, SCREEN_H, "First shot !")
arcade.set_background_color((51, 153, 255))
arcade.start_render()

# Board 10*20
arcade.draw_rectangle_outline(300, 300, 252, 502, arcade.color.CERULEAN_BLUE, 2)

# 1 Shape
# TODO : position = possition possible on board
newPiece = Piece.Shape( (300, 300) )
newPiece.drawShape()


arcade.finish_render()
arcade.run()

