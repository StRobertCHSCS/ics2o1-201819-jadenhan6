import arcade


# Set constants for screen height and width
WIDTH = 1080
HEIGHT = 785

# Define text and underline heights, then delta (change) rates.
text_height = 1000
delta_y_text = 9
underline_height = 990
delta_y_underline = 9

# Button animation variables
move_button_1 = False       # initiates button 1's movement sequence
button_1_moved = False      # variable that checks if button 1 has been moved.
delta_x_button_1 = 0        # change in the x-value of button 1.

move_button_2 = False
button_2_moved = False
delta_x_button_2 = 0

move_button_3 = False
button_3_moved = False
delta_x_button_3 = 0

button_1 = [780, 490, 290, 50]
button_2 = [780, 430, 290, 50]
button_3 = [780, 370, 290, 50]


def on_update(delta_time):
    global text_height, delta_y_text, underline_height, delta_y_underline, delta_x_button_1, button_1_moved,\
        delta_x_button_2, button_2_moved, delta_x_button_3, button_3_moved

    # Animate title and underline; move down until in view; 9 pixels down per on_update recall aka every 1/60 seconds
    text_height -= delta_y_text
    underline_height -= delta_y_underline

    # Stop movement when desired height reached
    if text_height < 720:
        delta_y_text = 0
    if underline_height < 710:
        delta_y_underline = 0

    # Button 1; if movement sequence initiated and the button hasn't already
    # been moved, move button 1 right by 1000 pixels; hence out of view.
    if move_button_1 and not button_1_moved:
        delta_x_button_1 = 1000
        button_1[0] += delta_x_button_1

        # checks if button has been moved; so when the area where the button used to be is clicked,
        # no movement occurs.
        button_1_moved = True

    if move_button_2 and not button_2_moved:
        delta_x_button_2 = 1000
        button_2[0] += delta_x_button_2
        button_2_moved = True

    if move_button_3 and not button_3_moved:
        delta_x_button_3 = 1000
        button_3[0] += delta_x_button_3
        button_3_moved = True


# Use a sprite / gradient texture as the background
def make_background():
    background = arcade.load_texture("textures/background.jpg")
    arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, background.width, background.height, background)


# Draw title, underline, accompanying images
def draw_title_things():
    # Draw title
    arcade.draw_text("Ransomware and Prevention Techniques", 240, text_height, arcade.color.DARK_BLUE, 30, 0,
                     "center", 'ARIAL', True)

    # Draw underline
    arcade.draw_line(230, underline_height, 890, underline_height, arcade.color.DARK_BLUE, 3)

    # Load texture_1 -- computer screen
    texture_1 = arcade.load_texture("textures/computer_1.png")
    scale = 0.055
    arcade.draw_texture_rectangle(150, text_height, scale * texture_1.width, scale * texture_1.height,
                                  texture_1)

    # Load texture_2 -- ransomware clipart
    texture_2 = arcade.load_texture("textures/malware_1.png")
    scale = 0.16
    arcade.draw_texture_rectangle(950, text_height, scale * texture_2.width, scale * texture_2.height,
                                  texture_2)


# Draw "What is a ransomware" with WannaCry sample image
def draw_ransomware_intro():
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
    arcade.draw_line(12, 580, 290, 580, arcade.color.DARK_BLUE, 3)

    # BULLET POINT AND TEXT 1
    arcade.draw_circle_filled(25, 515, 5, arcade.color.DARK_BLUE)
    arcade.draw_text("A malware that forcefully encrypts data, \nand demands ransom to \"save\" malware-led",
                     35, 505, arcade.color.BLACK, 14, 0)
    arcade.draw_text("data destruction.", 35, 487, arcade.color.DARK_RED, 14)

    # BULLET POINT AND TEXT 2
    arcade.draw_circle_filled(25, 455, 5, arcade.color.DARK_BLUE)
    arcade.draw_text("If ransom isn't paid, the data is destroyed. \nNo guarantee of decryption either.",
                     35, 440, arcade.color.BLACK, 14)

    # BULLET POINT AND TEXT 3
    arcade.draw_circle_filled(25, 420, 5, arcade.color.DARK_BLUE)
    arcade.draw_text("e.g. WannaCry, CryptoLocker, etc.", 35, 415, arcade.color.RED, 14)

    # EXAMPLE IMAGE
    ransomware_image = arcade.load_texture("textures/ransomware_image.png")
    arcade.draw_texture_rectangle(530, 525, 0.55*ransomware_image.width, 0.55*ransomware_image.height,
                                  ransomware_image)


