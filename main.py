import csv

from data_point import DataPoint

#Open CSV Files
#peerinfofile = input("Enter the path to the peer info file: ")
peerinfofile = "C:\Code\Projects\meshmapcsv-to-kml\Examples\Meshmapper_2023-08-29_10-50-35_peer_info.csv"
peerinfodata = list(csv.DictReader(open(peerinfofile)))

#TODO - Add import list of APT serials

#Declare lists for writing kml
bestScores = dict()
secondBestScores = dict()
bestTwoGigScores = dict()
bestFiveGigScores = dict()

# Convert CSV into a List of Objects
dataPoints = []
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
noConnection.Serial = "No Connection"
noConnection.Name = "No Connection"
noConnection.WLAN = "No Connection"
noConnection.Signal = "-110"

# Get radio with best signal at all points
for dataPoint in dataPoints:
    bestExisting = None
    if dataPoint.PointNum in bestScores:
        bestExisting = bestScores[dataPoint.PointNum]
    
    if int(dataPoint.Signal) !=0:
        if (bestExisting == None or int(bestExisting.Signal) < int(dataPoint.Signal)):
            bestScores[dataPoint.PointNum] = dataPoint

#Get radio with Second Best signal at all points
for dataPoint in dataPoints:
    bestExisting = bestScores[dataPoint.PointNum]
    secondBestExisting = None
    if dataPoint.PointNum in secondBestScores:
        secondBestExisting = secondBestScores[dataPoint.PointNum]
    else:
        secondBestScores[dataPoint.PointNum] = noConnection

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

#Write data into KML File

#Write best connections to kml
for count in bestScores:
    score = bestScores[str(count)]
    if int(score.Signal) > -65:
        linesToWrite = ['<Placemark>\n',
                        f'<name>{score.PointNum}</name>\n',
                        '<styleUrl>#good_pin</styleUrl>\n',
                        f'<Point><coordinates>{score.Longitude},{score.Latitude},0</coordinates></Point>\n',
                        f'<description>Signal: {score.Signal}\nTo: {score.Name}\nOn: {score.WLAN}</description>\n',
                        '</Placemark>\n']
        print (linesToWrite)
    elif -65 > int(score.Signal) >= -75:
        linesToWrite = ['<Placemark>\n',
                        f'<name>{score.PointNum}</name>\n',
                        '<styleUrl>#acceptable_pin</styleUrl>\n',
                        f'<Point><coordinates>{score.Longitude},{score.Latitude},0</coordinates></Point>\n',
                        f'<description>Signal: {score.Signal}\nTo: {score.Name}\nOn: {score.WLAN}</description>\n',
                        '</Placemark>\n']
        print (linesToWrite)
    elif -75 > int(score.Signal) >= -85:
        linesToWrite = ['<Placemark>\n',
                        f'<name>{score.PointNum}</name>\n',
                        '<styleUrl>#fair_pin</styleUrl>\n',
                        f'<Point><coordinates>{score.Longitude},{score.Latitude},0</coordinates></Point>\n',
                        f'<description>Signal: {score.Signal}\nTo: {score.Name}\nOn: {score.WLAN}</description>\n',
                        '</Placemark>\n']
        print (linesToWrite)
    elif -85 > int(score.Signal) >= -100:
        linesToWrite = ['<Placemark>\n',
                        f'<name>{score.PointNum}</name>\n',
                        '<styleUrl>#bad_pin</styleUrl>\n',
                        f'<Point><coordinates>{score.Longitude},{score.Latitude},0</coordinates></Point>\n',
                        f'<description>Signal: {score.Signal}\nTo: {score.Name}\nOn: {score.WLAN}</description>\n',
                        '</Placemark>\n']
        print (linesToWrite)
    else:
        linesToWrite = ['<Placemark>\n',
                        f'<name>{score.PointNum}</name>\n',
                        '<styleUrl>#noconnect_pin</styleUrl>\n',
                        f'<Point><coordinates>{score.Longitude},{score.Latitude},0</coordinates></Point>\n',
                        f'<description>Signal: {score.Signal}\nTo: {score.Name}\nOn: {score.WLAN}</description>\n',
                        '</Placemark>\n']
        print (linesToWrite)
