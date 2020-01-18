import math

def lift(CL_liftCoeffcient, P_airDensity, S_wingSurfacearea, V_airSpeed):
   Lift = CL_liftCoeffcient * 0.5 * P_airDensity * (V_airSpeed**2) * S_wingSurfacearea
   return Lift

def drag(CD_dragCoeffcient, P_airDensity, S_wingSurfacearea, V_airSpeed):
   Drag = CD_dragCoeffcient * 0.5 * P_airDensity * (V_airSpeed**2) * S_wingSurfacearea
   return Drag

def glide(bankAngle, Lift, Drag):
   Glide = (Lift * math.cos(bankAngle)) / Drag
   return Glide

def main():
   CD_dragCoeffcient = float(input("Please enter your plane's drag coefficient: "))
   CL_liftCoeffcient = float(input("Please enter your plane's lift coefficient: "))
   P_airDensity = float(input("Please enter the air density of your location: "))
   S_wingSurfacearea = float(input("Please enter the surface area of your wing: "))
   V_airSpeed = float(input("Please enter your locations air speed: "))
   bankAngle = float(input("Please enter your desired bank angle: "))

   Lift = lift(CL_liftCoeffcient, P_airDensity, S_wingSurfacearea, V_airSpeed)
   Drag = drag(CD_dragCoeffcient, P_airDensity, S_wingSurfacearea, V_airSpeed)

   Glide = glide(bankAngle, Lift, Drag)

   print(Glide)

if __name__ == "__main__":
   main()
