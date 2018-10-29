import arcade

SCREEN_W = 600
SCREEN_H = 600

def drawCircle(x, y, radius, color, filled):
    if filled:
        arcade.draw_circle_filled(x, y, radius, color)
    else:
        arcade.draw_circle_outline(x, y, radius, color)

arcade.open_window(SCREEN_W, SCREEN_H, "First shot !")
arcade.set_background_color(arcade.color.VIVID_SKY_BLUE)
arcade.start_render()

# Face
drawCircle(300, 300, 200, arcade.color.YELLOW_ORANGE, True)
drawCircle(300, 300, 201, arcade.color.BLACK, False)
# Eyes
drawCircle(370, 350, 20, arcade.color.BLACK, True)
drawCircle(230, 350, 20, arcade.color.BLACK, True)
# Smile
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(300, 280, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

arcade.finish_render()
arcade.run()

