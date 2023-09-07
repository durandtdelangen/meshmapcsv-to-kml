import csv

#Open CSV Files
#peerinfofile = input("Enter the path to the peer info file: ")
peerinfofile = "C:\Code\Projects\meshmapcsv-to-kml\Examples\Meshmapper_2023-08-29_10-50-35_peer_info.csv"
peerinfodata = list(csv.DictReader(open(peerinfofile)))
exportfile = open("Examples/terminalexport.txt", "w")
primaryfile = open("Examples/primaryexport.txt", "w")
secondaryfile = open("Examples/secondaryexport.txt", "w")

#Declare lists for writing kml
primaryAPT = []
secondaryAPT = []
twopointfourgig = []
fivegig = []
points = []
best = {'Point Num': '', 'Latitude': '', 'Longitude': '', 'Serial': '', 'Name': '', 'IP': '', 'Wlan': '', 'RSSI (SNR)': '', 'Cost': '', 'Signal': '', 'MAC Address': '', 'Channel': '', 'Frequency': '', 'Timestamp': ''}
second = {'Point Num': '', 'Latitude': '', 'Longitude': '', 'Serial': '', 'Name': '', 'IP': '', 'Wlan': '', 'RSSI (SNR)': '', 'Cost': '', 'Signal': '', 'MAC Address': '', 'Channel': '', 'Frequency': '', 'Timestamp': ''}

#Get data for lists
lastpoint = int(peerinfodata[-1]["Point Num"]) #Get point number of last point in list

for point in range(1, lastpoint+1):
    best['Signal'] = -108
    second['Signal'] = -108
    for row in peerinfodata: #get best and second best Signal level at point for valid readings
        if int(row['Point Num']) == point:
            if (int(row['Signal']) > int(best['Signal'])) & (int(row['Signal']) != 0):
                second = best
                best = row
            elif (int(row['Signal']) > int(second['Signal'])) & (int(row['Signal']) != 0):
                second = row
    linetowrite = (f"{best['Point Num']} {best['Serial']} {best['Name']} {best['Wlan']} {best['Signal']} {second['Serial']} {second['Name']} {second['Wlan']} {second['Signal']}\n") #debug code
    exportfile.writelines(linetowrite) #debug code
    primaryAPT.append(best)
    secondaryAPT.append(second)
    print (f"{point} {primaryAPT[point-1]}") #debug code
    print (f"{point} {primaryAPT[point-2]}") #debug code
    #best['Signal'] = -109
    #second['Signal'] = -108
    

#At this point I should have the best and second best signal levels saved in list of dicts called primaryAPT and secondaryAPT. This is the best and second best at these points, no matter the band or if they are to APT links
#print (primaryAPT)
for i in primaryAPT:#debug code
    linetowrite = (f"Point Num: {i['Point Num']} Serial: {i['Serial']} Name: {i['Name']} Best signal: {i['Signal']}\n")#debug code
    primaryfile.writelines(linetowrite) #debug code

for i in secondaryAPT:#debug code
    linetowrite = (f"Point Num: {i['Point Num']} Serial: {i['Serial']} Name: {i['Name']} Best signal: {i['Signal']}\n")#debug code
    secondaryfile.writelines(linetowrite) #debug code


#Get data for best 2.4GHz and best 5GHz connection per point into lists twopointfourgig and fivegig




#Write per point data into list points




#Write data into KML File



