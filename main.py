import csv

#Open CSV Files
#peerinfofile = input("Enter the path to the peer info file: ")
peerinfofile = "C:\Code\Projects\meshmapcsv-to-kml\Examples\Meshmapper_2023-08-29_10-50-35_peer_info.csv"
peerinfodata = list(csv.DictReader(open(peerinfofile)))
exportfile = open("Examples/terminalexport.txt", "w")
primaryfile = open("Examples/primaryexport.txt", "w")

#Declare lists for writing kml
primaryAPT = []
secondaryAPT = []
twopointfourgig = []
fivegig = []
points = []
best = {'Point Num': '', 'Latitude': '', 'Longitude': '', 'Serial': '', 'Name': '', 'IP': '', 'Wlan': '', 'RSSI (SNR)': '', 'Cost': '', 'Signal': '-108', 'MAC Address': '', 'Channel': '', 'Frequency': '', 'Timestamp': ''}
second = {'Point Num': '', 'Latitude': '', 'Longitude': '', 'Serial': '', 'Name': '', 'IP': '', 'Wlan': '', 'RSSI (SNR)': '', 'Cost': '', 'Signal': '-108', 'MAC Address': '', 'Channel': '', 'Frequency': '', 'Timestamp': ''}

#Get data for lists
lastpoint = int(peerinfodata[-1]["Point Num"]) #Get point number of last point in list

for point in range(1, lastpoint+1):
    for row in peerinfodata:
        if int(row['Point Num']) == point:
            if (int(row['Signal']) > int(best['Signal'])) & (int(row['Signal']) != 0):
                second = best
                best = row
            elif (int(row['Signal']) > int(second['Signal'])) & (int(row['Signal']) != 0):
                second = row
    #exportfile.write(f"{best['Point Num']} {best['Signal']} {second['Signal']}\n")
    primaryAPT.append(best)
    secondaryAPT.append(second)
    best['Signal'] = -108
    second['Signal'] = -108

#At this point I have the best and second best signal levels saved in list of dicts called primaryAPT and secondaryAPT. This is the best and second best at these points, no matter the band or if they are to APT links

    