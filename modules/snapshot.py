import csv
import math
import equations

# Test function to output all values of landing to a csv file for easy readability
def main():
    # Get the alititude and airspeed and glide ratio
    start_altitude = eval(input("Please input the altitude: "))
    airspeed = eval(input("Please enter the airspeed: "))
    glideratio = eval(input("Please input the glide ratio: "))

    # Calculate landings iterating by 1 degree
    for i in range(0, 46):
        change_glide_ratio(glideratio, i)
        
    print(equations.time_to_ground(start_altitude, glideratio, airspeed))
    # Rate of turn (degrees/second) = 1091 x Tan(Ө) / Airspeed in Knots
    # Glide Ratio Turn = Glide Ratio Straight x Cos(Ө)

# Return where the plane is going to land in the x coordinate
def landing_x(cur_alt):
    equations.glide_range(cur_alt)

# Return where the plane is going to land in the z coordinate
def landing_z():
    pass

# Function that takes the straight line ratio and returns a new bank angle for a given bank angle.
def change_glide_ratio(glideratio, bank_angle):
    return glideratio * math.cos(bank_angle)

if __name__ == "__main__":
    main()