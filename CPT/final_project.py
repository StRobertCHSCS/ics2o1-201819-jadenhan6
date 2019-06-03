# TODO: finish money functions
#   test button functionality; some are a bit wonkier than others.
#   can leave out the first of each function type... they probably have been verified.
#   add big texts.
#   comment on things

# Import necessary modules.
import arcade
import random
import math

# Set screen dimensions
WIDTH = 1450
HEIGHT = 795

# cheat variable. if pressed, skips the loading screen. meant to be used only in development only
W_pressed = False

# Set variable that will collect data from various computing functions in program.
user_input = " "


# PRE-SET VARIABLES AND OBJECTS ---------------------------------------------------------------------------------------


# Set back_button's click sound and coordinate set.
back_button = [100, 725, 102.4, 102.4]
back_button_click = arcade.load_sound("sounds/back_button_click.wav")


# Title screen variables; including the button's coordinate set.
on_title = True                             # Boolean to see if program is on title.
on_fake_loading = False                     # Boolean to see if program is on loading.
title_button = [500, 200, 400, 150]


# Variable that regulates inadvertent (or user-instigated) button spamming.
button_cooldown = 0.4


# Fake loading screen variables
on_topic_selection = False          # Boolean to see if program is on topic selection
loading_counter = 0                 # the counter of the loading screen, measured in seconds.
shapes_list = []                    # INIT a list for Shape rendering.
show_character_left = True          # show the loading screen character?
character_counter = 0               # counts down character's time on screen
show_character_right = False        # show the loading screen character's mirrored version?
transition_alpha = 0                # tracks visibility of transition screen.


# Selection screen variables, including button coordinate sets.
on_science_screen = False
on_math_screen = False
on_compsci_screen = False
select_button_click = arcade.load_sound("sounds/select_button_click.wav")

science_button = [250, 450, 364, 95]
math_button = [735, 450, 364, 95]
compsci_button = [1220, 450, 364, 95]


# Science screen variables
on_bio_screen = False
on_optics_screen = False

bio_button = [250, 450, 408.8, 138.6]
optics_button = [1150, 450, 408.8, 138.6]


# Optics screen variables
on_mirror_screen = False
on_refraction_screen = False

mirror_button = [350, 450, 596.4, 100.8]
refraction_button = [1050, 450, 596.4, 100.8]


# Math screen variables
on_cast_screen = False
on_sequences_screen = False
on_money_screen = False

cast_button = [250, 450, 262, 61]
seq_series_button = [710, 450, 262, 61]
money_button = [1200, 450, 262, 61]


# CAST screen variables
on_sin_screen = False
on_cos_screen = False
on_tan_screen = False

sin_button = [290, 450, 254, 65]
cos_button = [720, 450, 254, 65]
tan_button = [1170, 450, 254, 65]


# Sequences screen variables
on_arith_seq_screen = False
on_geo_seq_screen = False
on_arith_series_screen = False
on_geo_series_screen = False

arith_seq_button = [310, 450, 418, 68]
geo_seq_button = [310, 300, 418, 68]
arith_series_button = [1170, 450, 418, 68]
geo_series_button = [1170, 300, 418, 68]


# Money screen variables
on_simple_interest_screen = False
on_compound_interest_screen = False
on_present_value_screen = False

simple_interest_button = [260, 450, 334, 68]
compound_interest_button = [710, 450, 390, 68]
present_value_button = [1200, 450, 316, 68]

# Calculator - button coordinate sets
button_one = [1000, 475, 75, 75]
button_two = [1100, 475, 75, 75]
button_three = [1200, 475, 75, 75]
button_four = [1000, 375, 75, 75]
button_five = [1100, 375, 75, 75]
button_six = [1200, 375, 75, 75]
button_seven = [1000, 275, 75, 75]
button_eight = [1100, 275, 75, 75]
button_nine = [1200, 275, 75, 75]
button_zero = [1000, 175, 75, 75]
button_decimal = [1100, 175, 75, 75]
button_negative = [1000, 575, 75, 75]
button_AC = [1200, 575, 75, 75]
button_ENTER = [1200, 175, 75, 75]


# Determines if decimal or a negative has been placed.
decimal_placed = False
negative_placed = False


# Variables for calculation.
input_variable_1 = 0
input_variable_2 = 0
input_variable_3 = 0
result_1 = 0
result_2 = 0

# Boolean that determines if the answer will be drawn to a screen.
# Will only be set TRUE after needed variables have been entered. If TRUE, draws the concluding statement w/ answer.
answer_drawn = False


# Fake loading screen objects; create a class
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


# Create a rectangle subclass to be called.
class Rectangle(Shape):
    def draw_shape(self):
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, self.color)


# Create an ellipse subclass to be called.
class Ellipse(Shape):
    def draw_shape(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height, self.color)


# Create a circle subclass to be called.
class Circle(Shape):
    def draw_shape(self):
        arcade.draw_circle_filled(self.x, self.y, self.width, self.color)


# Render a Shape class 35 times.
for i in range(35):
    # randomizer; picks color, size, type, opacity and movement speeds at random.
    shape_type = random.randint(1, 3)
    color_red_strength = random.randint(0, 256)
    color_blue_strength = random.randint(0, 256)
    color_green_strength = random.randint(0, 256)
    opacity = random.randint(0, 256)

    # Depending on the shape type, render different subclasses of Shape object defined above.
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

    # Uploads newly created shape to the shapes_list specified above.
    shapes_list.append(Shape)


# Create Instructions object; textboxes that will find itself on every calculation screen.
class Instructions:
    def __init__(self, text, x, y, color, size, bold):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.bold = bold

    # Function that will draw the instructions
    def draw_instructions(self):
        arcade.draw_text(self.text, self.x, self.y, self.color, self.size, bold=self.bold)


# Fake loading screen text
text_1 = "Malware is software that damages your device in various ways."
text_2 = "Practicing good computer \"hygiene\" is important."
text_3 = "Always update your devices!"
text_4 = "It may be a good time to update your GPU if you have a slow rendering speed."
text_5 = "It is recommended to invest in a better CPU if performance lags behind."
text_6 = "Secure everything. Watch where you upload and submit data."
text_7 = "Cyberbullying is a stupid and senseless action that does nothing good at all"
text_8 = "Giraffes are heartless creatures."

# Sets a variable that determines what splash text will be shown upon launch.
# Go to fake_screen() function for application of this variable.
display_text = random.randint(1, 8)


# FUNCTIONS -----------------------------------------------------------------------------------------------------------