# Draw mouse-interactive parts, with header and text
def draw_facts_and_stats():
    # TOP LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(730, 650, 1080, 650, arcade.color.DARK_GREEN, 4)
    # BOTTOM LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(780, 550, 1080, 550, arcade.color.DARK_GREEN, 4)
    # CONNECTOR LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(730, 650, 780, 550, arcade.color.DARK_GREEN, 4)

    # FILL the lines; rectangle
    arcade.draw_xywh_rectangle_filled(780, 550, 300, 100, arcade.color.LIGHT_GREEN)
    # FILL the lines; triangle
    arcade.draw_triangle_filled(730, 650, 780, 650, 780, 550, arcade.color.LIGHT_GREEN)

    # Header: "Ransomware - Stats and Facts"
    arcade.draw_text("Ransomware Stats and Facts", 770, 590, arcade.color.DARK_GREEN, 20, 0,
                     "center", 'ARIAL', True)
    arcade.draw_line(775, 580, 1075, 580, arcade.color.DARK_GREEN, 3)

    # FACT 1, revealed by BUTTON 1 movement:
    arcade.draw_text("Ransomware attacks have almost \n                   in the last two years!", 800, 495,
                     arcade.color.BLACK, 15, align="left", bold=True)
    arcade.draw_text("doubled", 805, 495, arcade.color.DARK_RED, 15, align="center", bold=True)

    # FACT 2, revealed by BUTTON 2 movement:
    arcade.draw_text("Damage in finances due to ransomware \n attacks is set to hit             "
                     "        in 2021.", 780, 440, arcade.color.BLACK, 14, align="left", bold=True)
    arcade.draw_text("$6 trillion", 920, 440, arcade.color.DARK_RED, 14, align="center", bold=True)

    # FACT 3, revealed by BUTTON 3 movement:
    arcade.draw_text("77% of Canadian victims paid the ransom. \n Little to no cases had data actually decrypted.",
                     780, 390, arcade.color.BLACK, 12, align="left", bold=True)


def draw_buttons():
    # Button 1 clickable area
    arcade.draw_xywh_rectangle_filled(button_1[0], button_1[1], button_1[2], button_1[3], arcade.color.GRAY)

    # Button 1 outlines and text; top, bottom, left, right.
    arcade.draw_line(button_1[0], 540, button_1[0] + 290, 540, arcade.color.BLACK, 2)
    arcade.draw_line(button_1[0], 490, button_1[0] + 290, 490, arcade.color.BLACK, 2)
    arcade.draw_line(button_1[0], 540, button_1[0], 490, arcade.color.BLACK, 2)
    arcade.draw_line(button_1[0] + 290, 540, button_1[0] + 290, 490, arcade.color.BLACK, 2)
    arcade.draw_text("Click to reveal...", button_1[0] + 70, 505, arcade.color.BLACK, 20, bold=True)

    # Button 2 clickable area
    arcade.draw_xywh_rectangle_filled(button_2[0], button_2[1], button_2[2], button_2[3], arcade.color.GRAY)

    # Button 2 outlines and text
    arcade.draw_line(button_2[0], 480, button_2[0] + 290, 480, arcade.color.BLACK, 2)
    arcade.draw_line(button_2[0], 430, button_2[0] + 290, 430, arcade.color.BLACK, 2)
    arcade.draw_line(button_2[0], 480, button_2[0], 430, arcade.color.BLACK, 2)
    arcade.draw_line(button_2[0] + 290, 480, button_2[0] + 290, 430, arcade.color.BLACK, 2)
    arcade.draw_text("Click to reveal...", button_2[0] + 70, 445, arcade.color.BLACK, 20, bold=True)

    # Button 3 clickable area
    arcade.draw_xywh_rectangle_filled(button_3[0], button_3[1], button_3[2], button_3[3], arcade.color.GRAY)

    # Button 3 outlines and text
    arcade.draw_line(button_3[0], 420, button_3[0] + 290, 420, arcade.color.BLACK, 2)
    arcade.draw_line(button_3[0], 370, button_3[0] + 290, 370, arcade.color.BLACK, 2)
    arcade.draw_line(button_3[0], 420, button_3[0], 370, arcade.color.BLACK, 2)
    arcade.draw_line(button_3[0] + 290, 420, button_3[0] + 290, 370, arcade.color.BLACK, 2)
    arcade.draw_text("Click to reveal...", button_3[0] + 70, 385, arcade.color.BLACK, 20, bold=True)


