import csv

from data_point import DataPoint

bestScores = dict()
secondBestScores = dict()
bestTwoGigScores = dict()
bestFiveGigScores = dict()

dataPoints = []

peerinfofile = "C:\Code\Projects\meshmapcsv-to-kml\Examples\Meshmapper_2023-08-29_10-50-35_peer_info.csv"
peerinfodata = list(csv.DictReader(open(peerinfofile)))

# Convert CSV into an List of Objects
for row in peerinfodata:
    dataPoint = DataPoint()
    dataPoint.PointNum = row['Point Num']
    dataPoint.Latitude = row['Latitude']
    dataPoint.Longitude = row['Longitude']
    dataPoint.Serial = row['Serial']
    dataPoint.Name = row['Name']
    dataPoint.Signal = row['Signal']
    dataPoint.Channel = row['Channel']
    dataPoints.append(dataPoint)

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
        if  bestExisting.Serial != dataPoint.Serial and (secondBestExisting == None or int(secondBestExisting.Signal) < int(dataPoint.Signal)):
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

print(f'We have loaded [{len(bestScores)}] items with highest values')
print(f'We have loaded [{len(secondBestScores)}] items with second highest values')

for count in range(1,20):
    best = bestScores[str(count)]
    secondBest = secondBestScores[str(count)] 
    bestTwoGig = bestTwoGigScores[str(count)]
    bestFiveGig = bestFiveGigScores[str(count)]
    print(f'{count} | Best {best.Signal}dBm >> {best.Serial} | Second Best {secondBest.Signal}dBm >> {secondBest.Serial} | Best 2.4GHz  {bestTwoGig.Signal}dBm >> {bestTwoGig.Serial} | Best 5GHz  {bestFiveGig.Signal}dBm >> {bestFiveGig.Serial}')


