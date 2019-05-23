import arcade

# Set constants for screen height and width
WIDTH = 740
HEIGHT = 785

# Define text and underline heights, then delta (change) rates.
text_height = 1000
delta_y_text = 3
underline_height = 990
delta_y_underline = 3


def on_update(delta_time):
    global text_height, delta_y_text, underline_height, delta_y_underline

    # Animate title and underline; move down until in view. 3 pixels down per on_update recall
    text_height -= delta_y_text
    underline_height -= delta_y_underline

    # Stop when desired height reached
    if text_height < 720:
        delta_y_text = 0
    if underline_height < 710:
        delta_y_underline = 0


def draw_title_things():
    # Draw title and underline
    arcade.draw_text("Ransomware and Prevention Techniques", 140, text_height, arcade.color.WHITE, 22, 0,
                     "center", 'CALIBRI', True)
    arcade.draw_line(140, underline_height, 610, underline_height, arcade.color.WHITE, 3)

    # Load texture_1 -- computer screen
    texture_1 = arcade.load_texture("textures/computer_1.png")
    scale = 0.055
    arcade.draw_texture_rectangle(75, text_height, scale * texture_1.width, scale * texture_1.height,
                                  texture_1)
    # Load texture_2 -- ransomware clipart
    texture_2 = arcade.load_texture("textures/malware_1.png")
    scale = 0.17
    arcade.draw_texture_rectangle(650, text_height, scale * texture_2.width, scale * texture_2.height,
                                  texture_2)
    

def on_draw():
    arcade.start_render()
    draw_title_things()


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Computers and Society Poster")
    arcade.set_background_color(arcade.color.BLACK)
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