def ransomware_sources():
    # TOP LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(0, 375, 350, 375, arcade.color.DARK_RED, 4)
    # BOTTOM LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(0, 275, 300, 275, arcade.color.DARK_RED, 4)
    # CONNECTOR LINE: start_x, start_y, end_x, end_y
    arcade.draw_line(350, 375, 300, 275, arcade.color.DARK_RED, 4)

    # FILL the lines; rectangle
    arcade.draw_xywh_rectangle_filled(0, 275, 300, 100, arcade.color.LIGHT_RED_OCHRE)
    # FILL the lines; triangle
    arcade.draw_triangle_filled(350, 375, 300, 375, 300, 275, arcade.color.LIGHT_RED_OCHRE)

    # Header: "Ransomware - Stats and Facts"
    arcade.draw_text("Sources of Ransomware", 20, 315, arcade.color.DARK_RED, 22, 0,
                     "center", 'ARIAL', True)
    arcade.draw_line(20, 310, 295, 310, arcade.color.DARK_RED, 3)

    # BULLET POINT AND TEXT 1
    arcade.draw_circle_filled(25, 250, 5, arcade.color.DARK_RED)
    arcade.draw_text("Fake e-mails that look legit. Harbours \n an .exe file that will         "
                     "     the device if run.", 35, 230, arcade.color.BLACK, 14)
    arcade.draw_text("infect", 180, 230, arcade.color.DARK_RED, 14)

    # BULLET POINT AND TEXT 2
    arcade.draw_circle_filled(25, 195, 5, arcade.color.DARK_RED)
    arcade.draw_text("Computer vulnerabilites; older software \n is subject to a                "
                     "                of infecton.", 35, 185, arcade.color.BLACK, 14)
    arcade.draw_text("higher chance", 145, 185, arcade.color.DARK_RED, 14)

    # BULLET POINT AND TEXT 3
    arcade.draw_circle_filled(25, 145, 5, arcade.color.DARK_RED)
    arcade.draw_text("Lack of               "
                     "        ; cannot detect malware \n when they do infect the device.", 35, 135,
                     arcade.color.BLACK, 14)
    arcade.draw_text("antiviruses", 90, 154, arcade.color.DARK_RED, 14)

    # IMAGE AT BOTTOM
    malware_2 = arcade.load_texture("textures/malware_2.png")
    arcade.draw_texture_rectangle(150, 70, 0.25*malware_2.width, 0.25*malware_2.height, malware_2)


def on_draw():
    arcade.start_render()
    make_background()
    draw_title_things()
    draw_ransomware_intro()
    draw_facts_and_stats()
    draw_buttons()
    ransomware_sources()


def on_mouse_press(x, y, button, modifiers):
    global move_button_1, move_button_2, move_button_3

    # Buttons coordination and detection
    button_1x, button_1y, button_1w, button_1h = button_1
    button_2x, button_2y, button_2w, button_2h = button_2
    button_3x, button_3y, button_3w, button_3h = button_3

    # If button 1 has been clicked, and it hasn't already been clicked before, initiate button 1's moving sequence
    if (button_1w < x < button_1x + button_1w and button_1y < y < button_1y + button_1h) and not button_1_moved:
        move_button_1 = True

    # Same logic with buttons 2 and 3.
    if (button_2w < x < button_2x + button_2w and button_2y < y < button_2y + button_2h) and not button_2_moved:
        move_button_2 = True

    if (button_3w < x < button_3x + button_3w and button_3y < y < button_3y + button_3h) and not button_3_moved:
        move_button_3 = True


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Computers and Society Poster")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
