import csv

from data_point import DataPoint

bestScores = dict()
secondBestScores = dict()
bestTwoGigScores = dict()
bestFiveGigScores = dict()

dataPoints = []

peerinfofile = "C:\Code\Projects\meshmapcsv-to-kml\Examples\Meshmapper_2023-08-29_10-50-35_peer_info.csv"
peerinfodata = list(csv.DictReader(open(peerinfofile)))

# Convert CSV into a List of Objects
for row in peerinfodata:
    dataPoint = DataPoint()
    dataPoint.PointNum = row['Point Num']
    dataPoint.Latitude = row['Latitude']
    dataPoint.Longitude = row['Longitude']
    dataPoint.Serial = row['Serial']
    dataPoint.Name = row['Name']
    dataPoint.IP = row['IP']
    dataPoint.WLAN = row['Wlan']
    dataPoint.SNR = row['RSSI (SNR)']
    dataPoint.Cost = row['Cost']
    dataPoint.Signal = row['Signal']
    dataPoint.MAC = row['MAC Address']
    dataPoint.Channel = row['Channel']
    dataPoint.Frequency = row['Frequency']
    dataPoint.Timestamp = row['Timestamp']
    dataPoints.append(dataPoint)

#Add non connect object to be assigned when there is no valid value
noConnection = DataPoint()
#noConnection.PointNum = "No Connection"
#noConnection.Latitude = "No Connection"
#noConnection.Longitude = "No Connection"
noConnection.Serial = "No Connection"
noConnection.Name = "No Connection"
#noConnection.IP = "No Connection"
noConnection.WLAN = "No Connection"
#noConnection.SNR = "No Connection"
#noConnection.Cost = "No Connection"
noConnection.Signal = "-110"
#noConnection.MAC = "No Connection"
#noConnection.Channel = "No Connection"
#noConnection.Frequency = "No Connection"
#noConnection.Timestamp = "No Connection"

# Get Best
for dataPoint in dataPoints:
    bestExisting = None #Create a variable and assign a None Value to it
    if dataPoint.PointNum in bestScores: #Check if dataPoint.PointNum is already in bestScores Dict
        bestExisting = bestScores[dataPoint.PointNum] #if true, assign the current best to the variable best existing to be checked against
    
    if int(dataPoint.Signal) !=0: #Check if the current datapoint has a valid signal reading
        if (bestExisting == None or int(bestExisting.Signal) < int(dataPoint.Signal)): #If first iteration for point num (BestExisting == None) or current row signal better that existing best
            bestScores[dataPoint.PointNum] = dataPoint #Overwrite values for old best with values for new best for point num

# Get Second Best

for dataPoint in dataPoints:
    bestExisting = bestScores[dataPoint.PointNum] #Set bestExisting to values of best score for current point num
    secondBestExisting = None #Create secondBestExisting and set value to None
    if dataPoint.PointNum in secondBestScores: #Check if current pointNum exists in secondBestScores
        secondBestExisting = secondBestScores[dataPoint.PointNum] #if true, set secondBestExisting to current second best
    else:
        secondBestScores[dataPoint.PointNum] = noConnection

    if int(dataPoint.Signal) !=0: #Check if current row has valid signal reading
        #Check if the current row has the same serial number as the best rading for this point to avoid multiple WLANs from same radio
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
print(f'We have loaded [{len(bestTwoGigScores)}] items with 2.4GHz')
print(f'We have loaded [{len(bestFiveGigScores)}] items with 5GHz')

for count in range(1,350):
    best = bestScores[str(count)]
    secondBest = secondBestScores[str(count)] 
    bestTwoGig = bestTwoGigScores[str(count)]
    bestFiveGig = bestFiveGigScores[str(count)]
    print(f'{count} | Best {best.Signal}dBm >> {best.Serial} | Second Best {secondBest.Signal}dBm >> {secondBest.Serial} | Best 2.4GHz  {bestTwoGig.Signal}dBm >> {bestTwoGig.Serial} | Best 5GHz  {bestFiveGig.Signal}dBm >> {bestFiveGig.Serial}')


