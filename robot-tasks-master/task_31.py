#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    b = 1
    while b > 0:
        b = 0
        while wall_is_on_the_right() is False:
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
                    b+=1
            move_right()
        while wall_is_on_the_left() is False:
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
                    b+=1
            move_left()


if __name__ == '__main__':
    run_tasks()
