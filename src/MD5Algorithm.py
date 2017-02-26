import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from scipy import cluster
from sklearn.cluster import KMeans
from firebase import firebase
import openpyxl
import os
from sklearn.cluster import KMeans

wb = openpyxl.load_workbook('DisasterData.xlsx')
sheet = wb.get_sheet_by_name('Data')

latitudes = []
longitudes = []

latitudeSum = 0
longitudeSum = 0


for colOfCellObjects in sheet['A2':'A99']:
    for cellObj in colOfCellObjects:
        latitudes.append(cellObj.value)

for colOfCellObjects in sheet['B2':'B99']:
        for cellObj in colOfCellObjects:
            longitudes.append(cellObj.value)

for i in latitudes:
    #print(i)
    latitudeSum += i
for i in longitudes:
    #print(i)
    longitudeSum += 1

latNP = np.array(latitudes)
longNP = np.array(longitudes)
coordinates = np.column_stack((latNP, longNP))


latitudeAvg = latitudeSum/len(latitudes)
longitudeAvg = longitudeSum/len(longitudes)

latitudeMin = min(latitudes)
latitudeMax = max(latitudes)
longitudeMin = min(longitudes)
longitudeMax = max(longitudes)

#print(latitudeMin, latitudeMax, longitudeMin, longitudeMax)

fig, ax = plt.subplots(figsize=(10,20))

m = Basemap(resolution = 'f', projection = 'merc', lat_0 = latitudeAvg,
            lon_0 = longitudeAvg, llcrnrlon = (longitudeMin-0.01),
            llcrnrlat = (latitudeMin-0.01), urcrnrlon = (longitudeMax+0.01),
            urcrnrlat=(latitudeMax+0.01))

m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
m.drawcoastlines()
m.readshapefile('Haiti_all_roads','HaitiRoads')
m.readshapefile('hti_watrcrsl_rvr_minustah', 'HaitiRivers')

"""""################################################################### figure out how to make rivers blue
seg = m.HaitiRivers
poly = Polygon(seg,edgecolor='blue')
ax.add_patch(poly)

x, y = zip(m.hti_watrcrsl_rvr_minustah, m.HaitiRivers)
m.plot(x, y, marker=None, color='b')
"""
""""
for i in range(0, len(latitudes), 1):
    midLon = longitudes[i]
    midLat = latitudes[i]
    x, y = m(midLon, midLat)
    m.plot(x, y, 'ro', markersize=11)
"""
#x, y = m(longitudes,latitudes)
#m.scatter(x, y, marker='D',color='m')

#K = 6

#initial = [cluster.vq.kmeans(coordinates,i) for i in range(1,10)]
#print(initial)

#cent, var = initial[K-1]
#assignment, cdist = cluster.vq.vq(coordinates,cent)
#m.scatter(coordinates[:,1], coordinates[:,0], c=assignment,s=1000)
#print(assignment)

K = 4
kmeans = KMeans(n_clusters=K, random_state=3000).fit(coordinates)
centroids = kmeans.cluster_centers_
assignment = kmeans.labels_


print(assignment)
print(centroids)

#plt.scatter(centroids[:, 0], centroids[:, 1],
 #           marker = 'x', s = 169, linewidths = 3, color = 'w', zorder = 10)

count0 = True
count1 = True
count2 = True
count3 = True
count4 = True
count5 = True

for pt in range(0, len(latitudes), 1):
    lon = longitudes[pt]
    lat = latitudes[pt]
    x,y = m(lon,lat)
    if assignment[pt] == 0:
        m.plot(x, y, 'bo', markersize=11)
        if count0:
            midLon = centroids[0,1]
            midLat = centroids[0,0]
            x, y = m(midLon, midLat)
            m.plot(x, y, 'b*', markersize=14)
            count0 = False
    if assignment[pt] == 1:
        m.plot(x, y, 'go', markersize=11)
        if count1:
            midLon = centroids[1,1]
            midLat = centroids[1,0]
            x, y = m(midLon, midLat)
            m.plot(x, y, 'g*', markersize=14)
            count1 = False
    if assignment[pt] == 2:
        m.plot(x, y, 'ro', markersize=11)
        if count2:
            midLon = centroids[2,1]
            midLat = centroids[2,0]
            x, y = m(midLon, midLat)
            m.plot(x, y, 'r*', markersize=14)
            count2 = False
    if assignment[pt] == 3:
        m.plot(x, y, 'co', markersize=11)
        if count3:
            midLon = centroids[3,1]
            midLat = centroids[3,0]
            x, y = m(midLon, midLat)
            m.plot(x, y, 'c*', markersize=14)
            count3 = False
    if assignment[pt] == 4:
        m.plot(x, y, 'mo', markersize=11)
        if count4:
            midLon = centroids[4,1]
            midLat = centroids[4,0]
            x, y = m(midLon, midLat)
            m.plot(x, y, 'm*', markersize=14)
            count4 = False
    if assignment[pt] == 5:
        m.plot(x, y, 'yo', markersize=11)

        if count5:
            midLon = centroids[5,1]
            midLat = centroids[5,0]
            x, y = m(midLon, midLat)
            m.plot(x, y, 'y*', markersize=14)
            count5 = False


"""
cleanAssignment = assignment.tolist()
cleanLength = len(cleanAssignment)

for i in range(0, K, 1):
    try:
        value = cleanAssignment[i+1]
        while cleanAssignment[i+1] == cleanAssignment[i]:
            del cleanAssignment[i+1]
            try:
                value = cleanAssignment[i+1]
            except IndexError:
                break
    except IndexError:
        break
    print(cleanAssignment)
"""
""""
for i in range(0, K, 1):
    lon = centroids[i, 1]
    lat = centroids[i, 0]
    x, y = m(lon,lat)
    if cleanAssignment[i] == 0:
        m.plot(x, y, 'y*', markersize=15)
    if cleanAssignment[i] == 1:
        m.plot(x, y, 'r*', markersize=15)
    if cleanAssignment[i] == 2:
        m.plot(x, y, 'g*', markersize=15)
    if cleanAssignment[i] == 3:
        m.plot(x, y, 'b*', markersize=15)
    if cleanAssignment[i] == 4:
        m.plot(x, y, 'c*', markersize=15)
    if cleanAssignment[i] == 5:
        m.plot(x, y, 'm*', markersize=15)
"""


plt.show()

############################################################
############################################################
############################################################
"""""
def cluster_points(X, mu):
    clusters = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]]))
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(x, K):
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        clusters = cluster_points(X, mu)
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)
"""
