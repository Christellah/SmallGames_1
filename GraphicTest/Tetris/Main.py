import arcade

SCREEN_W = 800
SCREEN_H = 600

arcade.open_window(SCREEN_W, SCREEN_H, "First shot !")
arcade.set_background_color((51, 153, 255))
arcade.start_render()

# Board 10*12
arcade.draw_rectangle_outline(300, 300, 402, 482, arcade.color.CERULEAN_BLUE, 2)
# Square
# arcade.draw_rectangle_filled(120, 45, 40, 40, arcade.color.BABY_BLUE)

for row in range(12):
    for column in range(10):
        arcade.draw_rectangle_filled(120+(column*40), 80+(row*40), 40, 40, arcade.color.BABY_BLUE)
        arcade.draw_rectangle_outline(120+(column*40), 80+(row*40), 40, 40, arcade.color.CORNFLOWER_BLUE, 1)

arcade.finish_render()
arcade.run()

