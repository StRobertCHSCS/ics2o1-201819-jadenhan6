import arcade

WIDTH = 800
HEIGHT = 600

# x and y positions of the snow person
snow_person_x1 = 150
snow_delta_x1 = 3
snow_person_y1 = 50
snow_delta_y1 = 1

snow_person_x2 = 220
snow_delta_x2 = 5
snow_person_y2 = 140
snow_delta_y2 = 3

snow_player_x = 300
snow_player_y = 50

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, WIDTH, HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person_1(x, y):
    global snow_person_x1, snow_person_y1, snow_delta_y1, snow_delta_x1

    """
    # Draw a point at x, y for reference
    arcade.draw_point(snow_person_x1, snow_person_y1, arcade.color.RED, 5)
    """

    # Snow
    arcade.draw_circle_filled(x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 340 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(-15 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(15 + x, 350 + y, 5, arcade.color.BLACK)


def draw_snow_person_2(x, y):
    global snow_person_x2, snow_person_y2, snow_delta_y2, snow_delta_x2

    """
    # Draw a point at x, y for reference
    arcade.draw_point(snow_person_x1, snow_person_y1, arcade.color.RED, 5)
    """

    # Snow
    arcade.draw_circle_filled(x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 340 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(-15 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(15 + x, 350 + y, 5, arcade.color.BLACK)

    # Nose
    arcade.draw_triangle_filled(x, 330 + y, -5 + x, 345 + y, 5 + x, 345 + y, arcade.color.DARK_YELLOW)


def draw_player(x, y):
    global snow_player_x, snow_player_y
    # Snow
    arcade.draw_circle_filled(x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 340 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(-15 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(15 + x, 350 + y, 5, arcade.color.BLACK)

    # Nose
    arcade.draw_triangle_filled(x, 330 + y, -5 + x, 345 + y, 5 + x, 345 + y, arcade.color.ORANGE)


def on_update(delta_time):
    global snow_person_x1, snow_delta_x1, snow_person_y1, snow_delta_y1, snow_person_x2, snow_delta_x2, snow_person_y2,\
        snow_delta_y2, snow_player_x, snow_player_y, up_pressed, down_pressed, left_pressed, right_pressed

    # update position of snow person which each pass of the event loop
    snow_person_x1 += snow_delta_x1
    snow_person_y1 += snow_delta_y1
    snow_person_x2 += snow_delta_x2
    snow_person_y2 += snow_delta_y2

    # boundary check
    if snow_person_x1 < 60 or snow_person_x1 > WIDTH - 60:
        snow_delta_x1 *= -1
    if snow_person_y1 > HEIGHT - 380 or snow_person_y1 < 50:
        snow_delta_y1 *= -1
    if snow_person_x2 < 60 or snow_person_x2 > WIDTH - 60:
        snow_delta_x2 *= -1
    if snow_person_y2 > HEIGHT - 380 or snow_person_y2 < 50:
        snow_delta_y2 *= -1

    # player boundary check
    if up_pressed and snow_player_y < HEIGHT - 380:
        snow_player_y += 7
    if down_pressed and snow_player_y > 50:
        snow_player_y -= 7
    if left_pressed and snow_player_x > 60:
        snow_player_x -= 7
    if right_pressed and snow_player_x < WIDTH - 60:
        snow_player_x += 7


def on_draw():
    arcade.start_render()
    draw_grass()
    draw_snow_person_1(snow_person_x1, snow_person_y1)
    draw_snow_person_2(snow_person_x2, snow_person_y2)
    draw_player(snow_player_x, snow_player_y)


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.W:
        up_pressed = True
    if key == arcade.key.S:
        down_pressed = True
    if key == arcade.key.A:
        left_pressed = True
    if key == arcade.key.D:
        right_pressed = True


def on_key_release(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.W:
        up_pressed = False
    if key == arcade.key.S:
        down_pressed = False
    if key == arcade.key.A:
        left_pressed = False
    if key == arcade.key.D:
        right_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
