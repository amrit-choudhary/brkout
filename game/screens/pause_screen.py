from __future__ import absolute_import
from __future__ import division
import os
import pygame

# function to set path to current folder (py 2 to 3)
from past.utils import old_div


def import_modify():
    if __name__ == '__main__':
        if __package__ is None:
            import sys
            from os import path
            sys.path.append(path.abspath(
                path.join(path.dirname(__file__), '..')))


try:
    from game.global_objects import *
    from game.objects.ball import Ball
    from game.misc import *
except SystemError:
    from .global_objects import *
    from .objects.ball import Ball
    from .misc import *


def pause_game(game_manager):
    pygame = game_manager.pygame
    screen = game_manager.screen
    clock = game_manager.clock
    sound_manager = game_manager.sound_manager

    sound_manager.play_sound(pause_sound)

    oldtime = pygame.time.get_ticks()
    pause_ball = Ball(130, 140)  # Initializing pause_ball
    pause_option = E_Pause_Option.resume

    box_collider = Rect_Collider(
        scr_width // 2, scr_height // 2 + 20, 356, 376)

    wall_colliders = [
        Rect_Collider(scr_width // 2, -20, 2000, 100),                   # top
        Rect_Collider(scr_width + 20, scr_height, 100, 2000),           # right
        Rect_Collider(scr_width // 2, scr_height + \
                      20, 2000, 100),      # bottom
        Rect_Collider(-20, scr_height // 2, 100, 2000)]                  # left

    # Giving a delay of 200 ms
    while pygame.time.get_ticks() - oldtime < 100:
        pass

    oldtime = pygame.time.get_ticks()
    while True:

        newtime = pygame.time.get_ticks()
        delta_time = old_div((newtime - oldtime), 10)
        oldtime = newtime

        events = pygame.event.get()

        # checking events
        for event in events:
            if event.type == pygame.QUIT:
                os._exit(0)

        game_manager.input_manager.update(events)
        input = game_manager.input_manager

        if input.get_button('escape'):
            sound_manager.stop_sound(pause_sound)
            return E_Pause_Option.resume
            pass

        if input.get_button('up'):
            pause_option = decrease_enum(pause_option)

        if input.get_button('down'):
            pause_option = increase_enum(pause_option)

        if input.get_button('enter'):
            sound_manager.stop_sound(pause_sound)
            if pause_option == E_Pause_Option.quit:
                os._exit(0)
            else:
                return pause_option

        # ball updation
        pause_ball.menu_screen_move(delta_time)

        collision_result = Collision.check_circle_rects(
            pause_ball.get_collider(), wall_colliders)

        if collision_result != (0, 0):
            pause_ball.bounce(collision_result, delta_time)

        collision_result = Collision.check(
            pause_ball.get_collider(), box_collider)

        if collision_result != (0, 0):
            pause_ball.bounce(collision_result, delta_time)

        # display update
        screen.fill(black)
        draw_walls(screen, 100, 30)
        # displaying the top text
        disp_text(screen, "Wait! I saw something", (old_div(scr_width, 2),
                                                    old_div(scr_height, 2) - 250), pause_text_top, pause_text_tops)

        # displaying highlighted options
        if pause_option == E_Pause_Option.resume:
            disp_text(screen, "JUST A RAT!", (old_div(scr_width, 2),
                                              old_div(scr_height, 2) - 100), pause_text_s, pause_sel_col)
            disp_text(screen, "PRESS ENTER TO RESUME", (old_div(scr_width,
                                                                2), scr_height - 50), message_text1, credit_orange)
        else:
            disp_text(screen, "JUST A RAT!", (old_div(scr_width, 2),
                                              old_div(scr_height, 2) - 100), pause_text, pause_col)
        if pause_option == E_Pause_Option.restart:
            disp_text(screen, "YIKES! GUARDS", (old_div(scr_width, 2),
                                                old_div(scr_height, 2) - 20), pause_text_s, pause_sel_col)
            disp_text(screen, "PRESS ENTER TO RESTART", (old_div(scr_width,
                                                                 2), scr_height - 50), message_text1, credit_orange)
        else:
            disp_text(screen, "YIKES! GUARDS", (old_div(scr_width, 2),
                                                old_div(scr_height, 2) - 20), pause_text, pause_col)
        if pause_option == E_Pause_Option.main_menu:
            disp_text(screen, "PRESS ENTER FOR MAIN MENU", (old_div(scr_width,
                                                                    2), scr_height - 50), message_text1, credit_orange)
            disp_text(screen, "PULL OUT!", (old_div(scr_width, 2),
                                            old_div(scr_height, 2) + 60), pause_text_s, pause_sel_col)
        else:
            disp_text(screen, "PULL OUT!", (old_div(scr_width, 2),
                                            old_div(scr_height, 2) + 60), pause_text, pause_col)
        if pause_option == E_Pause_Option.quit:
            disp_text(screen, "PRESS ENTER TO QUIT", (old_div(scr_width, 2),
                                                      scr_height - 50), message_text1, credit_orange)
            disp_text(screen, "GIVE UP?", (old_div(scr_width, 2),
                                           old_div(scr_height, 2) + 140), pause_text_s, pause_sel_col)
        else:
            disp_text(screen, "GIVE UP?", (old_div(scr_width, 2),
                                           old_div(scr_height, 2) + 140), pause_text, pause_col)

        # drawing a box
        pygame.draw.rect(screen, white, (old_div(scr_width, 2) - 170,
                                         old_div(scr_height, 2) - 160, 340, 360), 2)
        pygame.draw.rect(screen, white, (old_div(scr_width, 2) - 178,
                                         old_div(scr_height, 2) - 168, 356, 376), 3)
        pygame.draw.aaline(screen, white, (old_div(scr_width, 2) - 178, old_div(scr_height,
                                                                                2) - 168), (old_div(scr_width, 2) + 178, old_div(scr_height, 2) - 168), 1)
        pygame.draw.aaline(screen, white, (old_div(scr_width, 2) - 178, old_div(scr_height,
                                                                                2) - 168), (old_div(scr_width, 2) - 178, old_div(scr_height, 2) + 208), 1)
        pygame.draw.aaline(screen, white, (old_div(scr_width, 2) + 178, old_div(scr_height,
                                                                                2) + 208), (old_div(scr_width, 2) - 178, old_div(scr_height, 2) + 208), 1)
        pygame.draw.aaline(screen, white, (old_div(scr_width, 2) + 178, old_div(scr_height,
                                                                                2) + 208), (old_div(scr_width, 2) + 178, old_div(scr_height, 2) - 168), 1)

        # draw ball
        pause_ball.draw(screen)
        pygame.display.update()

        clock.tick(FPS)
