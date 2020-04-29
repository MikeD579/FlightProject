# This snapshot will find the coordinates of where the plane can land with a given
# glide ratio and velocity. The plane's origin is going to be (0,0). All landing
# locations will be coordinate pairs.
#
# Written in Python 3
# Last edit date 04-28-2020

# This is test edit. 2

import math
import json
BANK_TIME = 2

def main():
    glide_ratio = eval(input('Please enter the glide ratio of the plane: '))
    plane_vel = eval(input('Please enter the plane\'s velocity: '))
    start_alt = eval(input('Please enter the starting altitude: '))
    # starting position is the plane. which is (0,0)
    start_pos = (0,0)
    landing_pos = []

    # Calculate where the plane will land if there is no chnage in the bank angle.
    for angle in range(0, 45, 5):
        coord = calc_landing(glide_ratio, plane_vel, angle, start_alt)
        landing_pos.append(coord)

        if angle != 0:
            landing_pos.append((abs(coord[0]), abs(coord[1])))

        # landing_pos.append(calc_landing(glide_ratio, plane_vel, angle, start_alt))

    for i in range(0, len(landing_pos)):
        print(landing_pos[i])
        


# Function that will return a tuple that is a coordinate pair of where the plane will land
# given a glide ratio, velocity, and bank angle.
def calc_landing(glide_ratio, velocity, bank_angle, alt):
    global BANK_TIME
    if bank_angle == 0:
        return (0, glide_ratio * alt)
    else:
        # Assume the bank angle is held for 2 seconds and then is released.
        # The plane will continue straight from there.

        # Figure out how much height is lost and then find wh
        turn_rate = get_turn_rate(velocity, bank_angle)
        deg_traveled = BANK_TIME * turn_rate
        

        turn_rad = get_turn_radius(velocity, bank_angle)
        arc_len = get_arc_len(turn_rad, deg_traveled)

        h_lost = 2 * velocity / (glide_ratio)
        h_new = alt - h_lost
        straight_dist = h_new * glide_ratio

        new_facing = 90 + deg_traveled

        bank_x = turn_rad - turn_rad * math.cos(conv_rad(deg_traveled))
        bank_y = turn_rad * math.sin(conv_rad(deg_traveled))

        polar_mag = math.sqrt(bank_x ** 2 + bank_y ** 2)
        polar_mag = polar_mag + straight_dist

        final_x = polar_mag * math.cos(conv_rad(new_facing))
        final_y = polar_mag * math.sin(conv_rad(new_facing))

        return (final_x, final_y)
    

# Convert from degrees to radians
def conv_rad(degrees):
    return degrees * math.pi / 180

# Get the turn rate based upon the FAA Pilot handbook
# https://aviation.stackexchange.com/questions/2871/how-to-calculate-angular-velocity-and-radius-of-a-turn
# This returns the rate of turn in degrees per second.
def get_turn_rate(velocity, bank_angle):
    return 1091 * math.tan(conv_rad(bank_angle)) / velocity

# Get the radius of the turn based upon FAA Pilot Handbook
# https://aviation.stackexchange.com/questions/2871/how-to-calculate-angular-velocity-and-radius-of-a-turn
# Returns the radius in feet
def get_turn_radius(velocity, bank_angle):
    return velocity ** 2 / (11.26 * math.tan(bank_angle * math.pi / 180))

# Get the arc lenght of the planes bank
# Returns the arc length in feet
def get_arc_len(radius, degrees):
    return 2 * math.pi * radius * degrees / 360

# Change the glide ratio for the given bank angle.
def change_glide(cur_glide, bank_angle):
    return cur_glide * math.cos(bank_angle * math.pi / 180)

if __name__ == '__main__':
    main()