#import libraries
import math
import Functionlibrary as fl
import numpy as np
import matplotlib.pyplot as plt
import folium as fo




#Define Constants
G=6.67430*math.pow(10, -11)
M=5.9722*math.pow(10,24)
#let's read from the txt file:

with open(r"C:\Users\Usuario\Desktop\MeineSatelliten.txt","r") as file:
    #HOW MANY SATELLITES ARE THERE IN THE .TXT FILE?

    length=len(file.readlines())
    file.close()
    #LISTS OF LISTS.AT THE END OF EXECUTION, WE WANT TO HAVE A LIST OF PARAMETERS FOR EVERY SATELLITE,WE WILL STORE THIS INFO IN A LIST OF LIST
    listofspacefixedcoordinatex = []
    listofspacefixedcoordinatey = []
    listofspacefixedcoordinatez = []

    listofearthfixedcoordinatex = []
    listofearthfixedcoordinatey = []
    listofearthfixedcoordinatez = []
    names = []
    xx = []
    yy = []
    listoflongitudes=[]
    listoflatitudes=[]
    listofelevations=[]
    listofazimuths=[]

    with open(r"C:\Users\Usuario\Desktop\MeineSatelliten.txt", "r") as file:
        #WE INITIALIZE THE COUNTER IN ORDER TO READ EVERY ROW OF THE TXT FILE
        counter = 0
        while (counter < length):

            listofthefile = file.readline()
            #READ A LINE AND GET THE PARAMETERS FROM THE THIS LINE
            listofthefile = listofthefile.split(",")
            name = listofthefile[0]
            e = float(listofthefile[2])
            a = float(listofthefile[1])
            rightascension = ((float(listofthefile[4]) / 360) * 2 * math.pi)
            elevation = ((float(listofthefile[3]) / 360) * 2 * math.pi)
            angleofperigee = ((float(listofthefile[5]) / 360) * 2 * math.pi)
            T = float(listofthefile[6]) * 3600  # in seconds
            #ADD THE NAME OF THE SATELLITE TO NAME LIST
            names.append(name)

            # CREATE A VECTOR OF TIMES DURING GIVEN HOURS WITH JUMPS OF GIVEN SECONDS
            hourstosimulate=24
            incrementoftime=10
            t = np.arange(0,hourstosimulate* 3600,incrementoftime)

            WGS84lat=49.151248
            WGS84lon=12.906711
            #LISTS OF PARAMETERS
            x = []
            y = []
            meananomaly = []
            excentricanomaly = []
            trueanomaly = []
            coordinatesinspacedfixed = []
            spacefixedcoordinatex = []
            spacefixedcoordinatey = []
            spacefixedcoordinatez = []
            earthfixedcoordinatex = []
            earthfixedcoordinatey = []
            earthfixedcoordinatez = []
            longitudes=[]
            latitudes=[]
            azimuths=[]
            elevations=[]



            for time in t:
                # CREATE PARAMETERS OF INTEREST
                parameters=fl.CreateParametersOfInterest(M,a,G,time,T,e)
                m= parameters[0]
                E=parameters[1]
                tanom=parameters[2]
                xpos=parameters[3]
                ypos=parameters[4]


                # apply rotations and get spacefixed parameters and earth fixed parameters
                spacefixedcoordinate = fl.PassiveMatriceRotation(xpos, ypos, elevation, rightascension, angleofperigee)
                spacefixedcoordinatexx = spacefixedcoordinate[0]
                spacefixedcoordinateyy = spacefixedcoordinate[1]
                spacefixedcoordinatezz = spacefixedcoordinate[2]

                earthfixedcoordinates = fl.EarthFixedRotation(spacefixedcoordinatexx, spacefixedcoordinateyy,spacefixedcoordinatezz, time)
                earthfixedcoordinatexx= earthfixedcoordinates[0]
                earthfixedcoordinateyy=earthfixedcoordinates[1]
                earthfixedcoordinatezz=earthfixedcoordinates[2]

                topocentriccoordinates=fl.TopocentricRotation(WGS84lat,WGS84lon,earthfixedcoordinates)
                topocentriccoordinatexx = topocentriccoordinates[0]
                topocentriccoordinateyy = topocentriccoordinates[1]
                topocentriccoordinatezz = topocentriccoordinates[2]

                longitude = np.arctan2(earthfixedcoordinateyy,earthfixedcoordinatexx)
                latitude = np.arctan2(earthfixedcoordinatezz,math.sqrt(earthfixedcoordinatexx**2+earthfixedcoordinateyy**2))
                longitude=longitude*(360)/(2*math.pi)
                latitude=latitude*(360)/(2*math.pi)

                azimuth = np.arctan2(topocentriccoordinateyy, topocentriccoordinatexx)
                elevationx = np.arctan2(topocentriccoordinatezz,math.sqrt(topocentriccoordinatexx ** 2 + topocentriccoordinateyy ** 2))
                azimuth = azimuth*(360)/(2 * math.pi)
                elevationx = elevationx*(360)/(2 * math.pi)




                #ADD EACH PARAMETER OF INTEREST TO ITS PARAMETER LIST
                trueanomaly.append(tanom)
                meananomaly.append(m)
                excentricanomaly.append(E)
                x.append(xpos)
                y.append(ypos)
                spacefixedcoordinatex.append(spacefixedcoordinatexx)
                spacefixedcoordinatey.append(spacefixedcoordinateyy)
                spacefixedcoordinatez.append(spacefixedcoordinatezz)
                #coordinatesinspacedfixed.append(spacefixedcoordinate)
                earthfixedcoordinatex.append(earthfixedcoordinatexx)
                earthfixedcoordinatey.append(earthfixedcoordinateyy)
                earthfixedcoordinatez.append(earthfixedcoordinatezz)
                latitudes.append(latitude)
                longitudes.append(longitude)
                azimuths.append(azimuth)
                elevations.append(elevationx)
                #AT THE END OF THE FOR LOOP WE WILL HAVE CREATED ALL NECESSARY PARAMETERS.(WHICH WILL BE STORED IN THE ABOVE LISTS) FOR A GIVEN SATELLITE/ROW


            #KNOW THE NEXT STEP IS TO SAVE THOSE LISTS, IN A LIST SO THE FOLLOWING ARE LISTS OF LISTS:
            xx.append(x)
            yy.append(y)
            listofspacefixedcoordinatex.append(spacefixedcoordinatex)
            listofspacefixedcoordinatey.append(spacefixedcoordinatey)
            listofspacefixedcoordinatez.append(spacefixedcoordinatez)
            listofearthfixedcoordinatex.append(earthfixedcoordinatex)
            listofearthfixedcoordinatey.append(earthfixedcoordinatey)
            listofearthfixedcoordinatez.append(earthfixedcoordinatez)
            listoflatitudes.append(latitudes)
            listoflongitudes.append(longitudes)
            listofazimuths.append(azimuths)
            listofelevations.append(elevations)

            t=t/3600
            plt.plot(t, meananomaly,'g')
            plt.plot(t,excentricanomaly,'r')
            plt.plot(t,trueanomaly,color='purple')
            plt.title(name)
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #plt.show()

            #ax = plt.axes(projection='3d')
            #ax.plot3D(spacefixedcoordinatex, spacefixedcoordinatey, spacefixedcoordinatez, 'green')
            #ax.set_title(name)
            #plt.show()

            counter = counter + 1
