# Basis for all Arcade programs; import the plugin to make it work.
import arcade

# Screen dimensions
WIDTH = 640
HEIGHT = 480

player_x = WIDTH / 2
player_y = HEIGHT / 2


# FUNCTIONS / "def" defines the function


# Updating / Refreshing function.
def on_update(delta_time):
    pass


# Drawing function.
def on_draw():
    arcade.start_render()
    # Draw in here...
    # arcade.draw_shape_etc (x-coord, y-coord, radius, colour)
    arcade.draw_circle_filled(player_x, player_y, 200, arcade.color.YELLOW)
    arcade.draw_ellipse_filled(255, 300, 20, 45, arcade.color.BLACK)
    arcade.draw_ellipse_filled(395, 300, 20, 45, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(265, 135, 120, 60, arcade.color.BLACK)


# Key input function.
def on_key_press(key, modifiers):
    pass


# Key release function.
def on_key_release(key, modifiers):
    pass


# Mouse click function
def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods; uses our OWN functions
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    arcade.run()


if __name__ == '__main__':
    setup()
