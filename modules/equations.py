import math


# p is the density of the air
# CD is drag coefficient
# alpha is the angle of attack
# CL is lift coefficient
# S is the surface area of the wing
# w is the weight of the aircraft
def glide_velocity(plane_weight, air_density, wing_sa):
    return math.sqrt((2 * plane_weight) / (air_density * wing_sa * math.sqrt(drag_coef ** 2 + lift_coef ** 2)))

# Method that returns the glide ratio for a given bank angle.
# Recieves the glide ratio if the plane was going straight
# and the bank angle that the plane is banking at
def angle_glide_ratio(glide_ratio, bank_angle):
    return glide_ratio * math.cos(bank_angle)

def glide_range(glide_ratio, altitude):
    return glide_ratio * altitude

def convert_air_speed(air_speed):
    return air_speed * 5820 / 3600

def time_to_ground(altitude, glide_ratio, air_speed):
    feet_second = convert_air_speed(air_speed)
    return (1 / feet_second) * (glide_ratio * altitude)