import arcade

# Set constants for screen height and width
WIDTH = 1080
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


def make_background():
    background = arcade.load_texture("textures/background.jpg")
    arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, background.width, background.height, background)


def draw_title_things():
    # Draw title
    arcade.draw_text("Ransomware and Prevention Techniques", 240, text_height, arcade.color.DARK_BLUE, 30, 0,
                     "center", 'ARIAL', True)

    # Draw underline
    arcade.draw_line(220, underline_height, 900, underline_height, arcade.color.DARK_BLUE, 3)

    # Load texture_1 -- computer screen
    texture_1 = arcade.load_texture("textures/computer_1.png")
    scale = 0.055
    arcade.draw_texture_rectangle(150, text_height, scale * texture_1.width, scale * texture_1.height,
                                  texture_1)

    # Load texture_2 -- ransomware clipart
    texture_2 = arcade.load_texture("textures/malware_1.png")
    scale = 0.17
    arcade.draw_texture_rectangle(950, text_height, scale * texture_2.width, scale * texture_2.height,
                                  texture_2)


def draw_left():
    # TOP LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(0, 650, 350, 650, arcade.color.DARK_BLUE, 4)
    # BOTTOM LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(0, 550, 300, 550, arcade.color.DARK_BLUE, 4)
    # CONNECTOR LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(300, 550, 350, 650, arcade.color.DARK_BLUE, 4)

    # FILL the lines; rectangle
    arcade.draw_xywh_rectangle_filled(0, 550, 300, 100, arcade.color.SKY_BLUE)
    # FILL the lines; triangle
    arcade.draw_triangle_filled(350, 650, 300, 650, 300, 550, arcade.color.SKY_BLUE)

    # Text: "What is a ransomware"?
    arcade.draw_text("What is a ransomware?", 15, 590, arcade.color.DARK_BLUE, 24, 0, "center", 'calibri', True)
    arcade.draw_line(10, 580, 280, 580, arcade.color.DARK_BLUE, 3)

    # BULLET POINT AND TEXT 1
    arcade.draw_circle_filled(25, 515, 5, arcade.color.BLACK)
    arcade.draw_text("A malware that forcefully encrypts data, \nand demands ransom to save malware-led",
                     35, 505, arcade.color.BLACK, 14, 0)
    arcade.draw_text("data destruction.", 35, 487, arcade.color.DARK_RED, 14)

    # BULLET POINT AND TEXT 2
    arcade.draw_circle_filled(25, 455, 5, arcade.color.BLACK)
    arcade.draw_text("If ransom isn't paid, the data is destroyed. \nNo guarantee of decryption either.",
                     35, 440, arcade.color.BLACK, 14)

    # BULLET POINT AND TEXT 3
    arcade.draw_circle_filled(25, 420, 5, arcade.color.BLACK)
    arcade.draw_text("e.g. WannaCry, CryptoLocker, etc.", 35, 415, arcade.color.RED, 14)

    # EXAMPLE IMAGE
    ransomware_image = arcade.load_texture("textures/ransomware_image.png")
    arcade.draw_texture_rectangle(550, 525, 0.55*ransomware_image.width, 0.55*ransomware_image.height,
                                  ransomware_image)




def on_draw():
    arcade.start_render()
    make_background()
    draw_title_things()
    draw_left()


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Computers and Society Poster")
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
