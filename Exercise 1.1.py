import numpy as np

x = float(input("Enter x: "))
y = float(input("Enter y: "))

r = ((x**2)+(y**2))**0.5

if(x == 0 and y > 0):
    print ("r =",r,"theta (in degrees) = 90")

elif(x == 0 and y < 0):
    print ("r =",r,"theta (in degrees) = 270")



if(x>0 and y>0):
    q = y/x
    d = (np.arctan(q))*(180/np.pi)
    theta = d
    print ("r =",r," theta (in degrees) =",theta)

elif (x<0 and y>0):
    q = y/x
    d = (np.arctan(q))*(180/np.pi)
    theta = d + 180
    print ("r =",r," theta (in degrees) =",theta)
    
elif (x<0 and y<0):
    q = y/x
    d = (np.arctan(q))*(180/np.pi)
    theta = d + 180
    print ("r =",r," theta (in degrees) =",theta)

elif (x>0 and y<0):
    q = y/x
    d = (np.arctan(q))*(180/np.pi)
    theta = 360 + d
    print ("r =",r," theta (in degrees) =",theta)
