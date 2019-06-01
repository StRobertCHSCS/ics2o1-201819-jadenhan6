# Import necessary modules.
import arcade
import random
import math

# Set screen dimensions
WIDTH = 1450
HEIGHT = 795

# cheat variable
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

# Selection screen variables
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
button_AC = [1200, 575, 75, 75]
button_ENTER = [1200, 175, 75, 75]

# Determines if decimal, in any calculator (of any function in program), has been placed.
decimal_placed = False

# Variables for calculation.
object_distance = 0
image_distance = 0
focal_length = 0


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


# Render a Shape class 35 times.
for i in range(35):
    # randomizer; picks color, size, type, opacity and movement speeds at random.
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

    # uploads newly created shape to the shapes_list specificed above.
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

# Sets a variable that determines what splash text will be shown upon launch.
# Go to fake_screen() function for application of this variable.
display_text = random.randint(1, 8)


# FUNCTIONS -----------------------------------------------------------------------------------------------------------

# Animation, timer, cooldown functions, etc.
def on_update(delta_time):
    global loading_counter, on_fake_loading, on_topic_selection, character_counter
    global show_character_left, show_character_right, transition_alpha
    global button_cooldown, on_science_screen, on_title

    # Fake loading screen updates
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
    if on_topic_selection:
        button_cooldown -= delta_time
    if on_science_screen:
        button_cooldown -= delta_time
    if on_bio_screen:
        button_cooldown -= delta_time
    if on_optics_screen:
        button_cooldown -= delta_time
    if on_mirror_screen:
        button_cooldown -= delta_time
    if on_refraction_screen:
        button_cooldown -= delta_time

    if W_pressed:
        on_title = False
        on_science_screen = True


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
            Shape.draw_shape()
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

        # Render the back button.
        back_button = arcade.load_texture("buttons/back_button.png")
        arcade.draw_texture_rectangle(100, 725, 0.4*back_button.width, 0.4*back_button.height, back_button)

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
        print(user_input)


