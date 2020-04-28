# This snapshot will find the coordinates of where the plane can land with a given
# glide ratio and velocity. The plane's origin is going to be (0,0). All landing
# locations will be coordinate pairs.
#
# Written in Python 3
# Last edit date 04-21-2020

import math


def main():
    glide_ratio = eval(input('Please enter the glide ratio of the plane: '))
    plane_vel = eval(input('Please enter the plane\'s velocity: '))
    start_alt = eval(input('Please enter the starting altitude: '))
    # starting position is the plane. which is (0,0)
    start_pos = (0,0)
    landing_pos = []

    # Calculate where the plane will land if there is no chnage in the bank angle.
    landing_pos.append(calc_landing(glide_ratio, plane_vel, 0, start_alt))

    print(landing_pos[0])



# Function that will return a tuple that is a coordinate pair of where the plane will land
# given a glide ratio, velocity, and bank angle.
def calc_landing(glide_ratio, velocity, bank_angle, alt):
    if bank_angle == 0:
        return (0, glide_ratio * alt)
    else:
        # Assume the bank angle is held for 2 seconds and then is released.
        # The plane will continue straight from there.

        # Figure out how much height is lost and then find wh
        bank_dist = 2 * velocity
        bank_x = bank_dist * math.cos(bank_angle)
        bank_y = bank_dist * math.cos(bank_angle)

        h_lost = 2 * velocity / (glide_ratio * math.cos(bank_angle))

        h_new = alt - h_lost
        straight_dist = h_new * glide_ratio




# Change the glide ratio for the given bank angle.
def change_glide(cur_glide, bank_angle):
    return cur_glide * bank_angle

if __name__ == '__main__':
    main()