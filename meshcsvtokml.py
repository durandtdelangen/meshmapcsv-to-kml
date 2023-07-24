import csv

csv_file = open('Meshmapper_2023-07-17_13-37-00_peer_info.csv', 'r')
data = list(csv.reader(csv_file, delimiter=','))
csv_file.close()
wlan0 = []
wlan1 = []

for row in data:
    if row[6] == 'wlan0':
        wlan0.append(row)
    elif row[6] == 'wlan1':
        wlan1.append(row)

wlan0_xml = []
wlan1_xml = []

for i in range(len(wlan0)-1):
    #print (wlan0[i][0] + ' ' + wlan0[i+1][0])
    if int(wlan0[i][9]) > -65:
        wlan0_xml.append (f'<Placemark>\n<name>{wlan0[i][0]}</name>\n<LineString>\n<tessellate>1</tessellate>\n<coordinates>{wlan0[i][2]},{wlan0[i][1]} {wlan0[i+1][2]},{wlan0[i+1][1]}</coordinates>\n</LineString>\n<styleUrl>#green_line</styleUrl>\n</Placemark>')
    elif -65 >=int(wlan0[i][9]) > -75:
        wlan0_xml.append (f'<Placemark>\n<name>{wlan0[i][0]}</name>\n<LineString>\n<tessellate>1</tessellate>\n<coordinates>{wlan0[i][2]},{wlan0[i][1]} {wlan0[i+1][2]},{wlan0[i+1][1]}</coordinates>\n</LineString>\n<styleUrl>#yellow_line</styleUrl>\n</Placemark>')
    elif -75 >=int(wlan0[i][9]) > -85:
        wlan0_xml.append (f'<Placemark>\n<name>{wlan0[i][0]}</name>\n<LineString>\n<tessellate>1</tessellate>\n<coordinates>{wlan0[i][2]},{wlan0[i][1]} {wlan0[i+1][2]},{wlan0[i+1][1]}</coordinates>\n</LineString>\n<styleUrl>#orange_line</styleUrl>\n</Placemark>')
    else:
        wlan0_xml.append (f'<Placemark>\n<name>{wlan0[i][0]}</name>\n<LineString>\n<tessellate>1</tessellate>\n<coordinates>{wlan0[i][2]},{wlan0[i][1]} {wlan0[i+1][2]},{wlan0[i+1][1]}</coordinates>\n</LineString>\n<styleUrl>#red_line</styleUrl>\n</Placemark>')

for i in range(len(wlan1)-1):
    #print (wlan0[i][0] + ' ' + wlan0[i+1][0])
    if int(wlan1[i][9]) > -65:
        wlan1_xml.append (f'<Placemark>\n<name>{wlan1[i][0]}</name>\n<LineString>\n<tessellate>1</tessellate>\n<coordinates>{wlan1[i][2]},{wlan1[i][1]} {wlan1[i+1][2]},{wlan1[i+1][1]}</coordinates>\n</LineString>\n<styleUrl>#green_line</styleUrl>\n</Placemark>')
    elif -65 >=int(wlan0[i][9]) > -75:
        wlan1_xml.append (f'<Placemark>\n<name>{wlan1[i][0]}</name>\n<LineString>\n<tessellate>1</tessellate>\n<coordinates>{wlan1[i][2]},{wlan1[i][1]} {wlan1[i+1][2]},{wlan1[i+1][1]}</coordinates>\n</LineString>\n<styleUrl>#yellow_line</styleUrl>\n</Placemark>')
    elif -75 >=int(wlan0[i][9]) > -85:
        wlan1_xml.append (f'<Placemark>\n<name>{wlan1[i][0]}</name>\n<LineString>\n<tessellate>1</tessellate>\n<coordinates>{wlan1[i][2]},{wlan1[i][1]} {wlan1[i+1][2]},{wlan1[i+1][1]}</coordinates>\n</LineString>\n<styleUrl>#orange_line</styleUrl>\n</Placemark>')
    else:
        wlan1_xml.append (f'<Placemark>\n<name>{wlan1[i][0]}</name>\n<LineString>\n<tessellate>1</tessellate>\n<coordinates>{wlan1[i][2]},{wlan1[i][1]} {wlan1[i+1][2]},{wlan1[i+1][1]}</coordinates>\n</LineString>\n<styleUrl>#red_line</styleUrl>\n</Placemark>')


#Open KML File and Write lists to kml file
with open ('meshmapper.kml', 'w') as kml_file:
    kml_file.write ('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml_file.write ('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kml_file.write ('<Document>\n')
    kml_file.write ('<Style id="green_line">\n')
    kml_file.write ('<LineStyle>\n')
    kml_file.write ('<color>ff30ad3e</color>\n')
    kml_file.write ('<width>5</width>\n')
    kml_file.write ('</LineStyle>\n')
    kml_file.write ('</Style>')
    kml_file.write ('<Style id="yellow_line">\n')
    kml_file.write ('<LineStyle>\n')
    kml_file.write ('<color>7f00ffff</color>\n')
    kml_file.write ('<width>5</width>\n')
    kml_file.write ('</LineStyle>\n')
    kml_file.write ('</Style>')
    kml_file.write ('<Style id="orange_line">\n')
    kml_file.write ('<LineStyle>\n')
    kml_file.write ('<color>ff006af2</color>\n')
    kml_file.write ('<width>5</width>\n')
    kml_file.write ('</LineStyle>\n')
    kml_file.write ('</Style>')
    kml_file.write ('<Style id="red_line">\n')
    kml_file.write ('<LineStyle>\n')
    kml_file.write ('<color>ff0000ff</color>\n')
    kml_file.write ('<width>5</width>\n')
    kml_file.write ('</LineStyle>\n')
    kml_file.write ('</Style>')
    kml_file.write ('<Folder>\n<name>wlan0</name>\n')
    for row in wlan0_xml:
        kml_file.write(row + "\n")
    kml_file.write('</Folder>')
    kml_file.write ('<Folder>\n<name>wlan1</name>\n')
    for row in wlan1_xml:
        kml_file.write(row + "\n")
    kml_file.write('</Folder>\n')
    kml_file.write ('</Document>\n')
    kml_file.write ('</kml>')

