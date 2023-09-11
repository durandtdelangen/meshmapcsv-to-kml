import csv

from data_point import DataPoint

#Open CSV Files
#peerinfofile = input("Enter the path to the peer info file: ")
peerinfofile = "C:\Code\Projects\meshmapcsv-to-kml\Examples\Meshmapper_2023-08-29_10-50-35_peer_info.csv"
peerinfodata = list(csv.DictReader(open(peerinfofile)))
exportfile = open("Examples/terminalexport.txt", "w") #debug code
primaryfile = open("Examples/primaryexport.txt", "w") #debug code
secondaryfile = open("Examples/secondaryexport.txt", "w") #debug code
#Add import list of APT serials

#Declare lists for writing kml
points = []
bestScores = dict()
secondBestScores = dict()

dataPoints = []

# Get Best
for dataPoint in dataPoints:
    bestExisting = None
    if dataPoint.PointNum in bestScores:
        bestExisting = bestScores[dataPoint.PointNum]

    if bestExisting == None or bestExisting.Signal > dataPoint.Signal:
        bestScores[dataPoint.PointNum] = dataPoint

print(f'We have loaded [{len(bestScores)}] items with highest values')


# Get Second Best
for dataPoint in dataPoints:
    bestExisting = bestScores[dataPoint.PointNum]
    secondBestExisting = None
    if dataPoint.PointNum in secondBestScores:
        secondBestExisting = secondBestScores[dataPoint.PointNum]

    if  bestExisting.Signal != dataPoint.Signal and (secondBestExisting == None or secondBestExisting.Signal > dataPoint.Signal):
        secondBestScores[dataPoint.PointNum] = dataPoint
    

#At this point I should have the best and second best signal levels saved in list of dicts called primaryAPT and secondaryAPT. This is the best and second best at these points, no matter the band or if they are to APT links



#Get data for best 2.4GHz and best 5GHz connection per point into lists twopointfourgig and fivegig




#Write per point data into list points




#Write data into KML File



