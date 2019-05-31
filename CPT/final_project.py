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
show_character_left = True          # show the loading screen character?
character_counter = 0
show_character_right = False        # show the loading screen character's mirrored version?
transition_alpha = 0

# Selection screen variables
on_science_screen = False
on_math_screen = False
on_compsci_screen = False
select_button_click = arcade.load_sound("select_button_click.wav")

science_button = [250, 450, 364, 95]
math_button = [735, 450, 364, 95]
compsci_button = [1220, 450, 364, 95]

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
        show_character_right, transition_alpha

    if on_fake_loading:
        loading_counter += delta_time
        if loading_counter >= 8.5:
            on_fake_loading = False
            on_topic_selection = True
        character_counter += delta_time
        if 2.3 <= character_counter <= 5.0:
            show_character_left = False
            show_character_right = True
        if 5.1 <= character_counter <= 7.4:
            show_character_left = True
            show_character_right = False
        if character_counter >= 7.5:
            show_character_left = False
            show_character_right = True
        if character_counter >= 5.3 and transition_alpha <= 256:
            transition_alpha += 170*delta_time
            if transition_alpha >= 256:
                transition_alpha -= 170*delta_time


def title_screen():
    if on_title:
        background = arcade.load_texture("background/background_title.png", 0, 0, 1500, 1134)
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
        transition_screen = arcade.load_texture("transition.png")

        if show_character_left:
            arcade.draw_texture_rectangle(700, 450, 0.6*loading_character_left.width, 0.6*loading_character_left.height,
                                          loading_character_left)

        if show_character_right:
            arcade.draw_texture_rectangle(700, 450, 0.6*loading_character_right.width,
                                          0.6*loading_character_right.height, loading_character_right)

        arcade.draw_texture_rectangle(700, 500, transition_screen.width, transition_screen.height,
                                      transition_screen, alpha=transition_alpha)


def topic_selection():
    if on_topic_selection:
        background = arcade.load_texture("background/background_selection.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)

        # Science Button and explanation render ----------------------------------------------------------------------
        science_button = arcade.load_texture("buttons/science_button.png")
        arcade.draw_texture_rectangle(250, 450, science_button.width, science_button.height, science_button)
        arcade.draw_text(" - Mini-programs that deal with optic formulae. \n - As well, biological drawings of "
                         "different \n organisms with explanations upon clicked.", 50, 325, arcade.color.BLACK, 18,
                         align="left", font_name='CALIBRI', bold=True)

        science_deco_1 = arcade.load_texture("decoration/science_button_deco_1.png")
        arcade.draw_texture_rectangle(150, 215, 0.7*science_deco_1.width, 0.7*science_deco_1.height, science_deco_1)

        science_deco_2 = arcade.load_texture("decoration/science_button_deco_2.png")
        arcade.draw_texture_rectangle(270, 70, 0.8*science_deco_2.width, 0.8*science_deco_2.height, science_deco_2)

        # Math Button and explanation render -------------------------------------------------------------------------
        math_button = arcade.load_texture("buttons/math_button.png")
        arcade.draw_texture_rectangle(735, 450, math_button.width, math_button.height, math_button)
        arcade.draw_text(" - A bunch of formulae that makes life easier. \n - Support for CAST rules, trigonometry,"
                         "\n sequences, series, and more.", 535, 325, arcade.color.BLACK, 18,
                         align="left", font_name='CALIBRI', bold=True)

        math_deco_1 = arcade.load_texture("decoration/math_button_deco_1.png")
        arcade.draw_texture_rectangle(765, 225, 0.8*math_deco_1.width, 0.8*math_deco_1.height, math_deco_1)

        math_deco_2 = arcade.load_texture("decoration/math_button_deco_2.png")
        arcade.draw_texture_rectangle(635, 70, 0.7*math_deco_2.width, 0.7*math_deco_2.height, math_deco_2)

        # Computer Science Button and explanation render --------------------------------------------------------------
        compsci_button = arcade.load_texture("buttons/compsci_button.png")
        arcade.draw_texture_rectangle(1220, 450, compsci_button.width, compsci_button.height, compsci_button)
        arcade.draw_text(" - Automated code generator, maybe? \n - As well, maybe an odd game \n in here somewhere.",
                         1045, 325, arcade.color.BLACK, 18, align="left", font_name='CALIBRI', bold=True)


def science_screen():
    if on_science_screen:
        background = arcade.load_texture("background/background_selection.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)


def on_draw():
    arcade.start_render()
    title_screen()
    fake_loading()
    topic_selection()
    science_screen()


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global on_title, on_fake_loading, on_topic_selection, on_science_screen, on_math_screen, on_compsci_screen

    # Buttons coordination and detection
    title_button_x, title_button_y, title_button_w, title_button_h = title_button
    science_button_x, science_button_y, science_button_w, science_button_h = science_button
    math_button_x, math_button_y, math_button_w, math_button_h = math_button
    compsci_button_x, compsci_button_y, compsci_button_w, compsci_button_h = compsci_button

    if title_button_x < x < title_button_x + title_button_w and title_button_y < y < title_button_y + title_button_h \
            and on_title:
        title_button_click = arcade.load_sound("title_button_click.wav")
        arcade.play_sound(title_button_click)
        on_title = False
        on_fake_loading = True

    if science_button_x - 364/2 < x < (science_button_x - 364/2) + science_button_w and science_button_y - 95/2 \
            < y < (science_button_y - 95/2) + science_button_h and on_topic_selection:
        arcade.play_sound(select_button_click)
        on_topic_selection = False
        on_science_screen = True


    if math_button_x - 364/2 < x < (math_button_x - 364/2) + math_button_w and math_button_y - 95/2 < y < \
            (math_button_y - 95/2) + math_button_h and on_topic_selection:
        arcade.play_sound(select_button_click)
        on_topic_selection = False
        on_math_screen = True


    if compsci_button_x - 364/2 < x < (compsci_button_x - 364/2) + compsci_button_w and compsci_button_y - 95/2 \
            < y < (compsci_button_y - 95/2) + compsci_button_h and on_topic_selection:
        arcade.play_sound(select_button_click)
        on_topic_selection = False
        on_compsci_screen = True



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
