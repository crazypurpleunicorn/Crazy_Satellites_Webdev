import math
import numpy as np
import navpy




def CalculateMeanAnomaly(M,a,G,t,T): # where M is the mass of the planet in one of the focal points and
        n=math.sqrt((G*M/(a**3))) # a is the semi-major axis and G the gravitational constant
                                 #t is the actual time, and T is the ephemeris time
                                 #finally n is the mean angular velocity
        m=n*(t-T)
        return m

def CalculateExcentricAnomaly(m,e): #objective,find iteratively E(excentric anomaly) once we have MeanAnomally

    error = 0.1;
    E = m;
    while (error > 10**-8):
        Eanterior = E;
        E =m + e * math.sin(Eanterior);
        error = abs(Eanterior - E);
    return E

def CalculateRadius(E,a,e):#with the excentric anomaly and semi-major axis
    r=a * (1 - e * math.cos(E))
    return r
def ReturnX(trueanomaly,r):

    x=r*math.cos(trueanomaly)
    return x
def ReturnY(trueanomaly,r):

    y=r*math.sin(trueanomaly)
    return y
def ReturnTrueAnomaly(e,E):
   tanventre2=math.sqrt((1+e)/(1-e))*math.tan(E/2)
   trueanomaly=2*math.atan(tanventre2)
   return trueanomaly

def CreateMatrix():
    r = int(input("Enter number of rows:"))
    c = int(input("Enter number of columns:"))

    matrix = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input("Enter element of [{}][{}]:".format(i, j))))
        matrix.append(row)

    print("Entered matrix is")

    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=" ")
        print("")




def PassiveMatriceRotation(xpositionorbit,ypositionorbit,elevation,rightascension,angleofperigee):#this function will express the orbital position of the satellite in the coordinates of the Space fixed reference frame
      positionontheorbitalplane=[xpositionorbit,ypositionorbit,0]

      elevation=-elevation
      rightascension=-rightascension
      angleofperigee=-angleofperigee

      R3minusW=np.array([[math.cos(angleofperigee),math.sin(angleofperigee),0],[-math.sin(angleofperigee),math.cos(angleofperigee),0],[0,0,1]])
      R1minusi = np.array([[1,0 ,0],[0,math.cos(elevation),math.sin(elevation)],[0,-math.sin(elevation),math.cos(elevation)]])
      R3minusrightascension = np.array([[math.cos(rightascension), math.sin(rightascension), 0],[-math.sin(rightascension), math.cos(rightascension), 0], [0, 0, 1]])

      RotationMatrix=np.matmul(R3minusrightascension,R1minusi)
      RotationMatrix = np.matmul(RotationMatrix,R3minusW)

      newcoordinates=np.matmul(RotationMatrix,positionontheorbitalplane)

      return newcoordinates

def EarthFixedRotation(spacedfixedx,spacefixedy,spacefixedz,time):
    #create the actual matrix with the actual angle
    angularspeedofearthrotation=(2*math.pi)/86164
    initialangle=((2*3600+52*60)/(24*3600))*2*math.pi
    angle=angularspeedofearthrotation*time+initialangle

    R3angle = np.array([[math.cos(angle), math.sin(angle), 0],
                         [-math.sin(angle), math.cos(angle), 0], [0, 0, 1]])

    spacefixedvector=np.array([spacedfixedx,spacefixedy,spacefixedz])
    newcoordinates = np.matmul(R3angle, spacefixedvector)

    return newcoordinates

def TopocentricRotation(WGS84lat,WGS84long,earthfixedvector):
    #create the vector between the observator and the satellite
    #create llaWGS84 vector:
    #altitude 0 because the observer is at the surface of the elipsoid
    #transform this llavectorto a xyz vector in ECEF
    newvectorinECEFcoordinates=navpy.lla2ecef(WGS84lat, WGS84long, 0, latlon_unit='deg', alt_unit='m', model='wgs84')

    positionvectorofsatellitefromobserver=earthfixedvector-newvectorinECEFcoordinates

    #Now we must apply the rotations,𝑟4 = 𝑄1𝑅2(90 − latitudeWettzell)𝑅3(longitudeWettzell)𝑟
    latitude = np.arctan2(newvectorinECEFcoordinates[2], math.sqrt(newvectorinECEFcoordinates[0] ** 2 + newvectorinECEFcoordinates[1] ** 2))

    WGS84long=math.radians(WGS84long)

    R3 = np.array([[math.cos(WGS84long), math.sin(WGS84long), 0],
                         [-math.sin(WGS84long), math.cos(WGS84long), 0], [0, 0, 1]])
    R2=np.array([[math.cos((math.pi/2)-latitude), 0, math.sin((math.pi/2)-latitude)],
                         [0, 1, 0], [-math.sin((math.pi/2)-latitude), 0,math.cos((math.pi/2)-latitude) ]])
    Q=np.array([[-1,0,0],
              [0,1,0], [0,0,1]])

    vectorfromtheobserverframe=np.matmul(R2,R3)
    vectorfromtheobserverframe=np.matmul(Q,vectorfromtheobserverframe)
    vectorfromtheobserverframe=np.matmul(vectorfromtheobserverframe,positionvectorofsatellitefromobserver)

    return  vectorfromtheobserverframe









def CreateParametersOfInterest(M,a,G,time,T,e):

    m = CalculateMeanAnomaly(M, a, G, time, T)
    E = CalculateExcentricAnomaly(m, e)
    m = m % (2 * math.pi)
    E = E % (2 * math.pi)
    r = CalculateRadius(E, a, e)
    tanom = ReturnTrueAnomaly(e, E)
    tanom=tanom%(2*math.pi)
    xpos = ReturnX(tanom, r)
    ypos = ReturnY(tanom, r)
    return [m,E,tanom,xpos,ypos]