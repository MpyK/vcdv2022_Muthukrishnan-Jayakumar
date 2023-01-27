import numpy as np
import matplotlib.pyplot as mpl #library to plot
print("Program to calculate Braking distance:")
m=int(input("Enter the mass of the car in kg: ")) #user input for mass of car
v=int(input("Enter the speed of the car in km/h: ")) #user input for velocity of car
g = 9.8; # acceleration due to gravity in earth
num=int(input(" Select Road type:\nPress 1 for concrete\n2 for ice\n3 for water\n4 for gravel\n5 for sand ")) # options given to user to choose appropriate road type
if num == 1:
    n=int(input(print("select road condition:\npress 6 for dry\n7 for wet"))) # user can choose concrete road condition
    if n==6:
        mu=0.5 #coefficient of friction dry
    else:
        mu=0.35 #coefficient of friction wet
elif num==2:
    n = int(input(print("select road condition:\npress 6 for dry\n7 for wet"))) # user can choose ice road condition
    if n == 6:
        mu = 0.15 #coefficient of friction dry
    else:
        mu = 0.08 #coefficient of friction wet
elif num==3:
    mu=0.05 #coefficient of friction water road
elif num==4:
    mu=0.35 #coefficient of friction gravel road
else:
    mu=0.3 #coefficient of friction sand road
rd=(v*0.01) #Normal reaction time in human is 0.01, reaction distance = velocity of car * reaction time
vn=v/3.6    #This formula converts the velocity of car from km/h to m/s.
bd=(0.051*pow(vn,2))/mu  # the 0.051 is a constant - (1/2g). Actual formula for braking distance is pow(vn,2)/2*mu*g
sd=(bd+rd)  # Actual stopping distance of car is breaking distance plus reaction distance
print("The braking distance is "+str(sd)+" m")
bt=sd/vn #breaking time is stopping distance divided by velocity
a=-((pow(vn,2))/(2*sd)) #derived from formula s=ut + 0.5*a*pow(t,2) where u=0, a is deceleration hence negative
taxis = np.arange(0, bt, bt/2000) #plotting of time in a resolution of 1/2000
vaxis = vn + (a * taxis) # copied formula from colleague siddarth s2210787022
daxis = vn * taxis + (0.5 * a * pow(a, 2)) # copied formula from colleague siddarth s2210787022

mpl.plot(taxis, daxis) # plotting deceleration vs time
mpl.show() # to display the plot






