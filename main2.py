import csv

from data_point import DataPoint

bestScores = dict()
secondBestScores = dict()

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


print(f'We have loaded [{len(dataPoints)}] items')


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
    
print(f'We have loaded [{len(bestScores)}] items with second highest values')

for count in range(1,20):
    best = bestScores[str(count)]
    secondBest = secondBestScores[str(count)] 
    print(f'{count}-Best [{best.Signal}] >> {best.Serial} Second Best [{secondBest.Signal} >> {secondBest.Serial}]')


