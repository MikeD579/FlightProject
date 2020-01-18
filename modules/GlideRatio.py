import math


# Calculate the lift using given variables.
def calcLift(CL_liftCoeffcient, P_airDensity, S_wingSurfacearea, V_airSpeed):
   lift = CL_liftCoeffcient * 0.5 * P_airDensity * (V_airSpeed**2) * S_wingSurfacearea
   return lift

# Calculate the drag using given variables.
def calcDrag(CD_dragCoeffcient, P_airDensity, S_wingSurfacearea, V_airSpeed):
   drag = CD_dragCoeffcient * 0.5 * P_airDensity * (V_airSpeed**2) * S_wingSurfacearea
   return drag

def calcGlide(bankAngle, lift, drag):
   glide = (lift * math.cos(bankAngle)) / drag
   return glide

def main():
   # we need to make sure we add the units on all of these
   CD_dragCoeffcient = float(input("Please enter your plane's drag coefficient: "))
   CL_liftCoeffcient = float(input("Please enter your plane's lift coefficient: "))
   # Make sure to add the units
   P_airDensity = float(input("Please enter the air density of your location: "))
   # front wings or back wings or both?
   S_wingSurfacearea = float(input("Please enter the surface area of your wing: "))
   # Wing speed? or flight speed?
   V_airSpeed = float(input("Please enter your locations air speed: "))
   bankAngle = float(input("Please enter your desired bank angle: "))

   lift = calcLift(CL_liftCoeffcient, P_airDensity, S_wingSurfacearea, V_airSpeed)
   drag = calcDrag(CD_dragCoeffcient, P_airDensity, S_wingSurfacearea, V_airSpeed)

   glide = calcGlide(bankAngle, lift, drag)

   print(glide)

if __name__ == "__main__":
   main()
