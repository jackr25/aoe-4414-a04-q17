# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second

# Parameters:
# o_x_km = origin x coord in km
# o_y_km = origin y coord in km
# o_z_km = origin z coord in km
# x_km = position x coord in km 
# y_km = position y coord in km
# z_km = position z coord in km
# Output:
#  outputs SEZ coordindates in order s_km e_km z_km
#
# Written by Jack Rathert
# Other contributors: None
# 
# Test Case Setup : python3 ecef_to_sez.py 822.933 -4787.187 4120.262 1131.698 -4479.324 4430.228
# import Python modules
# e.g., import math # math module
import sys 
import math as m
from math import trunc
# functions

def date_to_JD(Y: int,Mo: int,D: int,h: int,m:int,s: float):
 
  JD = D - 32075 \
   +  int( 1461 * ( Y + 4800 +  int((Mo-14)/12) ) /4) \
   + int( 367 * ( Mo - 2 - (int((Mo-14)/12) *12 )) / 12) \
   - int( 3 * int(( Y + 4900 + int((Mo-14)/12)) /100 ) /4 )

  JDmidnight = (JD) - 0.5
  Dfrac = (s + 60*(m + 60*h))/86400
  JDfrac = JDmidnight + Dfrac

  return JDfrac

# initialize script arguments
Y = int(0)
Mo = int(0)
D = int(0)
h = int(0)
m = int(0)
s = float(0.0)

# parse script arguments
if len(sys.argv)==7:
  Y = int(sys.argv[1])
  Mo = int(sys.argv[2])
  D = int(sys.argv[3])
  h = int(sys.argv[4])
  m = int(sys.argv[5])
  s = float(sys.argv[6])
  ...
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

# write script below this line
JDfrac = date_to_JD(Y,Mo,D,h,m,s)
print(JDfrac)