# "Calculator" function that will appear where user-input and computation is needed. Click logic is stored below.
def draw_calculator():
    # Draw calculator background.
    arcade.draw_xywh_rectangle_filled(950, 150, 375, 625, arcade.color.GRAY)
    arcade.draw_xywh_rectangle_outline(950, 150, 375, 625, arcade.color.BLACK, 3)
    arcade.draw_xywh_rectangle_filled(1000, 670, 275, 90, arcade.color.WHITE)
    arcade.draw_xywh_rectangle_outline(1000, 670, 275, 90, arcade.color.BLACK, 3)
    arcade.draw_text(user_input, 1130, 705, arcade.color.BLACK, 22)  # Displays user_input variable to screen.

    # Button "1". The coordinate sets are defined above, as well.
    arcade.draw_xywh_rectangle_filled(1000, 475, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1000, 475, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("1", 1032.5, 503, arcade.color.WHITE, 22, bold=True)

    # Button "2". Draws the "button", and so on...
    arcade.draw_xywh_rectangle_filled(1100, 475, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1100, 475, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("2", 1132.5, 503, arcade.color.WHITE, 22, bold=True)

    # Button "3"
    arcade.draw_xywh_rectangle_filled(1200, 475, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1200, 475, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("3", 1232.5, 503, arcade.color.WHITE, 22, bold=True)

    # Button "4"
    arcade.draw_xywh_rectangle_filled(1000, 375, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1000, 375, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("4", 1032.5, 403, arcade.color.WHITE, 22, bold=True)

    # Button "5"
    arcade.draw_xywh_rectangle_filled(1100, 375, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1100, 375, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("5", 1132.5, 403, arcade.color.WHITE, 22, bold=True)

    # Button "6"
    arcade.draw_xywh_rectangle_filled(1200, 375, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1200, 375, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("6", 1232.5, 403, arcade.color.WHITE, 22, bold=True)

    # Button "7"
    arcade.draw_xywh_rectangle_filled(1000, 275, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1000, 275, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("7", 1032.5, 303, arcade.color.WHITE, 22, bold=True)

    # Button "8"
    arcade.draw_xywh_rectangle_filled(1100, 275, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1100, 275, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("8", 1132.5, 303, arcade.color.WHITE, 22, bold=True)

    # Button "9"
    arcade.draw_xywh_rectangle_filled(1200, 275, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1200, 275, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("9", 1232.5, 303, arcade.color.WHITE, 22, bold=True)

    # Button "0"
    arcade.draw_xywh_rectangle_filled(1000, 175, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1000, 175, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("0", 1032.5, 203, arcade.color.WHITE, 22, bold=True)

    # Button "."
    arcade.draw_xywh_rectangle_filled(1100, 175, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1100, 175, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text(".", 1132.5, 203, arcade.color.WHITE, 22, bold=True)

    # Button "-"
    arcade.draw_xywh_rectangle_filled(1000, 575, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1000, 575, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("-", 1032.5, 603, arcade.color.WHITE, 22, bold=True)

    # Button "ENTER"
    arcade.draw_xywh_rectangle_filled(1200, 175, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1200, 175, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("ENTER", 1215, 205, arcade.color.WHITE, 14, bold=True)

    # Button "AC"
    arcade.draw_xywh_rectangle_filled(1200, 575, 75, 75, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1200, 575, 75, 75, arcade.color.WHITE, 2)
    arcade.draw_text("AC", 1217.5, 603, arcade.color.WHITE, 22, bold=True)


# Back_button function. Will be called at almost every screen.
def draw_back_button():
    back_button = arcade.load_texture("buttons/back_button.png")
    arcade.draw_texture_rectangle(100, 725, 0.4 * back_button.width, 0.4 * back_button.height, back_button)


# Reset variables function when user exits calculator environment.
def reset_all_variables():
    global decimal_placed, user_input, input_variable_1, input_variable_2, input_variable_3, result_1, result_2
    global negative_placed, answer_drawn

    decimal_placed = False
    negative_placed = False
    user_input = " "
    input_variable_1 = 0
    input_variable_2 = 0
    input_variable_3 = 0
    result_1 = 0
    result_2 = 0
    answer_drawn = False


# Animation, timer, cooldown functions, etc.
def on_update(delta_time):
    global loading_counter, on_fake_loading, on_topic_selection, character_counter
    global show_character_left, show_character_right, transition_alpha
    global button_cooldown, on_science_screen, on_title

    global on_math_screen

    # Fake loading screen animation.
    if on_fake_loading:
        loading_counter += delta_time           # Add 1/60s to counter.
        if loading_counter >= 8.5:              # Once loading_counter exceeds 8.5s, move to next screen
            on_fake_loading = False
            on_topic_selection = True
        character_counter += delta_time         # Add 1/60s to character counter
        if 2.3 <= character_counter <= 5.0:     # At 2.3s, show the mirrored version of Mr. Game and Watch.
            show_character_left = False         # These variables here are depicted below under fake_loading().
            show_character_right = True
        if 5.1 <= character_counter <= 7.4:     # At 5.1s, show the normal version of character.
            show_character_left = True
            show_character_right = False
        if character_counter >= 7.5:            # At 7.5s, say screw it and mirror the thing again.
            show_character_left = False
            show_character_right = True
        if character_counter >= 5.3 and transition_alpha <= 256:    # At 5.3, slowly make the white screen visible.
            transition_alpha += 170*delta_time
            if transition_alpha >= 256:                     # At full opacity, attempt to make white screen transparent.
                transition_alpha -= 170*delta_time

    # On each screen, count down button_cooldown by 1/60s.
    # This is done as Python seems to render clicks quickly; meaning if two buttons share the same coordinates spot
    # but on different screens (with pressing on the first one directly leading to the screen with the second),
    # Python registers clicks twice, making for the screen after the first button to be skipped.

    # To combat this, button_cooldown has been introduced; at every new screen, count down the 0.4s delay to
    # clicking buttons; by -1/60s. (aka delta_time)

    button_cooldown -= delta_time

    if W_pressed:
        on_title = False
        on_math_screen = True


# Render title screen
def title_screen():
    if on_title:            # variable to see if program is on title_screen
        background = arcade.load_texture("background/background_title.png", 0, 0, 1500, 1134)   # Draw background
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, background.width, background.height, background)
        arcade.draw_text("TITLE SCREEN", 475, 490, arcade.color.BLACK, 60, align="center", font_name='calibri',
                         bold=True)
        arcade.draw_text("Created by: Jaden Han", 575, 450, arcade.color.BLACK, 18, align="center", font_name='calibri',
                         bold=True)

        # Draws title button, in accordance to the title_button coordinate set defined at the top.
        arcade.draw_xywh_rectangle_filled(title_button[0], title_button[1], title_button[2], title_button[3],
                                          arcade.color.WHITE)
        arcade.draw_xywh_rectangle_outline(title_button[0], title_button[1], title_button[2], title_button[3],
                                           arcade.color.BLACK, 4)
        arcade.draw_text("START", title_button[0]+120, title_button[1]+50, arcade.color.BLACK, 46, align="center",
                         font_name='calibri', bold=True)


# Render fake loading screen
def fake_loading():
    global display_text, on_fake_loading, on_topic_selection
    if on_fake_loading:
        for Shape in shapes_list:       # render each Shape in shapes_list here!
            Shape.draw_shape()          # make sure to draw and move the shapes around.
            Shape.move_shape()

        # Determines what type of text the user will see, depending on the result of random.randint(1, 8) above.
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

        # Load character's normal and mirror version, for use for animation in on_update() function.
        loading_character_left = arcade.load_texture("game_n_watch_loading.png")
        loading_character_right = arcade.load_texture("game_n_watch_loading.png", mirrored=True)

        # Load white-screen transition image.
        transition_screen = arcade.load_texture("transition.png")

        # Render the normal image if told so.
        if show_character_left:
            arcade.draw_texture_rectangle(700, 450, 0.6*loading_character_left.width, 0.6*loading_character_left.height,
                                          loading_character_left)

        # Render the mirrored image if told so.
        if show_character_right:
            arcade.draw_texture_rectangle(700, 450, 0.6*loading_character_right.width,
                                          0.6*loading_character_right.height, loading_character_right)

        # Render the white-screen transition image, with opacity variable, manipulated in on_update().
        arcade.draw_texture_rectangle(700, 500, transition_screen.width, transition_screen.height,
                                      transition_screen, alpha=transition_alpha)


# Render topic / course selection screen.
def topic_selection():
    if on_topic_selection:
        background = arcade.load_texture("background/background_selection.png")     # Draw background
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


# Render SNC2D screen.
def science_screen():
    if on_science_screen:
        background = arcade.load_texture("background/background_selection.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)

        draw_back_button()

        # Render the biology button.
        bio_button = arcade.load_texture("buttons/bio_button.png")
        arcade.draw_texture_rectangle(250, 450, 1.4*bio_button.width, 1.4*bio_button.height, bio_button)
        arcade.draw_text(" - Includes interactive diagrams for \n organ systems.", 100, 318, arcade.color.BLACK,
                         18, align="left", font_name='calibri', bold=True)

        # Render the optics button.
        optics_button = arcade.load_texture("buttons/optics_button.png")
        arcade.draw_texture_rectangle(1150, 450, 1.4*optics_button.width, 1.4*optics_button.height, optics_button)
        arcade.draw_text(" - Formulae calculator; like magnification \n and indices of refraction.", 950, 318,
                         arcade.color.BLACK, 18, align="left", font_name='calibri', bold=True)


# Render the biology screen.
def bio_screen():
    if on_bio_screen:
        background = arcade.load_texture("background/background_bio.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)

        draw_back_button()


# Render the optics screen.
def optics_screen():
    if on_optics_screen:
        background = arcade.load_texture("background/background_optics.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)

        draw_back_button()

        # Draw button that paths to Mirror and Magnification
        mirror_button = arcade.load_texture("buttons/mirror_button.png")
        arcade.draw_texture_rectangle(350, 450, 1.4*mirror_button.width, 1.4*mirror_button.height, mirror_button)
        arcade.draw_text(" - Calculates focal length and magnification factor, \n given object distance and "
                         "image distance.", 75, 325, arcade.color.BLACK, 22, align="left", font_name='calibri',
                         bold=True)

        # Draw button that paths to Indices of Refraction
        refraction_button = arcade.load_texture("buttons/refraction_button.png")
        arcade.draw_texture_rectangle(1050, 450, 1.4*refraction_button.width, 1.4*refraction_button.height,
                                      refraction_button)
        arcade.draw_text(" - Calculates an index of refraction \n given the speed of light in a specific medium.",
                         825, 325, arcade.color.BLACK, 22, align="left", font_name='calibri', bold=True)


# Render the mirror and magnification screen.
def mirror_screen():
    global answer_drawn, mirror_outputs

    if on_mirror_screen:        # checks if the user is on this screen, before proceeding with the following logic.
        background = arcade.load_texture("background/background_optics.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        # Load back button and calculator.
        draw_back_button()
        draw_calculator()

        # Load images
        formula_1 = arcade.load_texture("formula/mirror_formula.png")
        arcade.draw_texture_rectangle(400, 500, formula_1.width, formula_1.height, formula_1)
        formula_2 = arcade.load_texture("formula/magnification_formula.png")
        arcade.draw_texture_rectangle(600, 500, formula_2.width, formula_2.height, formula_2)

        # Load instructions
        intro_mirror = Instructions("This screen deals with mirror and magnification equations. \nIs one-way; does"
                                    " not support ho or hi, or finding di or do yet."
                                    "\n Only calculates f and m in this case, given do and di.", 300, 600,
                                    arcade.color.BLACK, 18, False)

        step_one_mirror = Instructions("1. Enter do first, then di.", 300, 400, arcade.color.BLACK, 18, True)
        step_two_mirror = Instructions("2. Remember only five-characters long inputs are supported.", 300, 350,
                                       arcade.color.BLACK, 18, True)
        step_three_mirror = Instructions("3. Program will output focal length and magnification factor \n"
                                         "derived off the formulae. \n \n Note that entering the same value for both "
                                         "variables \n won't yield results.", 300, 230, arcade.color.BLACK, 18, True)

        # If told so, render the concluding sentence with the answer included.
        if answer_drawn:
            mirror_outputs = Instructions("The focal length is " + str(round(result_1, 2)) + ", and the magnification "
                                          "factor is " + str(round(result_2, 2)) + ", \n when object distance is "
                                          + str(input_variable_1) + " and image distance is " + str(input_variable_2) +
                                          ". \n Press AC to try another calculation!", 200, 100, arcade.color.BLACK, 22,
                                          False)

        if not answer_drawn:
            mirror_outputs = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        # Draw all the above instances of the Instructions class.
        intro_mirror.draw_instructions()
        step_one_mirror.draw_instructions()
        step_two_mirror.draw_instructions()
        step_three_mirror.draw_instructions()
        mirror_outputs.draw_instructions()


# Render the refraction screen.
def refraction_screen():
    global answer_drawn, refraction_output

    if on_refraction_screen:
        background = arcade.load_texture("background/background_optics.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        # Load back button and calculator. For the next screens, these comments will not appear,
        # as it's the same thing anyway
        draw_back_button()
        draw_calculator()

        # Load images
        formula = arcade.load_texture("formula/refraction_formula.png")
        arcade.draw_texture_rectangle(500, 520, formula.width, formula.height, formula)

        # Load instructions
        intro_refraction = Instructions("Calculates indices of refraction, given speed of light \n in two different"
                                        " media. Only able to calculate n, not c or v.", 300, 600, arcade.color.BLACK,
                                        18, False)

        step_one_refraction = Instructions("1. Enter speed of light in a specific medium aka v. \n Unit is understood "
                                           "to be 10^8 metres per second.", 300, 400,
                                           arcade.color.BLACK, 18, True)

        step_two_refraction = Instructions("2. Program will spit out index of refraction or n, through n = c/v. \n "
                                           "c is given; 3.00 x 10^8 m/s. \n"
                                           "Ensure your value of v does NOT end with a decimal!!", 300,
                                           300, arcade.color.BLACK, 18, True)

        if answer_drawn:
            refraction_output = Instructions("The index of refraction is about " + str(round(result_1, 2)) +
                                             ", \n when the speed of light in your medium (v) is " +
                                             str(input_variable_1) + " 10^8m/s. \n Press AC to try another calculation."
                                             , 200, 180, arcade.color.BLACK, 22, True)

        if not answer_drawn:
            refraction_output = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_refraction.draw_instructions()
        step_one_refraction.draw_instructions()
        step_two_refraction.draw_instructions()
        refraction_output.draw_instructions()


# Render the MCR3U screen.
def math_screen():
    if on_math_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)

        draw_back_button()

        # Draw button that paths to CAST
        cast_button = arcade.load_texture("buttons/CAST_button.png")
        arcade.draw_texture_rectangle(250, 450, 1.4*cast_button.width, 1.4*cast_button.height, cast_button)
        arcade.draw_text(" - Given an trigonometric ratio, figures out \n two angles in degrees that yield that ratio. "
                         "\n 0 ≤ θ ≤ 360. ", 75, 325, arcade.color.BLACK, 18, align="left", font_name='calibri',
                         bold=True)

        # Draw button that paths to Sequences and Series
        seq_series_button = arcade.load_texture("buttons/seq_series_button.png")
        arcade.draw_texture_rectangle(710, 450, 1.4*seq_series_button.width, 1.4*seq_series_button.height,
                                      seq_series_button)
        arcade.draw_text(" - Calculates a term in a series or the \nsum of a specific amount of terms in a sequence.",
                         510, 340, arcade.color.BLACK, 18, align="left", font_name='calibri',
                         bold=True)

        # Draw button that paths to Finances
        money_button = arcade.load_texture("buttons/money_button.png")
        arcade.draw_texture_rectangle(1200, 450, 1.4*money_button.width, 1.4*money_button.height, money_button)
        arcade.draw_text(" - Figures out simple and compound interests, \nincluding the present value.",
                         1000, 340, arcade.color.BLACK, 18, align="left", font_name='calibri',
                         bold=True)


# Render the CAST (ratio selection) screen.
def cast_screen():
    if on_cast_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)

        draw_back_button()

        # Draw button that paths to sin ratio conversion
        sin_button = arcade.load_texture("buttons/sin_button.png")
        arcade.draw_texture_rectangle(290, 450, 1.4*sin_button.width, 1.4*sin_button.height, sin_button)
        arcade.draw_text(" - Converts a sine ratio to two \n corresponding angles.",
                         130, 345, arcade.color.BLACK, 18, align="left", font_name='calibri',
                         bold=True)

        # Draw button that paths to cos ratio conversion
        cos_button = arcade.load_texture("buttons/cos_button.png")
        arcade.draw_texture_rectangle(725, 450, 1.4*cos_button.width, 1.4*cos_button.height, cos_button)
        arcade.draw_text(" - Converts a cosine ratio to two \n corresponding angles.",
                         565, 345, arcade.color.BLACK, 18, align="left", font_name='calibri',
                         bold=True)

        # Draw button that paths to tan ratio conversion
        tan_button = arcade.load_texture("buttons/tan_button.png")
        arcade.draw_texture_rectangle(1170, 450, 1.4*tan_button.width, 1.4*tan_button.height, tan_button)
        arcade.draw_text(" - Converts a tangent ratio to two \n corresponding angles.",
                         1010, 345, arcade.color.BLACK, 18, align="left", font_name='calibri',
                         bold=True)


# Render the sine ratio screen.
def sin_screen():
    global answer_drawn, sin_outputs

    if on_sin_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/cast_formula.png")
        arcade.draw_texture_rectangle(400, 505, 0.4*formula_1.width, 0.4*formula_1.height, formula_1)
        formula_2 = arcade.load_texture("formula/cast_image.png")
        arcade.draw_texture_rectangle(720, 510, 0.9*formula_2.width, 0.9*formula_2.height, formula_2)

        intro_sin = Instructions("This screen deals with finding TWO angles, given a SINE ratio."
                                 "\n Make sure your value is between -1 and 1, not including 0. \n "
                                 "Not done in radians; degrees only!", 300, 600, arcade.color.BLACK, 18, False)

        step_one_sin = Instructions("1. Enter a four-digit sine ratio number. (e.g. 0.8154)", 300, 400,
                                    arcade.color.BLACK, 18, True)
        step_two_sin = Instructions("2. Negatives are supported. Cannot be zero, however.", 300, 350,
                                       arcade.color.BLACK, 18, True)
        step_three_sin = Instructions("3. Program will output the two angles for your SINE ratio \n"
                                      "that exist within a 0 degrees to \n360 degrees domain.", 300, 250,
                                         arcade.color.BLACK, 18, True)

        if answer_drawn:
            # Reconvert input_variable to the RATIO, not the angle, as input_variable is computed to be the ANGLE once answer is inputted.
            sin_outputs = Instructions("If sinθ is " + str(input_variable_1) +
                                       " two angles exist: " + str(result_1) + " and " + str(result_2) +
                                       ". \nBoth in degrees.", 200, 170, arcade.color.BLACK, 22, False)

        if not answer_drawn:
            sin_outputs = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_sin.draw_instructions()
        step_one_sin.draw_instructions()
        step_two_sin.draw_instructions()
        step_three_sin.draw_instructions()
        sin_outputs.draw_instructions()


# Render the cosine ratio screen.
def cos_screen():
    global answer_drawn, cos_outputs

    if on_cos_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/cast_formula.png")
        arcade.draw_texture_rectangle(400, 505, 0.4 * formula_1.width, 0.4 * formula_1.height, formula_1)
        formula_2 = arcade.load_texture("formula/cast_image.png")
        arcade.draw_texture_rectangle(720, 510, 0.9 * formula_2.width, 0.9 * formula_2.height, formula_2)

        intro_cos = Instructions("This screen deals with finding TWO angles, given a COSINE ratio."
                                 "\n Make sure your value is between -1 and 1, not including 0. \n "
                                 "Not done in radians; degrees only!", 300, 600, arcade.color.BLACK, 18, False)

        step_one_cos = Instructions("1. Enter a four-digit cosine ratio number. (e.g. 0.8154)", 300, 400,
                                    arcade.color.BLACK, 18, True)
        step_two_cos = Instructions("2. Negatives are supported. Cannot be zero, however.", 300, 350,
                                       arcade.color.BLACK, 18, True)
        step_three_cos = Instructions("3. Program will output the two angles for your COSINE ratio \n"
                                      "that exist within a 0 degrees to \n360 degrees domain.", 300, 250,
                                         arcade.color.BLACK, 18, True)

        if answer_drawn:
            cos_outputs = Instructions("If cosθ is " + str(input_variable_1) +
                                       " two angles exist: " + str(result_1) + " and " + str(result_2) +
                                       ". \nBoth in degrees.", 200, 170, arcade.color.BLACK, 22, False)

        if not answer_drawn:
            cos_outputs = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_cos.draw_instructions()
        step_one_cos.draw_instructions()
        step_two_cos.draw_instructions()
        step_three_cos.draw_instructions()
        cos_outputs.draw_instructions()


# Render the tangent ratio screen.
def tan_screen():
    global answer_drawn, tan_outputs

    if on_tan_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/cast_formula.png")
        arcade.draw_texture_rectangle(400, 505, 0.4 * formula_1.width, 0.4 * formula_1.height, formula_1)
        formula_2 = arcade.load_texture("formula/cast_image.png")
        arcade.draw_texture_rectangle(720, 510, 0.9 * formula_2.width, 0.9 * formula_2.height, formula_2)

        intro_tan = Instructions("This screen deals with finding TWO angles, given a TANGENT ratio."
                                 "\n Make sure your value is between -1 and 1, not including 0. \n "
                                 "Not done in radians; degrees only!", 300, 600, arcade.color.BLACK, 18, False)

        step_one_tan = Instructions("1. Enter a four-digit tangent ratio number. (e.g. 0.8154)", 300, 400,
                                    arcade.color.BLACK, 18, True)
        step_two_tan = Instructions("2. Negatives are supported. Cannot be zero, however.", 300, 350,
                                       arcade.color.BLACK, 18, True)
        step_three_tan = Instructions("3. Program will output the two angles for your TANGENT ratio \n" 
                                      "that exist within a 0 degrees to \n360 degrees domain.", 300, 250,
                                         arcade.color.BLACK, 18, True)

        if answer_drawn:
            tan_outputs = Instructions("If tanθ is " + str(input_variable_1) +
                                       " two angles exist: " + str(result_1) + " and " + str(result_2) +
                                       ". \nBoth in degrees.", 200, 170, arcade.color.BLACK, 22, False)
        if not answer_drawn:
            tan_outputs = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_tan.draw_instructions()
        step_one_tan.draw_instructions()
        step_two_tan.draw_instructions()
        step_three_tan.draw_instructions()
        tan_outputs.draw_instructions()


# Render the sequences / series screen
def sequences_screen():
    if on_sequences_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()

        arcade.draw_text(" - Finds a specific TERM of a sequence, \n given a, d or r, and n.",
                         100, 525, arcade.color.BLACK, 20, align="left", font_name='calibri',
                         bold=True)

        arcade.draw_text(" - Finds a specific SUM of a sequence, \n given a, d or r, and n.",
                         975, 525, arcade.color.BLACK, 20, align="left", font_name='calibri',
                         bold=True)

        # Draw button that paths to arithmetic sequence
        arith_seq_button = arcade.load_texture("buttons/arith_seq_button.png")
        arcade.draw_texture_rectangle(310, 450, 1.4 * arith_seq_button.width, 1.4 * arith_seq_button.height,
                                      arith_seq_button)

        # Draw button that paths to geometric sequence
        geo_seq_button = arcade.load_texture("buttons/geo_seq_button.png")
        arcade.draw_texture_rectangle(310, 300, 1.4 * geo_seq_button.width, 1.4 * geo_seq_button.height, geo_seq_button)

        # Draw button that paths to arithmetic series
        arith_series_button = arcade.load_texture("buttons/arith_series_button.png")
        arcade.draw_texture_rectangle(1170, 450, 1.4 * arith_series_button.width, 1.4 * arith_series_button.height,
                                      arith_series_button)

        # Draw button that paths to geometric series
        geo_series_button = arcade.load_texture("buttons/geo_series_button.png")
        arcade.draw_texture_rectangle(1170, 300, 1.4 * geo_series_button.width, 1.4 * geo_series_button.height,
                                      geo_series_button)


# Render the arithmetic sequences screen
def arithmetic_sequence():
    global answer_drawn, arith_seq_output

    if on_arith_seq_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/arith_seq_formula.png")
        arcade.draw_texture_rectangle(600, 505, 0.9 * formula_1.width, 0.9 * formula_1.height, formula_1)

        intro_arith_seq = Instructions("Calculates a TERM of an arithmetic sequence, given the 1st term, \n"
                                       "the common difference, and the number of the term."
                                       "\n -> The number of term MUST be an integer; \n cannot have a \"2.7th\" "
                                       "term of a sequence.", 300, 600, arcade.color.BLACK, 18, False)

        step_one_arith_seq = Instructions("1. Enter a (first term), d (common difference), THEN n (term number)", 300,
                                          375, arcade.color.BLACK, 18, True)
        step_two_arith_seq = Instructions("2. INPUT IN ORDER!! a -> d -> n \n Refrain from entering 0 on any of them. "
                                          "\nAlso, refrain from having your answer be 0 as well, somehow",
                                          300, 295, arcade.color.BLACK, 18, True)
        step_three_arith_seq = Instructions("3. Program will output the nth term of your arithmetic sequence.", 300,
                                            250,arcade.color.BLACK, 18, True)

        if answer_drawn:
            arith_seq_output = Instructions("If the first term of your sequence (a) is " + str(input_variable_1) +
                                            ", with your common \n difference (d) being " + str(input_variable_2) +
                                            ", the " + str(input_variable_3) + "th term of this sequence is " +
                                            str(result_1) + ".", 200, 100, arcade.color.BLACK, 22, True)

        if not answer_drawn:
            arith_seq_output = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_arith_seq.draw_instructions()
        step_one_arith_seq.draw_instructions()
        step_two_arith_seq.draw_instructions()
        step_three_arith_seq.draw_instructions()
        arith_seq_output.draw_instructions()


# Render the geometric sequences screen
def geometric_sequence():
    global answer_drawn, geo_seq_output

    if on_geo_seq_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/geo_seq_formula.png")
        arcade.draw_texture_rectangle(600, 505, 1.1 * formula_1.width, 1.1 * formula_1.height, formula_1)

        intro_geo_seq = Instructions("Calculates a TERM of an arithmetic sequence, given the 1st term, \n" 
                                     "the common ratio, and the number of the term. "
                                     "\n -> The number of term MUST be an integer; \n cannot have a \"2.7th\" "
                                     "term of a sequence.", 300, 600, arcade.color.BLACK, 18, False)

        step_one_geo_seq = Instructions("1. Enter a (first term), r (common ratio), THEN n (term number)", 300,
                                        375, arcade.color.BLACK, 18, True)
        step_two_geo_seq = Instructions("2. INPUT IN ORDER!! a -> r -> n \n Refrain from entering 0 on any of them. "
                                        "\nAlso, refrain from having your answer be 0 as well, somehow",
                                        300, 295, arcade.color.BLACK, 18, True)
        step_three_geo_seq = Instructions("3. Program will output the nth term of your geometric sequence.", 300,
                                         250, arcade.color.BLACK, 18, True)

        if answer_drawn:
            geo_seq_output = Instructions("If the first term of your sequence (a) is " + str(input_variable_1) +
                                          ", with your common \n ratio (r) being " + str(input_variable_2) +
                                          ", the " + str(input_variable_3) + "th term of this sequence is " +
                                          str(result_1) + ".", 200, 100, arcade.color.BLACK, 22, True)

        if not answer_drawn:
            geo_seq_output = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_geo_seq.draw_instructions()
        step_one_geo_seq.draw_instructions()
        step_two_geo_seq.draw_instructions()
        step_three_geo_seq.draw_instructions()
        geo_seq_output.draw_instructions()


# Render the arithmetic series screen
def arithmetic_series():
    global answer_drawn, arith_series_output

    if on_arith_series_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/arith_series_formula.png")
        arcade.draw_texture_rectangle(600, 505, 0.7 * formula_1.width, 0.7 * formula_1.height, formula_1)

        intro_arith_series = Instructions("Calculates a SUM of the nth term of an arithmetic sequence, \ngiven the 1st "
                                          "term, the common difference, and the number of \n terms added."
                                          "\n\n -> The number of terms MUST be an integer; \n cannot add \"1.4\" "
                                          "terms of a sequence.", 300, 600, arcade.color.BLACK, 18, False)

        step_one_arith_series = Instructions("1. Enter a (first term), d (common difference), THEN n (no. of terms)",
                                             300, 375, arcade.color.BLACK, 18, True)
        step_two_arith_series = Instructions("2. INPUT IN ORDER!! a -> d -> n \n Refrain from entering 0. "
                                             "\nAlso, refrain from having your answer be 0 as well, somehow",
                                             300, 295, arcade.color.BLACK, 18, True)
        step_three_arith_series = Instructions("3. Program will output the nth sum of your arithmetic sequence.", 300,
                                              250,arcade.color.BLACK, 18, True)

        if answer_drawn:
            arith_series_output = Instructions("If the first term of your sequence (a) is " + str(input_variable_1) +
                                               ", with your common \ndifference (d) being " + str(input_variable_2) +
                                               ", the " + str(input_variable_3) + "th series (sum) of this sequence is "
                                               + str(result_1) + ".", 200, 100, arcade.color.BLACK, 22, True)

        if not answer_drawn:
            arith_series_output = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_arith_series.draw_instructions()
        step_one_arith_series.draw_instructions()
        step_two_arith_series.draw_instructions()
        step_three_arith_series.draw_instructions()
        arith_series_output.draw_instructions()


# Render the geometric series screen
def geometric_series():
    global answer_drawn, geo_series_output

    if on_geo_series_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/geo_series_formula.png")
        arcade.draw_texture_rectangle(600, 505, 0.75 * formula_1.width, 0.75 * formula_1.height, formula_1)

        intro_geo_series = Instructions("Calculates a SUM of the nth term of an geometric sequence, \ngiven the 1st "
                                        "term, the common ratio, and the number of \n terms added."
                                        "\n\n -> The number of terms MUST be an integer; \n cannot add \"1.4\" "
                                        "terms of a sequence.", 300, 600, arcade.color.BLACK, 18, False)

        step_one_geo_series = Instructions("1. Enter a (first term), r (common ratio), THEN n (no. of terms)",
                                           300, 375, arcade.color.BLACK, 18, True)
        step_two_geo_series = Instructions("2. INPUT IN ORDER!! a -> r -> n \n Refrain from entering 0. "
                                           "\nAlso, refrain from having your answer be 0 as well, somehow",
                                             300, 295, arcade.color.BLACK, 18, True)
        step_three_geo_series = Instructions("3. Program will output the nth sum of your geometric sequence.", 300,
                                             250,arcade.color.BLACK, 18, True)

        if answer_drawn:
            geo_series_output = Instructions("If the first term of your sequence (a) is " + str(input_variable_1) +
                                             ", with your common \nratio (r) being " + str(input_variable_2) +
                                             ", the " + str(input_variable_3) + "th series (sum) of this sequence is "
                                             + str(result_1) + ".", 200, 100, arcade.color.BLACK, 22, True)

        if not answer_drawn:
            geo_series_output = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_geo_series.draw_instructions()
        step_one_geo_series.draw_instructions()
        step_two_geo_series.draw_instructions()
        step_three_geo_series.draw_instructions()
        geo_series_output.draw_instructions()


# Render the financial applications screen.
def money_screen():
    if on_money_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)

        draw_back_button()

        # Draw button that paths to simple interest calculator
        simple_interest_button = arcade.load_texture("buttons/simple_interest_button.png")
        arcade.draw_texture_rectangle(260, 450, 1.2*simple_interest_button.width, 1.2*simple_interest_button.height,
                                      simple_interest_button)
        arcade.draw_text(" - Simple interest calculator; \n given principle, rate and time.",
                         100, 340, arcade.color.BLACK, 20, align="left", font_name='calibri',
                         bold=True)

        # Draw button that paths to compound interest calculator
        compound_interest_button = arcade.load_texture("buttons/compound_interest_button.png")
        arcade.draw_texture_rectangle(725, 450, 1.2*compound_interest_button.width, 1.2*compound_interest_button.height,
                                      compound_interest_button)
        arcade.draw_text(" - Compound interest calculator; \n given principle, rate and time.",
                         550, 340, arcade.color.BLACK, 20, align="left", font_name='calibri',
                         bold=True)

        # Draw button that paths to present value calculator
        present_value_button = arcade.load_texture("buttons/present_value_button.png")
        arcade.draw_texture_rectangle(1185, 450, 1.2*present_value_button.width, 1.2*present_value_button.height,
                                      present_value_button)
        arcade.draw_text(" - Present value calculator; \n given principle, rate and time.",
                         1025, 340, arcade.color.BLACK, 20, align="left", font_name='calibri',
                         bold=True)


# Render the simple interest screen
def simple_interest_screen():
    global answer_drawn, simple_interest_output

    if on_simple_interest_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/simple_interest_formula.png")
        arcade.draw_texture_rectangle(600, 505, formula_1.width, formula_1.height, formula_1)

        intro_simple_interest = Instructions("Calculates SIMPLE INTEREST given the principle, \n"
                                             "the interest rate, and the amount of YEARS passed."
                                             "\n -> The interest rate is also per annum only.", 300, 600,
                                             arcade.color.BLACK, 18, False)

        step_one_simple_interest = Instructions("1. Enter P (principle), r (interest rate per year), "
                                                "\n THEN t (amount of years passed)", 300,
                                                375, arcade.color.BLACK, 18, True)
        step_two_simple_interest = Instructions("2. INPUT IN ORDER!! P -> r -> t \n Refrain from entering 0 on any "
                                                "of them. \nAlso, refrain from having your answer be 0 as well, somehow"
                                                "\n As well, input interest rate in DECIMALS (8% -> 0.08)"
                                                , 300, 250, arcade.color.BLACK, 18, True)
        step_three_simple_interest = Instructions("3. Program will output both TOTAL AMOUNT and interest.", 300,
                                                  200, arcade.color.BLACK, 18, True)

        if answer_drawn:
            simple_interest_output = Instructions("If your principle is " + str(input_variable_1) +
                                                  " dollars, your interest rate " + str(input_variable_2) +
                                                  " \nand it has been " + str(input_variable_3) +
                                                  " years, your amount is " + str(round(result_1, 2)) +
                                                  "; \nyour interest is " + str(round(result_1 - input_variable_1, 2))
                                                  + " dollars.", 200, 75, arcade.color.BLACK, 22, True)

        if not answer_drawn:
            simple_interest_output = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_simple_interest.draw_instructions()
        step_one_simple_interest.draw_instructions()
        step_two_simple_interest.draw_instructions()
        step_three_simple_interest.draw_instructions()
        simple_interest_output.draw_instructions()


# Render the compound interest screen
def compound_interest_screen():
    global answer_drawn, compound_interest_output

    if on_compound_interest_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/compound_interest_formula.png")
        arcade.draw_texture_rectangle(600, 505, 1.3 * formula_1.width, 1.3 * formula_1.height, formula_1)

        intro_compound_interest = Instructions("Calculates COMPOUND INTEREST given the principle, \n"
                                               "the interest rate, and the amount of YEARS passed."
                                               "\n -> The interest rate is also per annum only.", 300, 600,
                                               arcade.color.BLACK, 18, False)

        step_one_compound_interest = Instructions("1. Enter P (principle), r (interest rate per year), "
                                                  "\n THEN t (amount of years passed)", 300,
                                                  375, arcade.color.BLACK, 18, True)
        step_two_compound_interest = Instructions("2. INPUT IN ORDER!! P -> r -> t \n Refrain from entering 0 on any "
                                                  "of them. \nAlso, refrain from having your answer be 0 as well, "
                                                  "somehow \n As well, input interest rate in DECIMALS (8% -> 0.08)"
                                                  , 300, 250, arcade.color.BLACK, 18, True)
        step_three_compound_interest = Instructions("3. Program will output both TOTAL AMOUNT and interest.", 300,
                                                    200, arcade.color.BLACK, 18, True)

        if answer_drawn:
            compound_interest_output = Instructions("If your principle is " + str(input_variable_1) +
                                                    " dollars, your interest rate " + str(input_variable_2) +
                                                    " \n and it has been " + str(input_variable_3) +
                                                    " years, your amount is " + str(round(result_1, 2)) +
                                                    "; \nyour interest is " + str(round(result_1 - input_variable_1, 2))
                                                    + " dollars.", 200, 75, arcade.color.BLACK, 22, True)

        if not answer_drawn:
            compound_interest_output = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_compound_interest.draw_instructions()
        step_one_compound_interest.draw_instructions()
        step_two_compound_interest.draw_instructions()
        step_three_compound_interest.draw_instructions()
        compound_interest_output.draw_instructions()


# Render the present value screen
def present_value_screen():
    global answer_drawn, present_value_output

    if on_present_value_screen:
        background = arcade.load_texture("background/background_math.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        draw_back_button()
        draw_calculator()

        formula_1 = arcade.load_texture("formula/present_value_formula.png")
        arcade.draw_texture_rectangle(600, 505, formula_1.width, formula_1.height, formula_1)

        intro_present_value = Instructions("Calculates the principle needed to fulfill a future amount, \n"
                                           "given the future amount, the rate and years passed."
                                           "\n -> The interest rate is per annum only.", 300, 600,
                                           arcade.color.BLACK, 18, False)

        step_one_present_value = Instructions("1. Enter A (future amount), r (interest rate), "
                                              "\n THEN t (amount of years passed)", 300,
                                              375, arcade.color.BLACK, 18, True)
        step_two_present_value = Instructions("2. INPUT IN ORDER!! A -> r -> t \n Refrain from entering 0 on any "
                                              "of them. \nAlso, refrain from having your answer be 0 as well, somehow"
                                              "\n As well, input interest rate in DECIMALS (8% -> 0.08)", 300, 250,
                                              arcade.color.BLACK, 18, True)
        step_three_present_value = Instructions("3. Program will output the present value or principle.", 300,
                                                200, arcade.color.BLACK, 18, True)

        if answer_drawn:
            present_value_output = Instructions("If your desired future amount is " + str(input_variable_1) +
                                                " dollars, your interest rate " + str(input_variable_2) +
                                                " \nand it will be " + str(input_variable_3) +
                                                " years since, your principle needs to be " + str(round(result_1, 2))
                                                + " dollars.", 200, 70, arcade.color.BLACK, 22, True)

        if not answer_drawn:
            present_value_output = Instructions(" ", 200, 100, arcade.color.BLACK, 22, False)

        intro_present_value.draw_instructions()
        step_one_present_value.draw_instructions()
        step_two_present_value.draw_instructions()
        step_three_present_value.draw_instructions()
        present_value_output.draw_instructions()


# Draw all the above.
def on_draw():
    arcade.start_render()
    title_screen()
    fake_loading()
    topic_selection()
    science_screen()
    bio_screen()
    optics_screen()
    mirror_screen()
    refraction_screen()
    math_screen()
    cast_screen()
    sin_screen()
    cos_screen()
    tan_screen()
    sequences_screen()
    arithmetic_sequence()
    geometric_sequence()
    arithmetic_series()
    geometric_series()
    money_screen()
    simple_interest_screen()
    compound_interest_screen()
    present_value_screen()


def on_key_press(key, modifiers):
    global W_pressed

    if key == arcade.key.W:
        W_pressed = True


def on_key_release(key, modifiers):
    global W_pressed

    if key == arcade.key.W:
        W_pressed = False


# Custom calculator - button input logic. Will be called upon in all future screens and functions, namely in
# on_mouse_press().
def calc_input(x, y):
    global user_input, decimal_placed, input_variable_1, input_variable_2, input_variable_3
    global answer_drawn, negative_placed

    # Unpack button variables into readable data.
    button_one_x, button_one_y, button_one_w, button_one_h = button_one
    button_two_x, button_two_y, button_two_w, button_two_h = button_two
    button_three_x, button_three_y, button_three_w, button_three_h = button_three
    button_four_x, button_four_y, button_four_w, button_four_h = button_four
    button_five_x, button_five_y, button_five_w, button_five_h = button_five
    button_six_x, button_six_y, button_six_w, button_six_h = button_six
    button_seven_x, button_seven_y, button_seven_w, button_seven_h = button_seven
    button_eight_x, button_eight_y, button_eight_w, button_eight_h = button_eight
    button_nine_x, button_nine_y, button_nine_w, button_nine_h = button_nine
    button_zero_x, button_zero_y, button_zero_w, button_zero_h = button_zero
    button_decimal_x, button_decimal_y, button_decimal_w, button_decimal_h = button_decimal
    button_negative_x, button_negative_y, button_negative_w, button_negative_h = button_negative
    button_AC_x, button_AC_y, button_AC_w, button_AC_h = button_AC


    # ADD SCREEN VARIABLES!!!!!!!!!!!!!!!!!!!!!!!
    if on_mirror_screen or on_refraction_screen or on_sin_screen or on_cos_screen or on_tan_screen or \
            on_arith_seq_screen or on_geo_seq_screen or on_arith_series_screen or on_geo_series_screen or \
            on_simple_interest_screen or on_compound_interest_screen or on_present_value_screen:

        # The Mirror + Mag screen requires TWO variables. Take in one if not on that screen. Take two if ON that screen.
        # CAST rules need seven (max) digit characters. Take seven if on those screens.
        # Seq + Series screens need THREE inputs. Take three inputs if on those.
        # Interest screens also need THREE inputs; take three on these screens.
        if (len(user_input) <= 5 and input_variable_1 == 0 and not on_mirror_screen) \
                or (len(user_input) <= 5 and (input_variable_1 == 0 or input_variable_2 == 0) and on_mirror_screen) or \
                (len(user_input) <= 7 and input_variable_1 == 0 and (on_sin_screen or on_cos_screen or on_tan_screen)) \
                or (len(user_input) <= 4 and (input_variable_1 == 0 or input_variable_2 == 0 or input_variable_3 == 0)
                    and (on_arith_seq_screen or on_geo_seq_screen or on_arith_series_screen or on_geo_series_screen)) \
                or (len(user_input) <= 7 and (input_variable_1 == 0 or input_variable_2 == 0 or input_variable_3 == 0)
                    and (on_simple_interest_screen or on_compound_interest_screen or on_present_value_screen)):

            # If button_one has been clicked (on the calculator), add "1" to the user_input string, and so on.
            if button_one_x < x < button_one_x + button_one_w and button_one_y < y < button_one_y + button_one_h \
                    and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "1"

            if button_two_x < x < button_two_x + button_two_w and button_two_y < y < button_two_y + button_two_h \
                    and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "2"

            if button_three_x < x < button_three_x + button_three_w and button_three_y < y < \
                    button_three_y + button_three_h and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "3"

            if button_four_x < x < button_four_x + button_four_w and button_four_y < y < button_four_y + \
                    button_four_h and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "4"

            if button_five_x < x < button_five_x + button_five_w and button_five_y < y < button_five_y + \
                    button_five_h and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "5"

            if button_six_x < x < button_six_x + button_six_w and button_six_y < y < button_six_y + button_six_h \
                    and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "6"

            if button_seven_x < x < button_seven_x + button_seven_w and button_seven_y < y < button_seven_y + \
                    button_seven_h and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "7"

            if button_eight_x < x < button_eight_x + button_eight_w and button_eight_y < y < button_eight_y + \
                    button_eight_h and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "8"

            if button_nine_x < x < button_nine_x + button_nine_w and button_nine_y < y < button_nine_y + button_nine_h \
                    and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "9"

            # Only render in zeros, if the character before it is a decimal (...and user_input[-1] == ".":)
            if button_zero_x < x < button_zero_x + button_zero_w and button_zero_y < y < button_zero_y + button_zero_h \
                    and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "0"

            # Only render in decimals if it hasn't been placed before in the same string (...and not decimal_placed:)
            # Prohibit decimals in sequence and series screens, if asking for NUMBER OF TERMS.
            if button_decimal_x < x < button_decimal_x + button_decimal_w and button_decimal_y < y < button_decimal_y \
                    + button_decimal_h and button_cooldown < 0 and not decimal_placed and user_input != " " and not \
                    ((on_arith_seq_screen or on_arith_series_screen or on_geo_seq_screen or on_geo_series_screen)
                     and (input_variable_1 == 0 or input_variable_2 == 0)):

                arcade.play_sound(select_button_click)
                user_input += "."
                decimal_placed = True  # If it has been placed, prohibit further placement.

            # Only render in negatives if it's the first character; and has not been placed before.
            # As well, prohibit negative placement where not required (aka speed, time, indices, etc.)
            # As well, prohibit them when asking for the number of terms in sequence / series screens.
            # Prohibit negatives in all money-related screens.
            if button_negative_x < x < button_negative_x + button_negative_w and button_negative_y < y < \
                    button_negative_y + button_negative_h and button_cooldown < 0 and not negative_placed \
                    and user_input == " " and not on_refraction_screen and not \
                    ((on_arith_seq_screen or on_arith_series_screen or on_geo_seq_screen or on_geo_series_screen)
                     and (input_variable_1 == 0 or input_variable_2 == 0)) and not \
                    (on_simple_interest_screen or on_compound_interest_screen or on_present_value_screen):

                arcade.play_sound(select_button_click)
                user_input += "-"
                negative_placed = True

            # Automatic decimal placement - refraction. Will always follow the first character.
            if on_refraction_screen and len(user_input) > 1 and user_input[1] != " " and not decimal_placed:
                user_input += "."
                decimal_placed = True

            # Automatic decimal placement - angle ratios. Will always follow a zero.
            if len(user_input) <= 2 and user_input[-1] == "0" and not decimal_placed:
                user_input += "."
                decimal_placed = True

        # Reset button logic.
        if button_AC_x < x < button_AC_x + button_AC_w and button_AC_y < y < button_AC_y + button_AC_h \
                and button_cooldown < 0:
            arcade.play_sound(select_button_click)
            # When "reset" hit, reset the user_input string, and decimal_placed variable.
            user_input = " "
            decimal_placed = False
            negative_placed = False

            # If AC is hit with the calculation already complete, reset all variables.
            if on_mirror_screen:
                if result_1 != 0 and result_2 != 0:
                    reset_all_variables()

            # If AC is hit with the calculation already complete, reset all variables, and so on...
            if on_refraction_screen:
                if result_1 != 0:
                    reset_all_variables()

            if on_sin_screen or on_cos_screen or on_tan_screen:
                if result_1 != 0 and result_2 != 0:
                    reset_all_variables()

            if on_arith_seq_screen or on_arith_series_screen or on_geo_series_screen or on_arith_seq_screen:
                if result_1 != 0:
                    reset_all_variables()

            if on_simple_interest_screen or on_compound_interest_screen or on_present_value_screen:
                if result_1 != 0:
                    reset_all_variables()


# Clicking logic. -----------------------------------------------------------------------------------------------------
def on_mouse_press(x, y, button, modifiers):
    global button_cooldown

    global on_title, on_fake_loading, on_topic_selection, on_science_screen, on_math_screen, on_compsci_screen
    global on_bio_screen, on_optics_screen, on_mirror_screen, on_refraction_screen
    global on_cast_screen, on_sequences_screen, on_money_screen
    global on_sin_screen, on_cos_screen, on_tan_screen
    global on_arith_seq_screen, on_geo_seq_screen, on_arith_series_screen, on_geo_series_screen
    global on_simple_interest_screen, on_compound_interest_screen, on_present_value_screen

    global user_input, decimal_placed, input_variable_1, input_variable_2, input_variable_3, result_1, result_2
    global answer_drawn, negative_placed

    # Buttons coordination; all coordinate sets above are unpacked into a single variable.
    title_button_x, title_button_y, title_button_w, title_button_h = title_button
    back_button_x, back_button_y, back_button_w, back_button_h = back_button
    science_button_x, science_button_y, science_button_w, science_button_h = science_button
    math_button_x, math_button_y, math_button_w, math_button_h = math_button
    compsci_button_x, compsci_button_y, compsci_button_w, compsci_button_h = compsci_button

    bio_button_x, bio_button_y, bio_button_w, bio_button_h = bio_button
    optics_button_x, optics_button_y, optics_button_w, optics_button_h = optics_button
    mirror_button_x, mirror_button_y, mirror_button_w, mirror_button_h = mirror_button
    refraction_button_x, refraction_button_y, refraction_button_w, refraction_button_h = refraction_button

    cast_button_x, cast_button_y, cast_button_w, cast_button_h = cast_button
    sin_button_x, sin_button_y, sin_button_w, sin_button_h = sin_button
    cos_button_x, cos_button_y, cos_button_w, cos_button_h = cos_button
    tan_button_x, tan_button_y, tan_button_w, tan_button_h = tan_button

    seq_series_button_x, seq_series_button_y, seq_series_button_w, seq_series_button_h = seq_series_button
    arith_seq_button_x, arith_seq_button_y, arith_seq_button_w, arith_seq_button_h = arith_seq_button
    geo_seq_button_x, geo_seq_button_y, geo_seq_button_w, geo_seq_button_h = geo_seq_button
    arith_series_button_x, arith_series_button_y, arith_series_button_w, arith_series_button_h = arith_series_button
    geo_series_button_x, geo_series_button_y, geo_series_button_w, geo_series_button_h = geo_series_button

    money_button_x, money_button_y, money_button_w, money_button_h = money_button

    simple_interest_button_x, simple_interest_button_y, simple_interest_button_w, simple_interest_button_h = \
        simple_interest_button

    compound_interest_button_x, compound_interest_button_y, compound_interest_button_w, compound_interest_button_h = \
        compound_interest_button

    present_value_button_x, present_value_button_y, present_value_button_w, present_value_button_h = \
        present_value_button

    button_ENTER_x, button_ENTER_y, button_ENTER_w, button_ENTER_h, = button_ENTER

    # TITLE BUTTON CLICK DETECTION
    if title_button_x < x < title_button_x + title_button_w and title_button_y < y < title_button_y + title_button_h \
            and on_title:
        title_button_click = arcade.load_sound("sounds/title_button_click.wav")
        arcade.play_sound(title_button_click)
        on_title = False
        on_fake_loading = True

    # SCIENCE BUTTON CLICK DETECTION
    if science_button_x - 364/2 < x < (science_button_x - 364/2) + science_button_w and science_button_y - 95/2 \
            < y < (science_button_y - 95/2) + science_button_h and on_topic_selection and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_topic_selection = False
        on_science_screen = True
        button_cooldown = 0.4

    # BIO BUTTON CLICK DETECTION
    if bio_button_x - 408.8 / 2 < x < (bio_button_x - 408.8 / 2) + bio_button_w and bio_button_y - 138.6 / 2 < y < \
            bio_button_y - 138.6 / 2 + bio_button_h and on_science_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_science_screen = False
        on_bio_screen = True
        button_cooldown = 0.4

    # OPTICS BUTTON CLICK DETECTION
    if optics_button_x - 408.8 / 2 < x < (optics_button_x - 408.8 / 2) + optics_button_w and optics_button_y - 138.6 \
            / 2 < y < optics_button_y - 138.6 / 2 + optics_button_h and on_science_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_science_screen = False
        on_optics_screen = True
        button_cooldown = 0.4

    # MIRROR BUTTON CLICK DETECTION
    if mirror_button_x - 596.4/2 < x < (mirror_button_x - 596.4/2) + mirror_button_w and mirror_button_y - 100.8/2 < \
            y < (mirror_button_y - 100.8/2) + mirror_button_h and on_optics_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_optics_screen = False
        on_mirror_screen = True
        button_cooldown = 0.4

    # MIRROR AND MAGNIFICATION CALCULATION - Uses button detection to enter data into user_input. ----------------------
    if on_mirror_screen:
        calc_input(x, y)

        # If ENTER pressed:
        if button_ENTER_x < x < button_ENTER_x + button_ENTER_w and button_ENTER_y < y < button_ENTER_y + \
                button_ENTER_h and button_cooldown < 0:

            # Assigns first input to input_variable_1; as TWO are required in the Mirror / Mag Equations
            # 1/f = 1/do + 1/di
            # m = -di/do

            if input_variable_1 == 0:                 # This variable (in this equation) is "object distance' or do.
                input_variable_1 = float(user_input)        # Converts user_input to float for calculation
                user_input = " "                            # Resets user_input and decimal_placed
                decimal_placed = False
                negative_placed = False

            # If first variable is not zero (aka one user_input has been entered), enter another to the 2nd variable.
            elif input_variable_2 == 0:                     # In this case, this variable is "image distance" or di.
                input_variable_2 = float(user_input)
                user_input = " "
                decimal_placed = False
                negative_placed = False

        # If both needed variables are not empty, proceed calculation.
        if input_variable_1 != 0 and input_variable_2 != 0:
            result_1 = (1/input_variable_2 + 1/input_variable_1) ** -1      # FORMULA for Mirror, shown in line 653.
            result_2 = (input_variable_2 * -1) / input_variable_1        # FORMULA for Magnification, shown in line 654.
            answer_drawn = True              # Variable that determines whether the concluder sentence should be drawn.

    # REFRACTION BUTTON DETECTION
    if refraction_button_x - 596.4 / 2 < x < (refraction_button_x - 596.4 / 2) + refraction_button_w and \
            refraction_button_y - 100.8 / 2 < y < (refraction_button_y - 100.8 / 2) + refraction_button_h and \
            on_optics_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_optics_screen = False
        on_refraction_screen = True
        button_cooldown = 0.4

    # REFRACTION CALCULATION - Uses button detection to enter data into user_input. ------------------------------------
    if on_refraction_screen:
        calc_input(x, y)

        if button_ENTER_x < x < button_ENTER_x + button_ENTER_w and button_ENTER_y < y < button_ENTER_y + \
                button_ENTER_h and button_cooldown < 0:

            # Assigns first and only input to variable_1, which is v. c is given.
            # n = c / v.

            if input_variable_1 == 0:  # This variable is the speed of light in a medium, aka V. C is given.
                input_variable_1 = float(user_input)  # Converts user_input to float for calculation
                user_input = " "  # Resets user_input and decimal_placed
                decimal_placed = False
                negative_placed = False

        # If needed variable is not empty:
        if input_variable_1 != 0:
            result_1 = 3.00 / input_variable_1
            answer_drawn = True

    # MATH BUTTON DETECTION
    if math_button_x - 364/2 < x < (math_button_x - 364/2) + math_button_w and math_button_y - 95/2 < y < \
            (math_button_y - 95/2) + math_button_h and on_topic_selection and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_topic_selection = False
        on_math_screen = True
        button_cooldown = 0/4

    # CAST BUTTON DETECTION
    if cast_button_x - 262 / 2 < x < (cast_button_x - 262 / 2) + cast_button_w and cast_button_y - 61 / 2 < y < \
            (cast_button_y - 61 / 2) + cast_button_h and on_math_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_math_screen = False
        on_cast_screen = True
        button_cooldown = 0.4

    # SIN BUTTON DETECTION
    if sin_button_x - 254/2 < x < (sin_button_x - 254/2) + sin_button_w and sin_button_y - 65/2 < y < sin_button_y - \
            65/2 + sin_button_h and on_cast_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_cast_screen = False
        on_sin_screen = True
        button_cooldown = 0/4

    # COS BUTTON DETECTION
    if cos_button_x - 254/2 < x < (cos_button_x - 254/2) + cos_button_w and cos_button_y - 65/2 < y < cos_button_y - \
            65/2 + cos_button_h and on_cast_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_cast_screen = False
        on_cos_screen = True
        button_cooldown = 0/4

    # TAN BUTTON DETECTION
    if tan_button_x - 254/2 < x < (tan_button_x - 254/2) + tan_button_w and tan_button_y - 65/2 < y < tan_button_y - \
            65/2 + tan_button_h and on_cast_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_cast_screen = False
        on_tan_screen = True
        button_cooldown = 0/4

    # CAST RULE CALCULATION - Uses button detection to enter data into user_input. ------------------------------------
    if on_sin_screen or on_cos_screen or on_tan_screen:
        calc_input(x, y)

        if button_ENTER_x < x < button_ENTER_x + button_ENTER_w and button_ENTER_y < y < button_ENTER_y + \
                button_ENTER_h and button_cooldown < 0:

            if input_variable_1 == 0:  # This variable represents the trigonometric ratio of two angles.
                input_variable_1 = float(user_input)  # Converts user_input to float for calculation
                user_input = " "  # Resets user_input and decimal_placed
                decimal_placed = False
                negative_placed = False

        # If needed variable is not empty:
        if input_variable_1 != 0:
            if input_variable_1 < -1 or input_variable_1 > 1:
                reset_all_variables()

            if 0 < input_variable_1 <= 1:
                if on_sin_screen:
                    result_1 = round(math.degrees(math.asin(input_variable_1)))
                    result_2 = 180 - round(math.degrees(math.asin(input_variable_1)))

                if on_cos_screen:
                    result_1 = round(math.degrees(math.acos(input_variable_1)))
                    result_2 = 360 - round(math.degrees(math.acos(input_variable_1)))

                if on_tan_screen:
                    result_1 = round(math.degrees(math.atan(input_variable_1)))
                    result_2 = 180 + round(math.degrees(math.atan(input_variable_1)))

                answer_drawn = True

            if -1 < input_variable_1 < 0:
                if on_sin_screen:
                    result_1 = 180 + round(math.degrees(math.asin(input_variable_1)))
                    result_2 = 360 - round(math.degrees(math.asin(input_variable_1)))

                if on_cos_screen:
                    result_1 = 180 - round(math.degrees(math.acos(input_variable_1)))
                    result_2 = 180 + round(math.degrees(math.acos(input_variable_1)))

                if on_tan_screen:
                    result_1 = 180 - round(math.degrees(math.atan(input_variable_1)))
                    result_2 = 360 - round(math.degrees(math.atan(input_variable_1)))

                answer_drawn = True

    # SEQUENCES AND SERIES BUTTON DETECTION
    if seq_series_button_x - 262/2 < x < (seq_series_button_x - 262/2) + seq_series_button_w and \
            seq_series_button_y - 61/2 < y < seq_series_button_y - 61/2 + seq_series_button_h and on_math_screen and \
            button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_math_screen = False
        on_sequences_screen = True
        button_cooldown = 0/4

    # ARITHMETIC SEQUENCE BUTTON DETECTION
    if arith_seq_button_x - 418 / 2 < x < (arith_seq_button_x - 418 / 2) + arith_seq_button_w and \
            arith_seq_button_y - 68 / 2 < y < (arith_seq_button_y - 68 / 2) + arith_seq_button_h \
            and on_sequences_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_sequences_screen = False
        on_arith_seq_screen = True
        button_cooldown = 0.4

    # GEOMETRIC SEQUENCE BUTTON DETECTION
    if geo_seq_button_x - 418 / 2 < x < (geo_seq_button_x - 418 / 2) + geo_seq_button_w and \
            geo_seq_button_y - 68 / 2 < y < (geo_seq_button_y - 68 / 2) + geo_seq_button_h \
            and on_sequences_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_sequences_screen = False
        on_geo_seq_screen = True
        button_cooldown = 0.4

    # ARITHMETIC SERIES BUTTON DETECTION
    if arith_series_button_x - 418 / 2 < x < (arith_series_button_x - 418 / 2) + arith_series_button_w and \
            arith_series_button_y - 68 / 2 < y < (arith_series_button_y - 68 / 2) + arith_series_button_h \
            and on_sequences_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_sequences_screen = False
        on_arith_series_screen = True
        button_cooldown = 0.4

    # GEOMETRIC SEQUENCE BUTTON DETECTION
    if geo_series_button_x - 418 / 2 < x < (geo_series_button_x - 418 / 2) + geo_series_button_w and \
            geo_series_button_y - 68 / 2 < y < (geo_series_button_y - 68 / 2) + geo_series_button_h \
            and on_sequences_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_sequences_screen = False
        on_geo_series_screen = True
        button_cooldown = 0.4

    # SEQUENCES AND SERIES CALCULATION - Uses button detection to enter data into user_input. --------------------------
    if on_arith_seq_screen or on_arith_series_screen or on_geo_seq_screen or on_geo_series_screen:
        calc_input(x, y)

        if button_ENTER_x < x < button_ENTER_x + button_ENTER_w and button_ENTER_y < y < button_ENTER_y + \
                button_ENTER_h and button_cooldown < 0:

            if input_variable_1 == 0:  # This variable represents the first term of the sequence.
                input_variable_1 = float(user_input)
                user_input = " "
                decimal_placed = False
                negative_placed = False

            elif input_variable_2 == 0: # This variable represents the common difference or ratio of the sequence.
                input_variable_2 = float(user_input)
                user_input = " "
                decimal_placed = False
                negative_placed = False

            elif input_variable_3 == 0: # This variable represents the number of terms.
                input_variable_3 = int(user_input)
                user_input = " "
                decimal_placed = False
                negative_placed = False

        # If needed variables are not empty:
        if input_variable_1 != 0 and input_variable_2 != 0 and input_variable_3 != 0:
            if on_arith_seq_screen:
                result_1 = input_variable_1 + (input_variable_3 - 1) * input_variable_2
            elif on_geo_seq_screen:
                result_1 = input_variable_1 * input_variable_2 ** (input_variable_3 - 1)
            elif on_arith_series_screen:
                result_1 = (input_variable_3 * (2*input_variable_1 + (input_variable_3-1)*input_variable_2)) / 2
            elif on_geo_series_screen:
                result_1 = (input_variable_1 * (input_variable_2 ** input_variable_3 - 1)) / (input_variable_2 - 1)

            answer_drawn = True

    # FINANCIAL CALCULATORS BUTTON DETECTION
    if money_button_x - 262 / 2 < x < (money_button_x - 262 / 2) + money_button_w and \
            money_button_y - 61 / 2 < y < (money_button_y - 61 / 2) + money_button_h \
            and on_math_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_math_screen = False
        on_money_screen = True
        button_cooldown = 0.4

    # SIMPLE INTEREST BUTTON DETECTION
    if simple_interest_button_x - 262 / 2 < x < (simple_interest_button_x - 262 / 2) + simple_interest_button_w and \
            simple_interest_button_y - 61 / 2 < y < (simple_interest_button_y - 61 / 2) + simple_interest_button_h \
            and on_money_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_money_screen = False
        on_simple_interest_screen = True
        button_cooldown = 0.4

    # COMPOUND INTEREST BUTTON DETECTION
    if compound_interest_button_x - 262 / 2 < x < (compound_interest_button_x - 262 / 2) + compound_interest_button_w \
            and compound_interest_button_y - 61 / 2 < y < (compound_interest_button_y - 61 / 2) + \
            compound_interest_button_h and on_money_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_money_screen = False
        on_compound_interest_screen = True
        button_cooldown = 0.4

    # PRESENT VALUE BUTTON DETECTION
    if present_value_button_x - 262 / 2 < x < (present_value_button_x - 262 / 2) + present_value_button_w and \
            present_value_button_y - 61 / 2 < y < (present_value_button_y - 61 / 2) + present_value_button_h \
            and on_money_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_money_screen = False
        on_present_value_screen = True
        button_cooldown = 0.4

    # FINANCIAL THINGS CALCULATION - Uses button detection to enter data into user_input. ------------------------------
    if on_simple_interest_screen or on_compound_interest_screen or on_present_value_screen:
        calc_input(x, y)

        if button_ENTER_x < x < button_ENTER_x + button_ENTER_w and button_ENTER_y < y < button_ENTER_y + \
                button_ENTER_h and button_cooldown < 0:

            if input_variable_1 == 0:  # For interest screens, this is P. For present value, this is A.
                input_variable_1 = float(user_input)
                user_input = " "
                decimal_placed = False
                negative_placed = False

            elif input_variable_2 == 0: # Represents interest rate PER ANNUM
                input_variable_2 = float(user_input)
                user_input = " "
                decimal_placed = False
                negative_placed = False

            elif input_variable_3 == 0: # Represents time elapsed, in YEARS
                input_variable_3 = int(user_input)
                user_input = " "
                decimal_placed = False
                negative_placed = False

        # If needed variables are not empty:
        if input_variable_1 != 0 and input_variable_2 != 0 and input_variable_3 != 0:
            # A = P + (Prt)
            if on_simple_interest_screen:
                result_1 = input_variable_1 + (input_variable_1 * input_variable_2 * input_variable_3)
            # A = P(1 + r)^t
            elif on_compound_interest_screen:
                result_1 = input_variable_1 * ((1 + input_variable_2) ** input_variable_3)
            # PV = A / (1 + r)^t OR A(1 + r)^-t
            elif on_present_value_screen:
                result_1 = input_variable_1 / ((1 + input_variable_2) ** input_variable_3)

            answer_drawn = True

    # COMPSCI BUTTON DETECTION
    if compsci_button_x - 364/2 < x < (compsci_button_x - 364/2) + compsci_button_w and compsci_button_y - 95/2 \
            < y < (compsci_button_y - 95/2) + compsci_button_h and on_topic_selection:
        arcade.play_sound(select_button_click)
        on_topic_selection = False
        on_compsci_screen = True

    # BACK BUTTON; Science --> Topic
    if back_button_x - 102.4/2 < x < (back_button_x - 102.4/2) + back_button_w and back_button_y - 102.4/2 < y < \
            back_button_y - 120.4/2 + back_button_h and on_science_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_science_screen = False
        on_topic_selection = True
        button_cooldown = 0.4

    # BACK BUTTON; Biology --> Science
    if back_button_x - 102.4/2 < x < (back_button_x - 102.4/2) + back_button_w and back_button_y - 102.4/2 < y < \
            back_button_y - 120.4/2 + back_button_h and on_bio_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_bio_screen = False
        on_science_screen = True
        button_cooldown = 0.4

    # BACK BUTTON; Optics --> Science
    if back_button_x - 102.4/2 < x < (back_button_x - 102.4/2) + back_button_w and back_button_y - 102.4/2 < y < \
            back_button_y - 120.4/2 + back_button_h and on_optics_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_optics_screen = False
        on_science_screen = True
        button_cooldown = 0.4

    # BACK BUTTON; Mirror --> Optics
    if back_button_x - 102.4/2 < x < (back_button_x - 102.4/2) + back_button_w and back_button_y - 102.4/2 < y < \
            back_button_y - 120.4/2 + back_button_h and on_mirror_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_mirror_screen = False
        on_optics_screen = True
        button_cooldown = 0.4

        reset_all_variables()

    # BACK BUTTON; Refraction --> Optics
    if back_button_x - 102.4 / 2 < x < (
            back_button_x - 102.4 / 2) + back_button_w and back_button_y - 102.4 / 2 < y < \
            back_button_y - 120.4 / 2 + back_button_h and on_refraction_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_refraction_screen = False
        on_optics_screen = True
        button_cooldown = 0.4

        reset_all_variables()

    # BACK BUTTON; Math --> Topic
    if back_button_x - 102.4/2 < x < (back_button_x - 102.4/2) + back_button_w and back_button_y - 102.4/2 < y < \
            back_button_y - 120.4/2 + back_button_h and on_math_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_math_screen = False
        on_topic_selection = True
        button_cooldown = 0.4

    # BACK BUTTON; CAST --> Math
    if back_button_x - 102.4/2 < x < (back_button_x - 102.4/2) + back_button_w and back_button_y - 102.4/2 < y < \
            back_button_y - 120.4/2 + back_button_h and on_cast_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_cast_screen = False
        on_math_screen = True
        button_cooldown = 0.4

    # BACK BUTTON; Sequences Selection Screen --> Math
    if back_button_x - 102.4 / 2 < x < (back_button_x - 102.4 / 2) + back_button_w and back_button_y - 102.4 / 2 < y < \
            back_button_y - 120.4 / 2 + back_button_h and on_sequences_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_sequences_screen = False
        on_math_screen = True
        button_cooldown = 0.4

    # BACK BUTTON; Money Selection Screen --> Math
    if back_button_x - 102.4/2 < x < (back_button_x - 102.4/2) + back_button_w and back_button_y - 102.4/2 < y < \
            back_button_y - 120.4/2 + back_button_h and on_money_screen and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_money_screen = False
        on_math_screen = True
        button_cooldown = 0.4

    # BACK BUTTON; any angle ratio --> CAST
    if back_button_x - 102.4 / 2 < x < (back_button_x - 102.4 / 2) + back_button_w and back_button_y - 102.4 / 2 < y < \
            back_button_y - 120.4 / 2 + back_button_h and (on_sin_screen or on_cos_screen or on_tan_screen) \
            and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_sin_screen = False
        on_cos_screen = False
        on_tan_screen = False
        on_cast_screen = True
        button_cooldown = 0.4

        reset_all_variables()

    # BACK BUTTON; any sequences or series --> Sequence Selection Screen
    if back_button_x - 102.4 / 2 < x < (back_button_x - 102.4 / 2) + back_button_w and back_button_y - 102.4 / 2 < y < \
            back_button_y - 120.4 / 2 + back_button_h and (on_arith_seq_screen or on_geo_seq_screen
                                                           or on_arith_series_screen or on_geo_series_screen) \
            and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_arith_seq_screen = False
        on_geo_seq_screen = False
        on_arith_series_screen = False
        on_geo_series_screen = False
        on_sequences_screen = True
        button_cooldown = 0.4

        reset_all_variables()

    # BACK BUTTON; any money calculators --> Money Selection Screen
    if back_button_x - 102.4 / 2 < x < (back_button_x - 102.4 / 2) + back_button_w and back_button_y - 102.4 / 2 < y < \
            back_button_y - 120.4 / 2 + back_button_h and (on_simple_interest_screen or on_compound_interest_screen or
                                                           on_present_value_screen) and button_cooldown < 0:
        arcade.play_sound(back_button_click)
        on_simple_interest_screen = False
        on_compound_interest_screen = False
        on_present_value_screen = False
        on_money_screen = True
        button_cooldown = 0.4

        reset_all_variables()


# Setup the thing
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
