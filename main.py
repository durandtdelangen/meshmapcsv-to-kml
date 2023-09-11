import csv

from data_point import DataPoint

#Open CSV Files
#peerinfofile = input("Enter the path to the peer info file: ")
peerinfofile = "C:\Code\Projects\meshmapcsv-to-kml\Examples\Meshmapper_2023-08-29_10-50-35_peer_info.csv"
peerinfodata = list(csv.DictReader(open(peerinfofile)))

#Add import list of APT serials

#Declare lists for writing kml
points = []
bestScores = dict()
secondBestScores = dict()
bestTwoGigScores = dict()
bestFiveGigScores = dict()

dataPoints = []

# Get Best
for dataPoint in dataPoints:
    bestExisting = None
    if dataPoint.PointNum in bestScores:
        bestExisting = bestScores[dataPoint.PointNum]
    
    if int(dataPoint.Signal) !=0:
        if (bestExisting == None or int(bestExisting.Signal) < int(dataPoint.Signal)):
            bestScores[dataPoint.PointNum] = dataPoint


# Get Second Best
for dataPoint in dataPoints:
    bestExisting = bestScores[dataPoint.PointNum]
    secondBestExisting = None
    if dataPoint.PointNum in secondBestScores:
        secondBestExisting = secondBestScores[dataPoint.PointNum]

    if int(dataPoint.Signal) !=0:
        if  int(bestExisting.Signal) != int(dataPoint.Signal) and (secondBestExisting == None or int(secondBestExisting.Signal) < int(dataPoint.Signal)):
            secondBestScores[dataPoint.PointNum] = dataPoint

#Get Best 2.4
for dataPoint in dataPoints:
    bestExisting = None
    if dataPoint.PointNum in bestTwoGigScores:
        bestExisting = bestTwoGigScores[dataPoint.PointNum]
    
    if int(dataPoint.Signal) !=0 and int(0 < int(dataPoint.Channel) < 15):
        if (bestExisting == None or int(bestExisting.Signal) < int(dataPoint.Signal)):
            bestTwoGigScores[dataPoint.PointNum] = dataPoint


#Get Best 5GHz
for dataPoint in dataPoints:
    bestExisting = None
    if dataPoint.PointNum in bestFiveGigScores:
        bestExisting = bestFiveGigScores[dataPoint.PointNum]
    
    if int(dataPoint.Signal) !=0 and int(35 < int(dataPoint.Channel) < 166):
        if (bestExisting == None or int(bestExisting.Signal) < int(dataPoint.Signal)):
            bestFiveGigScores[dataPoint.PointNum] = dataPoint


#At this point I should have the best and second best signal levels saved in list of dicts called primaryAPT and secondaryAPT. This is the best and second best at these points, no matter the band or if they are to APT links



#Get data for best 2.4GHz and best 5GHz connection per point into lists twopointfourgig and fivegig




#Write per point data into list points




#Write data into KML File



