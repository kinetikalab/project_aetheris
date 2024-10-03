#input parameters
import math

#please ream readme.md for dimentions definitions

u0 = 3.5 #volume mix ratio air / water
T = 40+273 #Water temperature

Vp = 8/16.6667 #m3/h - water pump capacity
Pc = 1*101325 #Pa - outlet of the ejector pressure
Pp = 10*101325 #Pa - pump pressure

Ps = 7381 #Pa - water vapour pressure in giving temperature

b = 0.52 #mixing furnel angel

fi1 = 0.95
fi2 = 0.975
fi3 = 0.9
fi4 = 0.925

a = (2-fi3**2)/(2*fi2-1/fi1)*(1+u0)**2

a = a

Pn = (a*Pc-Pp)/(a-1) #Pa pressure in dishcarge chamber

fp1 = Vp*10**6/(0.95*3600*(2*(Pp-Pn)/1000)**0.5) #square of ejectore nozzle
dp1 = (4*fp1/math.pi)**0.5 #diameter of ejector nozzle

d3 = dp1*((Pp-Pn)/(Pc-Pn))**0.5 #diameter of mixing tube

Lc1 = (0.37 + u0)*dp1/(4.4*0.08) #distance from nozzle to mixing tube furnel

d4 = 1.55*dp1*(1+u0)

Lc2 = (d4-d3)/(2*math.tan(b))

dp_ratio = (Pp-Pn)/(Pc-Pn)
Lk = dp1*20*(dp_ratio-1)

print('dp1 = '+str(round(dp1,1))+' mm')
print('d3 = '+str(round(d3,1))+' mm')
print('Lc1 = '+str(round(Lc1,1))+' mm')
print('Lc2 = '+str(round(Lc2,1))+' mm')
print('d4 = '+str(round(d4,1))+' mm')
print('Lk = '+str(round(Lk,1))+' mm')