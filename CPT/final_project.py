# Import necessary modules.
import arcade
import random

# Screen dimensions
WIDTH = 1450
HEIGHT = 795

# PRE-SET VARIABLES AND OBJECTS ---------------------------------------------------------------------------------------

# Title screen variables
on_title = True
on_fake_loading = False
title_button = [500, 200, 400, 150]

# Fake loading screen variables
on_topic_selection = False
loading_counter = 0
shapes_list = []
show_character_left = True          # show the loading screen character's left?
character_counter = 0
show_character_right = False        # show the loading screen character's right?


# Fake loading screen objects
class Shape:
    def __init__(self, x, y, width, height, delta_x, delta_y, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.color = color

    def move_shape(self):
        self.x += self.delta_x
        self.y += self.delta_y


class Rectangle(Shape):
    def draw_shape(self):
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, self.color)


class Ellipse(Shape):
    def draw_shape(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height, self.color)


class Circle(Shape):
    def draw_shape(self):
        arcade.draw_circle_filled(self.x, self.y, self.width, self.color)


for i in range(35):
    shape_type = random.randint(1, 3)
    color_red_strength = random.randint(0, 256)
    color_blue_strength = random.randint(0, 256)
    color_green_strength = random.randint(0, 256)
    opacity = random.randint(0, 256)

    if shape_type == 1:
        Shape = Rectangle(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(20, 50),
                          random.randint(20, 50), random.randint(-1, 2), random.randint(-1, 2), (color_red_strength,
                                                                                                 color_blue_strength,
                                                                                                 color_green_strength,
                                                                                                 opacity))

    elif shape_type == 2:
        Shape = Ellipse(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(20, 50),
                        random.randint(20, 50), random.randint(-1, 2), random.randint(-1, 2), (color_red_strength,
                                                                                               color_blue_strength,
                                                                                               color_green_strength,
                                                                                               opacity))

    elif shape_type == 3:
        Shape = Circle(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(20, 50),
                       random.randint(20, 50), random.randint(-1, 2), random.randint(-1, 2), (color_red_strength,
                                                                                              color_blue_strength,
                                                                                              color_green_strength,
                                                                                              opacity))

    shapes_list.append(Shape)

# Fake loading screen text
text_1 = "Malware is software that damages your device in various ways."
text_2 = "Practicing good computer \"hygiene\" is important."
text_3 = "Always update your devices!"
text_4 = "It may be a good time to update your GPU if you have a slow rendering speed."
text_5 = "It is recommended to invest in a better CPU if performance lags behind."
text_6 = "Secure everything. Watch where you upload and submit data."
text_7 = "Cyberbullying is a stupid and senseless action that does nothing good at all"
text_8 = "Giraffes are heartless creatures."
display_text = random.randint(1, 8)


# FUNCTIONS -----------------------------------------------------------------------------------------------------------


def on_update(delta_time):
    global loading_counter, on_fake_loading, on_topic_selection, character_counter, show_character_left, \
        show_character_right

    if on_fake_loading:
        loading_counter += delta_time
        if loading_counter >= 5.5:
            on_fake_loading = False
            on_topic_selection = True
        character_counter += delta_time
        if 2.3 <= character_counter <= 5.0:
            show_character_left = False
            show_character_right = True
        if character_counter >= 5.1:
            show_character_left = True
            show_character_right = False


def title_screen():
    if on_title:
        background = arcade.load_texture("background_title.png", 0, 0, 1500, 1134)
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
    global display_text, on_fake_loading, on_topic_selection
    if on_fake_loading:
        for Shape in shapes_list:
            Shape.draw_shape()
            Shape.move_shape()

        if display_text == 1:
            arcade.draw_text(text_1, 325, 275, arcade.color.WHITE, 24, align="center", font_name='arial', bold=True)
        elif display_text == 2:
            arcade.draw_text(text_2, 400, 275, arcade.color.WHITE, 24, align="center", font_name='arial', bold=True)
        elif display_text == 3:
            arcade.draw_text(text_3, 525, 275, arcade.color.WHITE, 24, align="center", font_name='arial', bold=True)
        elif display_text == 4:
            arcade.draw_text(text_4, 295, 275, arcade.color.WHITE, 24, align="center", font_name='arial', bold=True)
        elif display_text == 5:
            arcade.draw_text(text_5, 295, 275, arcade.color.WHITE, 24, align="center", font_name='arial', bold=True)
        elif display_text == 6:
            arcade.draw_text(text_6, 350, 275, arcade.color.WHITE, 24, align="center", font_name='arial', bold=True)
        elif display_text == 7:
            arcade.draw_text(text_7, 270, 275, arcade.color.WHITE, 24, align="center", font_name='arial', bold=True)
        elif display_text == 8:
            arcade.draw_text(text_8, 500, 275, arcade.color.WHITE, 24, align="center", font_name='arial', bold=True)

        loading_character_left = arcade.load_texture("game_n_watch_loading.png")
        loading_character_right = arcade.load_texture("game_n_watch_loading.png", mirrored=True)

        if show_character_left:
            arcade.draw_texture_rectangle(700, 450, 0.6*loading_character_left.width, 0.6*loading_character_left.height,
                                          loading_character_left)

        if show_character_right:
            arcade.draw_texture_rectangle(700, 450, 0.6*loading_character_right.width,
                                          0.6*loading_character_right.height, loading_character_right)


def on_draw():
    arcade.start_render()
    title_screen()
    fake_loading()


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global on_title, on_fake_loading
    # Buttons coordination and detection
    title_button_x, title_button_y, title_button_w, title_button_h = title_button

    if title_button_x < x < title_button_x + title_button_w and title_button_y < y < title_button_y + title_button_h \
            and on_title:
        title_button_click = arcade.load_sound("title_button_click.wav")
        arcade.play_sound(title_button_click)
        on_title = False
        on_fake_loading = True


def setup():
    arcade.open_window(WIDTH, HEIGHT, "???")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_update = on_update
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


setup()
