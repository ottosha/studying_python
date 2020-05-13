#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    a = 0
    while not wall_is_on_the_right():
        if wall_is_above():
            fill_cell()
        elif not wall_is_above():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    a+=1
                elif cell_is_filled() is False:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        move_right()
    mov(AX, a)

if __name__ == '__main__':
    run_tasks()