# Render the optics screen.
def optics_screen():
    if on_optics_screen:
        background = arcade.load_texture("background/background_optics.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1.7*background.width, 1.7*background.height, background)

        back_button = arcade.load_texture("buttons/back_button.png")                # Draw back button
        arcade.draw_texture_rectangle(100, 725, 0.4 * back_button.width, 0.4 * back_button.height, back_button)

        # Draw button that paths to Mirror and Magnification
        mirror_button = arcade.load_texture("buttons/mirror_button.png")
        arcade.draw_texture_rectangle(350, 450, 1.4*mirror_button.width, 1.4*mirror_button.height, mirror_button)

        # Draw button that paths to Indices of Refraction
        refraction_button = arcade.load_texture("buttons/refraction_button.png")
        arcade.draw_texture_rectangle(1050, 450, 1.4*refraction_button.width, 1.4*refraction_button.height,
                                      refraction_button)


# Render the mirror and magnification screen.
def mirror_screen():
    if on_mirror_screen:
        background = arcade.load_texture("background/background_optics.png")
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.7 * background.width, 1.7 * background.height,
                                      background)

        back_button = arcade.load_texture("buttons/back_button.png")
        arcade.draw_texture_rectangle(100, 725, 0.4 * back_button.width, 0.4 * back_button.height, back_button)

        # Draw calculator background.
        arcade.draw_xywh_rectangle_filled(950, 150, 375, 625, arcade.color.GRAY)
        arcade.draw_xywh_rectangle_outline(950, 150, 375, 625, arcade.color.BLACK, 3)
        arcade.draw_xywh_rectangle_filled(1000, 670, 275, 90, arcade.color.WHITE)
        arcade.draw_xywh_rectangle_outline(1000, 670, 275, 90, arcade.color.BLACK, 3)
        arcade.draw_text(user_input, 1130, 705, arcade.color.BLACK, 22)       # Displays user_input variable to screen.

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

        # Button "ENTER"
        arcade.draw_xywh_rectangle_filled(1200, 175, 75, 75, arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(1200, 175, 75, 75, arcade.color.WHITE, 2)
        arcade.draw_text("ENTER", 1215, 205, arcade.color.WHITE, 14, bold=True)

        # Button "AC"
        arcade.draw_xywh_rectangle_filled(1200, 575, 75, 75, arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(1200, 575, 75, 75, arcade.color.WHITE, 2)
        arcade.draw_text("AC", 1217.5, 603, arcade.color.WHITE, 22, bold=True)


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


def on_key_press(key, modifiers):
    global W_pressed

    if key == arcade.key.W:
        W_pressed = True



def on_key_release(key, modifiers):
    global W_pressed

    if key == arcade.key.W:
        W_pressed = False

# Clicking logic.
def on_mouse_press(x, y, button, modifiers):
    global on_title, on_fake_loading, on_topic_selection, on_science_screen, on_math_screen, on_compsci_screen
    global on_bio_screen, on_optics_screen, on_mirror_screen, on_refraction_screen, button_cooldown
    global user_input, decimal_placed, object_distance, image_distance, focal_length

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

    # UNIVERSAL CALCULATOR BUTTON LOGIC
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
    button_ENTER_x, button_ENTER_y, button_ENTER_w, button_ENTER_h, = button_ENTER
    button_AC_x, button_AC_y, button_AC_w, button_AC_h = button_AC

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



    # MIRROR AND MAGNIFICATION CALCULATION - Uses button detection to enter data into user_input.
    if on_mirror_screen:
        # If length of string is less than 5 characters, with until both needed variables are NOT zeros...
        if len(user_input) <= 5 and (object_distance == 0 or image_distance == 0):
            # If button_one has been clicked (on the calculator), add "1" to the user_input string, and so on.
            if button_one_x < x < button_one_x + button_one_w and button_one_y < y < button_one_y + button_one_h and \
                    on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "1"

            if button_two_x < x < button_two_x + button_two_w and button_two_y < y < button_two_y + button_two_h and \
                    on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "2"

            if button_three_x < x < button_three_x + button_three_w and button_three_y < y < \
                    button_three_y + button_three_h and on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "3"

            if button_four_x < x < button_four_x + button_four_w and button_four_y < y < button_four_y + \
                    button_four_h and on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "4"

            if button_five_x < x < button_five_x + button_five_w and button_five_y < y < button_five_y + \
                    button_five_h and on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "5"

            if button_six_x < x < button_six_x + button_six_w and button_six_y < y < button_six_y + button_six_h and \
                    on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "6"

            if button_seven_x < x < button_seven_x + button_seven_w and button_seven_y < y < button_seven_y + \
                    button_seven_h and on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "7"

            if button_eight_x < x < button_eight_x + button_eight_w and button_eight_y < y < button_eight_y + \
                    button_eight_h and on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "8"

            if button_nine_x < x < button_nine_x + button_nine_w and button_nine_y < y < button_nine_y + button_nine_h \
                    and on_mirror_screen and button_cooldown < 0:
                arcade.play_sound(select_button_click)
                user_input += "9"

            # Only render in zeros, if the character before it is a decimal (...and user_input[-1] == ".":)
            if button_zero_x < x < button_zero_x + button_zero_w and button_zero_y < y < button_zero_y + button_zero_h \
                    and on_mirror_screen and button_cooldown < 0 and user_input[-1] == ".":
                arcade.play_sound(select_button_click)
                user_input += "0"

            # Only render in decimals if it hasn't been placed before in the same string (...and not decimal_placed:)
            if button_decimal_x < x < button_decimal_x + button_decimal_w and button_decimal_y < y < button_decimal_y \
                    + button_decimal_h and on_mirror_screen and button_cooldown < 0 and not decimal_placed:
                arcade.play_sound(select_button_click)
                user_input += "."
                decimal_placed = True       # If it has been placed, prohibit further placement.

        if button_AC_x < x < button_AC_x + button_AC_w and button_AC_y < y < button_AC_y + button_AC_h and \
                on_mirror_screen and button_cooldown < 0:
            arcade.play_sound(select_button_click)
            # When "reset" hit, reset the user_input string, and decimal_placed variable.
            user_input = " "
            decimal_placed = False

        if button_ENTER_x < x < button_ENTER_x + button_ENTER_w and button_ENTER_y < y < button_ENTER_y + \
                button_ENTER_h and on_mirror_screen and button_cooldown < 0:

            # Assigns first input to object_distance, which is one of the variables needed in the Mirror Equation
            # 1/f = 1/do + 1/di
            if object_distance == 0:
                object_distance = float(user_input)         # Converts user_input to float for calculation
                user_input = " "                            # Resets user_input and decimal_placed
                decimal_placed = False

            # If object_distance is not zero (aka one user_input has been entered), enter another to the 2nd variable.
            elif image_distance == 0:
                image_distance = float(user_input)
                user_input = " "
                decimal_placed = False

    # If both needed variables are not empty:
    if object_distance != 0 and image_distance != 0:
        print("Calculating focal length...")
        focal_length = (1/image_distance + 1/object_distance) ** -1     # FORMULA for Mirror, shown in line 633.
        print("The focal length is about", round(focal_length, 2))      # Round final answer.

        object_distance = 0                                             # Reset all variables.
        image_distance = 0
        user_input = " "
        decimal_placed = False


    # REFRACTION BUTTON DETECTION
    if refraction_button_x - 596.4/2 < x < (refraction_button_x - 596.4/2) + refraction_button_w and \
            refraction_button_y - 100.8/2 < y < (refraction_button_y - 100.8/2) + refraction_button_h and \
            on_optics_screen and button_cooldown < 0:
        arcade.play_sound(select_button_click)
        on_optics_screen = False
        on_refraction_screen = True
        button_cooldown = 0.4

    # MATH BUTTON DETECTION
    if math_button_x - 364/2 < x < (math_button_x - 364/2) + math_button_w and math_button_y - 95/2 < y < \
            (math_button_y - 95/2) + math_button_h and on_topic_selection:
        arcade.play_sound(select_button_click)
        on_topic_selection = False
        on_math_screen = True

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
        user_input = " "                # As user is exiting out of a calculator environment, reset all variables.
        decimal_placed = False


# Setup the monstrosity
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
