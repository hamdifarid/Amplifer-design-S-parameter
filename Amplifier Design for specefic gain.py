import cmath
import math
#math.degrees(math.atan(1.18))
#x = math.sin(math.radians(y))
#print (cmath.polar(2 + 3j

def cal_complex(z,y):
    a = z*(math.cos(math.radians(y)))
    b = z*(math.sin(math.radians(y)))
    comp = complex(a,b)
    return comp

def cal_complexconj(z,y):
    a = z*(math.cos(math.radians(y)))
    b = z*(math.sin(math.radians(y)))
    comp = complex(a,b)
    return comp.conjugate()

def calculate_polar(z):
    a = z.real
    b = z.imag
    r = abs(z)
    return ((a**2+b**2)**0.5, math.degrees(math.acos(a/r) if r != 0 else 0))

def mod(z):
    a = z.real
    b = z.imag
    r = abs(z)
    return ((a**2+b**2)**0.5)

def cvtdb(z):
    a = 10*math.log(z,10)
    return a

def cvtlog(z):
    a = 10**(z/10)
    return a


s11 = float(input('Enter the R value for s11'))#0.75
s11angle = float(input('Enter the angle for s11'))#-120
s22 = float(input('Enter the R value for s22'))#0.6
s22angle = float(input('Enter the angle or s22'))#-70
s21 = float(input('Enter the R valye for s21'))#2.5
s21angle = float(input('Enter the angle for s21'))#80
s12 = float(input('Enter the R value or s12'))#0
s12angle = float(input('Enter the angle for s12'))#0

Gsmax = 3
Gsmin = 2
Glmax = 1
Glmin = 0


gs = 1/(1-s11**2)
gl = 1/(1-s22**2)
g0 = (s21**2)
gtu = cvtdb(gs)+cvtdb(gl)+cvtdb(g0)
delta=(cal_complex(s11,s11angle)*cal_complex(s22,s22angle))-(cal_complex(s12,s12angle)*cal_complex(s21,s21angle))
deltamod = (mod(delta))
Gsmaxval = cvtlog(Gsmax)/gs
Glmaxval = cvtlog(Glmax)/gl
Gsminval = cvtlog(Gsmin)/gs
Glminval = cvtlog(Glmin)/gl
Csmax = (Gsmaxval*cal_complexconj(s11,s11angle))/(1-(1-Gsmaxval)*(s11**2))
Clmax = (Glmaxval*cal_complexconj(s22,s22angle))/(1-(1-Glmaxval)*(s22**2))
Rsmax = (((1-Gsmaxval)**0.5)*(1-s11**2))/(1-(1-Gsmaxval)*(s11**2))
Rlmax = (((1-Glmaxval)**0.5)*(1-s22**2))/(1-(1-Glmaxval)*(s22**2))
Taus = calculate_polar(cal_complexconj(s11,s11angle))
Taul = calculate_polar(cal_complexconj(s22,s22angle))
Csmin = (Gsminval*cal_complexconj(s11,s11angle))/(1-(1-Gsminval)*(s11**2))
Clmin = (Glminval*cal_complexconj(s22,s22angle))/(1-(1-Glminval)*(s22**2))
Rsmin = (((1-Gsminval)**0.5)*(1-s11**2))/(1-(1-Gsminval)*(s11**2))
Rlmin = (((1-Glminval)**0.5)*(1-s22**2))/(1-(1-Glminval)*(s22**2))
if s12!=0:
    k = (1+(deltamod**2)-(s11**2)-(s22**2))/(2*(cal_complex(s12,s12angle)*cal_complex(s21,s21angle)))          
    print(mod(k))
    if mod(k)>1:
        print('unconditoinally stable')
    if mod(k)<1:
        print('potentionally unstable')
    print(deltamod)
if s12==0:
    print('As s12 is 0 Value of K is infinite and amplifier is unconditionally stable')
    print('maximum unilateral gain=',gtu,'db')#DO NOT CONSIDER IF S12!=0


print('gs=',gs,'gL=',gl,'G0=',g0)
print('gs=',cvtdb(gs),'DB')
print('gL=',cvtdb(gl),'DB')
print('G0=',cvtdb(g0),'DB')
print('Taus= ',Taus)
print('Taul= ',Taul)
print('Csmax=',calculate_polar(Csmax))
print('Clmax=',calculate_polar(Clmax))
print('Rsmax=',calculate_polar(Rsmax))
print('Rlmax=',calculate_polar(Rlmax))
print('Csmin=',calculate_polar(Csmin))
print('Clmin=',calculate_polar(Clmin))
print('Rsmin=',calculate_polar(Rsmin))
print('Rlmin=',calculate_polar(Rlmin))


