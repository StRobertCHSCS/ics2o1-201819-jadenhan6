# Basis for all Arcade programs; import the plugin to make it work.
import arcade
import random
import math

# Screen dimensions
WIDTH = 1450
HEIGHT = 795

# Title screen variables
on_title = True
title_button = [500, 200, 400, 150]
on_fake_loading = False

# Fake loading screen text
text_1 = "Malware is software that damages your device in various ways."
text_2 = "Practicing good computer hygiene is important."
text_3 = "Always update your devices!"
text_4 = "It may be a good time to update your GPU if you have a slow rendering speed."
text_5 = "It is recommended to invest in a better CPU if performance lags behind."
text_6 = "a"


# Updating / Refreshing function.
def on_update(delta_time):
    pass


def title_screen():
    if on_title:
        background = arcade.load_texture("textures/1_title_screen/background_title.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, background.width, background.height, background)
        arcade.draw_text("TITLE SCREEN", 475, 490, arcade.color.BLACK, 60, align="center", font_name='calibri',
                         bold=True)
        arcade.draw_text("Created by: Jaden Han", 575, 450, arcade.color.BLACK, 18, align="center", font_name='calibri',
                         bold=True)

        arcade.draw_xywh_rectangle_filled(title_button[0], title_button[1], title_button[2], title_button[3],
                                          arcade.color.WHITE)
        arcade.draw_xywh_rectangle_outline(title_button[0], title_button[1], title_button[2], title_button[3],
                                           arcade.color.BLACK, 4)
        arcade.draw_text("START", title_button[0]+120, title_button[1]+50, arcade.color.BLACK, 46, align="center",
                         font_name='calibri', bold=True)

def fake_loading():
    if on_fake_loading:
        arcade.draw_rectangle_filled(100, 100, 4000, 2000, arcade.color.BLACK)




# Drawing function.
def on_draw():
    arcade.start_render()
    title_screen()
    fake_loading()


# Key input function.
def on_key_press(key, modifiers):
    pass


# Key release function.
def on_key_release(key, modifiers):
    pass


# Mouse click function
def on_mouse_press(x, y, button, modifiers):
    global on_title, on_fake_loading
    # Buttons coordination and detection
    title_button_x, title_button_y, title_button_w, title_button_h = title_button

    # If button 1 has been clicked, and it hasn't already been clicked before, initiate button 1's moving sequence
    if (title_button_x < x < title_button_x + title_button_w and title_button_y < y < title_button_y + title_button_h):
        on_title = False
        on_fake_loading = True


def setup():
    arcade.open_window(WIDTH, HEIGHT, "???")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods; uses our OWN functions
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_update = on_update
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