counter3 = 0

while (counter3 < length):
    plt.plot(xx[counter3], yy[counter3])
    counter3 = counter3 + 1
plt.xlim([-6*math.pow(10,7), +6*math.pow(10,7)])
plt.ylim([-5*math.pow(10,7), +5*math.pow(10,7)])

plt.show()

counter3 = 0

while (counter3 < length):
    plt.plot(listoflongitudes[counter3],listoflatitudes[counter3])
    counter3 = counter3 + 1
plt.xlim([-180,180])
plt.ylim([-90,90])

plt.show()






counter2=0
ax = plt.axes(projection='3d')
while(counter2<length):

    ax.plot3D(listofspacefixedcoordinatex[counter2], listofspacefixedcoordinatey[counter2], listofspacefixedcoordinatez[counter2], label=names[counter2])
    counter2=counter2+1

ax.set_title('all satellites')
plt.legend()
plt.xlim([-4*math.pow(10,7), +4*math.pow(10,7)])
plt.ylim([-4*math.pow(10,7), +4*math.pow(10,7)])


plt.show()

counter2=0
ax = plt.axes(projection='3d')
while(counter2<length):
    ax.plot3D(listofearthfixedcoordinatex[counter2], listofearthfixedcoordinatey[counter2], listofearthfixedcoordinatez[counter2], label=names[counter2])
    counter2=counter2+1

ax.set_title('all satellites')
plt.legend()
plt.xlim([-4*math.pow(10,7), +4*math.pow(10,7)])
plt.ylim([-4*math.pow(10,7), +4*math.pow(10,7)])


plt.show()

# setting the axes projection as polar
plt.axes(projection='polar')

# setting the radius

# creating an array containing the
# radian values
j=0
while(j<length):

    l1=listofazimuths[j];
    l11=listofelevations[j]
    i=0
    while(i<len(l1)):
        if(l11[i]>=0):

            plt.polar(math.radians(l1[i]),-1*(l11[i]-90), 'r.')

        i=i+1
    plt.polar(0, 90, 'b.')
    plt.polar(0, 0, 'b.')
    plt.show()
    j=j+1


# display the Polar plot
plt.show()



file.close()




